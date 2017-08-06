# bgg-owned-games

At this point this is a really basic project - it reads in a list of boardgamegeek users and writes the games they own out to a spreadsheet on Google.
I threw it together in a couple hours on a whim, to be able to easily be able to see what games other gamers in a group own.
It prints out to a google sheet all the games owned by people in your group (listed by ranking on BGG) as well as a list of people that own that game

I am open to contributions, even ones that drastically change the structure of the project, as long as they only add functionality, and don't remove any.

### Screenshot
<img width="395" alt="screen shot 2017-08-05 at 6 40 36 pm" src="https://user-images.githubusercontent.com/17733030/28999678-e17dd2c6-7a0d-11e7-8ac1-90e4bfd5e564.png">

### Using this for your group
1. Clone the repository.
2. Create a file named usernames.csv in the directory where you will be running the script, I do it in the root folder of the repo (formatted "Person,username")
3. Create a project through the Google API Console and get credentials to hit the google sheets api, as explained [here](https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html).
Put the credentials file (name it client-secret.json) in the directory where you will be running the script.
4. Create a spreadsheet named "Games" in Google Drive and share it to the email associated with the credentials created in step 3.
5. Using launchd, cron, or some other utility, set up the script to run at some specified interval. A sample launchd configuration file is given below.
6. Share the spreadsheet created in step 4 with your group.

#### Sample launchd config file
Note that this only works on mac, but apple recommends you use it over cron on mac
1. Go to ~/Library/LaunchAgents
2. Create a file called local.bgg.plist, that contains the following: (more info about plist files [here](http://www.launchd.info/))
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>Label</key>
	<string>local.bgg</string>
	<key>Program</key>
	<string>/path/to/repo/run.sh</string>
	<key>WorkingDirectory</key>
	<string>/path/to/working/directory</string>
	<key>EnvironmentVariables</key>
	<!-- make git, grep, sed accessible -->
	<dict>
		<key>PATH</key>
		<string>/bin:/usr/bin:/usr/local/bin</string>
	</dict>
	<!-- run every morning at 6 (or when the computer wakes up if it's sleeping at 6 -->
	<key>StartCalendarInterval</key>
	<dict>
		<key>Hour</key>
		<integer>6</integer>
		<key>Minute</key>
		<integer>0</integer>
	</dict>
	<!-- also run whenever the usernames file is updated -->
	<key>WatchPaths</key>
	<array>
		<string>/path/to/usernames.csv</string>
	</array>
	<key>StandardOutPath</key>
	<string>/tmp/bgg.stdout</string>
	<key>StandardErrorPath</key>
	<string>/tmp/bgg.stdout</string>
</dict>
</plist>
```
3. Run `launchctl load ~/Library/LaunchAgents/local.bgg.plist`
