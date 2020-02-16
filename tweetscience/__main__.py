import os
from telegram.ext import Updater, MessageHandler, Filters
import logging
import twitter

api = twitter.Api(consumer_key=os.environ.get("TWITTER_API_KEY"),
                  consumer_secret=os.environ.get("TWITTER_API_SECRET_KEY"),
                  access_token_key=os.environ.get("TWITTER_ACCESS_TOKEN"),
                  access_token_secret=os.environ.get("TWITTER_ACCESS_TOKEN_SECRET"))


def post_to_twitter(message):
    api.PostUpdate(message)

def channel_post_handler(update, context):
    post_to_twitter(update.channel_post.text)

def main():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
    logging.info("Bot started")
    updater = Updater(token=os.environ.get("TELEGRAM_BOT_TOKEN", None), use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.update.channel_posts, channel_post_handler))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()