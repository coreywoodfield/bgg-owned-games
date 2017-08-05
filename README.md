# bgg-owned-games

At this point this is a really basic project - it reads in a list of boardgamegeek users and writes the games they own out to a spreadsheet on Google.
I threw it together in a couple hours on a whim, to be able to easily be able to see what games other gamers in a group own.

I am open to contributions, even ones that drastically change the structure of the project, as long as they only add functionality, and don't remove any.


### Using this for your group
1. Clone the repository.
2. Create a file named usernames.csv in the directory where you will be running the script, I do it in the root folder of the repo.
3. Create a project through the Google API Console and get credentials to hit the google sheets api, as explained [here](https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html).
Put the credentials file (name it client-secret.json) in the directory where you will be running the script.
4. Create a spreadsheet named "Games" in Google Drive and share it to the email associated with the credentials created in step 3.
5. Using launchd, cron, or some other utility, set up the script to run at some specified interval.
6. Share the spreadsheet created in step 4 with your group.
