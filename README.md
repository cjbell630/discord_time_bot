# Usage
Once the bot is running, use this syntax to convert a time:

    !time convert [TIME_TO_CONVERT] [CURRENT_LOCAL_TIME]
    
With all times being in HH:mm 24-hour format.

Here's an example. It currently says "2:47 PM" on your PC clock,
and you want to let others know about an event at 8:00 PM your
time. To give them a conversion link, you would run: 
    
    !time convert 20:00 14:47
    
Then, anyone who wants to know what that is in their timezone
could simply click the generated link.

# IMPORTANT
This is a Discord bot where users can supply a target time,
along with their current local time, and a URL will be generated.

When opened, this URL will convert the supplied time into the
client's local time, as it is known by their web browser.

The HTML page looks like garbage, and I'm sure someone else has
done it better, but you can use mine if you want. If you do,
please be aware that I made this for fun, mostly as a proof of
concept for myself, and because of that, it hasn't been
thoroughly tested.

Taking to heart [the wise words of Tom Scott][1], I attempted
to create this project without having to deal with timezones.
That's the reason for the "current local time" parameter to
the bot. With this, the code can extract how long it is until
the specified time, and simply give a client-side script the
time the message was called and the duration from that time
to display. However, this is not without its problems.

Any time-skip (such as Daylight Savings time or Leap Day) will
cause this method to fail if it falls between the time the
message was sent and the target time in the sender's time zone.

For example, if it was 10:00 AM, and the time increased by one
hour at 3:00 AM in my time zone (ex DST), and there was some
event at 2:00 PM the next day I wanted to tell people about,
I would run this command:

    !time convert 14:00 10:00
    
Given this, the bot would calculate that the was referring to
an event taking place in 22 hours. This is wrong, however,
because one hour is skipped over that night. In reality, the
event is in 21 hours. Even if the user viewing the URL also
has the same time skip, it will still fail.

There are probably many other issues with this method,
but I have yet to come across them. If you do use this bot,
please let me know of any issues you come across!

[1]: <https://www.youtube.com/watch?v=-5wpm-gesOY> "click me to hear said words"