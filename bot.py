"""raid_reset_bot.py"""
import os
import shelve
import datetime

from dotenv import load_dotenv
from discord.ext import commands

from settings import BotSettings


class RaidResetBot(commands.Bot):

    def __init__(self, *args, **kwargs):
        super(RaidResetBot, self).__init__(*args, **kwargs)
        load_dotenv()
        self.token = os.getenv('TOKEN')
        self._register_commands()

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
        await ctx.send(datetime.datetime.now())

    async def configure(self, ctx):
        """
        Configures the bot for your specific server, and persists the settings.
        Configuration settings:
            - realm_region: EU, US
                    - Default: US
            - realm_time_zone: EST, PST, CST, etc
                    - Default: EST
            - notifications: bool - Automatically send messages to the channel printing the raid reset day/time for the configured raids
                    - Default: True
            - notification_schedule: Integer array of the # of days before reset to notify the channel.
                0 = notify on reset day that the raid has reset, and output the next reset.
                    - Default: [0, 1, 3]
            - raids_enabled: The raids to enable notifications for.
                    - Default: ['MC', 'Onyxia']
            - raid_days: This is used for calculating double reset periods based on your configured raid schedule.
                    - Default: [3, 4]
                    - 0: Sunday
                    - 1: Monday
                    - 2: Tuesday
                    - 3: Wednesday
                    - 4: Thursday
                    - 5: Friday
                    - 6: Saturday
            - alert_double_reset: bool - Whether or not the mention in the reset notification that this week is a double reset week for the given raid_days.
                    - Default: True
        """
        pass

    async def on_guild_join(self, guild):
        guild_id = str(guild.id)
        with shelve.open('setting_state') as d:
            guild_settings = self._get_guild_settings(guild_id)
            if not guild_settings:
                d[guild_id] = str(BotSettings.default())
            return d[guild_id]

    async def display_calendar(self):
        pass

    def _get_guild_settings(self, guild_id):
        with shelve.open('setting_state') as d:
            return d.get(guild_id, None)


if __name__ == '__main__':
    bot = RaidResetBot(command_prefix='?')

    bot.run_stateful()
