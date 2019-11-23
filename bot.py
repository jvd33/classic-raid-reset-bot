"""raid_reset_bot.py"""
import os
import shelve
import datetime
import pytz

from dotenv import load_dotenv
from discord.ext import commands

from dateutils import get_localized_reset_time
from settings import BotSettings
from data import RedisClient

class RaidResetBot(commands.Bot):

    def __init__(self, *args, **kwargs):
        super(RaidResetBot, self).__init__(*args, **kwargs)
        load_dotenv()
        self.token = os.getenv('TOKEN')
        self._register_commands()
        self.redis = RedisClient()
        self.date_fmt = '%A, %B %d'

    def _register_commands(self):
        registry = {
            'heartbeat': self.heartbeat,
            'getReset': self.print_reset_date,
            'config': self.configure,
            'calendar': self.display_calendar,
        }

        [self.command(name=name)(func) for name, func in registry.items()]
        self.event(self.on_guild_join)

    def run_stateful(self):
        self.run(self.token)

    async def heartbeat(self, ctx):
        """
        Responds with 'OK' and your current configuration settings if the bot is operational. No response indicates an error state.
        """
        guild_id = str(ctx.guild.id)
        await ctx.send(f'OK: {self._get_guild_settings(guild_id)}')

    async def print_reset_date(self, ctx, raid: str):
        """ 
        Gets the next reset date of the raid specified in the 'raid' argument.
        params: Raid: The raid to output the reset date for.
                - ['Onyxia', 'MC', 'ZG', 'Naxxramas', 'BWL', 'AQ20', 'AQ40']
        """
        reset = self.redis.get_raid_reset(raid)
        settings = self.redis.get_guild_config(str(ctx.guild.id))
        tz = pytz.timezone(settings.realm_time_zone)
        server_reset_time = get_localized_reset_time(settings.realm_region, tz)
        if reset:
            reset = datetime.datetime.strptime(reset)
            localized = tz.localize(reset)
            await ctx.send(f'{raid} resets on {localized.strftime(self.date_fmt)} at {server_reset_time}.')

    async def configure(self, ctx, setting: str, value: str):
        """
        ?configure <setting_name> <setting_value>
        Configures the bot for your specific server, and persists the settings. 
        Configuration settings:
            - realm_region: EU, US
                    - Default: US
            - realm_time_zone: The time zone your server is hosted in
                    - Default: America/New York - valid values are any of the timezone names from the standard tz database.
            - notifications: bool - Automatically send messages to the channel printing the raid reset day/time for the configured raids. Accepts most "truthy" string values, like true, false, y, n, yes, no, etc.
                    - Default: True
            - notification_schedule: Integer array of the # of days before reset to notify the channel.
                0 = notify on reset day that the raid has reset, and output the next reset.
                    - Default: [0, 1, 3]
            - raids_enabled: The raids to enable notifications for.
                    - Default: [MC, Onyxia]
            - raid_days: This is used for calculating double reset periods based on your configured raid schedule.
                    - Default: [3, 4]
                    - 1: Monday
                    - 2: Tuesday
                    - 3: Wednesday
                    - 4: Thursday
                    - 5: Friday
                    - 6: Saturday
                    - 7: Sunday
            - alert_double_reset: bool - Whether or not the mention in the reset notification that this week is a double reset week for the given raid_days.
                    - Default: True
        """
        guild_id = str(ctx.guild.id)
        if setting in BotSettings.props:
            is_valid = BotSettings.validate_str_input(val)
            if is_valid:
                settings = self.redis.get_guild_config(guild_id)
                settings[setting] = value
                self.redis.set_guild_config(settings)
                ctx.send(f'Settings successfully updated, new Guild Settings: {settings}')
            ctx.send(f'Invalid value for setting {setting}. See ?help for more information.')
        ctx.send(f'Invalid setting name, valid setting names: {BotSettings.props}')


    async def on_guild_join(self, guild):
        guild_id = str(guild.id)
        defaults = BotSettings.default()
        self.redis.set_guild_config(defaults)
        

    async def display_calendar(self):
        pass


if __name__ == '__main__':
    bot = RaidResetBot(command_prefix='?')

    bot.run_stateful()
