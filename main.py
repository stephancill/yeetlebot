import os
import random
import sys
import telepot
from telepot.loop import MessageLoop


def chat_handler(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	print(content_type, chat_type, chat_id)

	if content_type == 'text':
		if msg['text'].lower()[:len("/yeet")] == "/yeet":
			bot.sendMessage(chat_id, "yeet")
		elif "?" in msg['text'].lower() and random.random() < 0.05:
			bot.sendMessage(chat_id, "yeet", reply_to_message_id=msg['message_id'])

if __name__ == "__main__":
	BOT_TOKEN = None
	try:
		BOT_TOKEN = os.environ["BOT_TOKEN"] #Hosting the bot on Heroku
	except KeyError:
		BOT_TOKEN = sys.argv[1] 

	#make our bot and feed it the tokenhend
	bot = telepot.Bot(BOT_TOKEN)

	#fetch messages and keep script looped
	bot.message_loop({'chat' : chat_handler},
					  run_forever="Bot Running...")
