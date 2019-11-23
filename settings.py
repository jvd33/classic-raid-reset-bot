"""settings.py"""
from constants import Raids, Days


class BotSettings(object):

    def __init__(self, **kwargs):
        self.__dict__.update(**kwargs)

    """
     - realm_region: EU, US
                    - Default: US
            - realm_time_zone: EST, PST, CST, etc
                    - Default: EST
            - notifications_enabled: bool - Automatically send messages to the channel printing the raid reset day/time for the configured raids
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
    __slots__ = ['realm_region', 'realm_time_zone', 'notifications_enabled', 'notification_schedule', 'raids_enabled',
                 'raid_days', 'alert_double_reset', '__dict__']

    @staticmethod
    def default():

        defaults = {
            'realm_region': 'US',
            'realm_time_zone': 'EST',
            'notifications_enabled': True,
            'notification_schedule': [0, 1, 3],
            'raids_enabled': [Raids.MoltenCore, Raids.Onyxia],
            'raid_days': [Days.Wednesday, Days.Thursday],
            'alert_double_reset': True
        }
        return BotSettings(**defaults)

    def __str__(self):
        return f"""
                Realm Region: {self.realm_region}\n
                Realm Time Zone: {self.realm_time_zone}\n
                Notifications Enabled: {self.notifications_enabled}\n
                Notification Schedule: {self.notification_schedule}\n
                Raids Enabled: {self.raids_enabled}\n
                Raid Days: {self.raid_days}\n
                Alert Double Resets?: {self.alert_double_reset}
                """
