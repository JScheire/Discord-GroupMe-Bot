# Discord GroupMe Bot

Python Script that will send messages from a specified channel to a GroupMe group chat.

## Install Dependencies

```
cd discord-groupme-bot
pip install -r requirements.txt
```

## Discord Bot

First, create a [Discord bot](https://discord.com/developers/applications) and invite it to your server, making sure that you make sure it can view channels and messages when generating the URL.

## GroupMe Bot

Next, create a GroupMe bot at https://dev.groupme.com/bots.

## Set environment variables

In the `.env` file, set the `DISCORD_TOKEN` to the Discord bot's token, the `GROUPME_BOT_ID` to the GroupMe bot id given on the GroupMe developer website, and the `CHANNEL_NAME` to the desired discord channel name.

## Running the bot
Finally, run `python bot.py` to run the bot.
