import datetime
import pytz

def get_localized_reset_time(region, realm_time_zone):
    date_fmt = '%I:%M %p'
    return {
        'US': lambda x: datetime.datetime.time(hour=16, tzinfo=pytz.utc).astimezone(realm_time_zone).strftime(date_fmt),
        'EU': lambda x: datetime.datetime.time(hour=7, tzinfo=pytz.utc).astimezone(realm_time_zone).strftime(date_fmt)
    }.get(region)
