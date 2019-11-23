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
    __slots__ = ['__dict__', 'realm_region', 'realm_time_zone', 'notifications_enabled', 'notification_schedule', 'raids_enabled',
                 'raid_days', 'alert_double_reset']

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
    
    @property
    def props(self):
        return ['realm_region', 'realm_time_zone', 'raids_enabled', 'raid_days', 'alert_double_reset', 'notifications_enabled', 
                'notification_schedule']
    @staticmethod
    def validate_str_input(setting: str, val: str):
        val_arrays = {
            'realm_region': lambda x: return x.lower() in ['us', 'eu'],
            'realm_time_zone': lambda x: return x.lower() in ['est', 'cst', 'pst'],
            'raids_enabled': lambda x: return x.lower() in [Raids.MoltenCore, Raids.Onyxia, Raids.ZulGurub, Raids.Naxxramas, Raids.AQForty, Raids.AQTwenty],
            'raid_days': lambda x: return x.lower() in [Days.Monday, Days.Tuesday, Days.Wednesday, Days.Thursday, Days.Friday, Days.Saturday, Days.Sunday],
            'alert_double_reset': lambda x: return x.lower() in ['true', 'false', 't', 'f', 'yes', 'no', 'y', 'n'],
            'notifications_enabled': lambda x: return x.lower() in ['true', 'false', 't', 'f', 'yes', 'no', 'y', 'n'],
            'notification_schedule': lambda x: return all([i.isdigit() for i in x.split(',')])
        }
        return True if val_arrays.get(setting, None) := func and func(val) else False


    def __str__(self):
        return f'
                Realm Region: {self.realm_region}\n
                Realm Time Zone: {self.realm_time_zone}\n
                Notifications Enabled: {self.notifications_enabled}\n
                Notification Schedule: {self.notification_schedule}\n
                Raids Enabled: {self.raids_enabled}\n
                Raid Days: {self.raid_days}\n
                Alert Double Resets?: {self.alert_double_reset}
                '
