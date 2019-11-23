# Classic-Raid-Reset-Bot
This Discord bot helps keep track of Raid Resets in Classic WoW, like Onyxia's 5 day reset.

This is so we don't miss boss kills and everyone is aware of when each raid resets.

### Features
   * Molten Core, Onyxia, Naxxramas, Blackwing Lair, AQ20, AQ40 raid reset tracking. 
   * Custom raid schedules so you can notify your guild when you are able to kill Onyxia twice in the same raid week
        * see `?config` command
   * Custom notification cadences (1 day before reset, 3 days before reset, day of reset, etc)
        * see `?config` command
   * Custom realm regions and timezones
   * Enable/disable notifications on a per-raid basis (don't alert on Molten Core resets, but DO alert Onyxia for example)

#### Commands
* `?heartbeat`
    * Responds with 'OK' and your current configuration settings if the bot is operational. No response indicates an error state.
* `?getReset <raid: str>`
    * Gets the next reset date of the raid specified in the 'raid' argument.
    * `raid`: The raid to output the reset date for.
        * Valid Values: `['Onyxia', 'MC', 'ZG', 'Naxxramas', 'BWL', 'AQ20', 'AQ40']`
* `?configure`
    *  Configures the bot for your specific server, and persists the settings.
        * Configuration settings:
            - `realm_region`: 
                * Valid Values: `['EU', 'US']` 
                * Default: `US`
            - `realm_time_zone`: 
                * Valid Values: `['EST', 'PST', 'CST', ...]` etc
                * Default: `EST`
            - `notifications`: Automatically send messages to the channel printing the raid reset day/time for the configured raids
                * Valid Values: `[True, False]`
                * Default: True
            - `notification_schedule`: Integer array of the # of days before reset to notify the channel. 0 = notify on reset day that the raid has reset, and output the next reset.
                * Valid Values: `[0, 1, 2, 3, 4, 5, 6, 7]`
                * Default: `[0, 1, 3]` - The day of reset, 1 day before reset, 3 days before reset.
            - `raids_enabled`: The raids to enable notifications for.
                * Valid Values: `['MC', 'Onyxia', 'BWL', 'AQ20', 'AQ40', 'ZG', 'Naxxramas']`
                * Default: `['MC', 'Onyxia']`
            - `raid_days`: This is used for calculating double reset periods based on your configured raid schedule. Integer representations of day of the week, with 0 being Sunday.
                * Valid Values: `[0, 1, 2, 3, 4, 5, 6]`
                * Default: `[3, 4]`
            * `alert_double_reset` Whether or not the mention in the reset notification that this week is a double reset week for the given raid_days.
                * Valid Values: `[True, False]`
                * Default: `True`
                
    * `?calendar <start_date> <end_date> <optional: raid>`
        * Display a calendar visually laying out the raid reset days for the given time range. 
        * **NOTE: start_date cannot be in the past or more than 30 days into the future, and the difference between the `start_date` and `end_date` can't span more than a month.**
            * `start_date`: `YYYY-MM-dd` formatted date string representing the day to start the calendar on.
            * `end_date`: `YYYY-MM-dd` formatted date string representing the day to end the calendar on.
            * `raid`
                * Valid Values: `['MC', 'Onyxia', 'BWL', 'AQ20', 'AQ40', 'ZG', 'Naxxramas']`
    * `?help <optional: command_name>`
        * Display the help dialog, optionally for the given command
        
        

#### Info
* [Github](github.com/jvd33/ClassicRaidResetBot)
* [Discord]()


##### WoW 
* Aemin < Dirty > @ Skeram (US-PvP)