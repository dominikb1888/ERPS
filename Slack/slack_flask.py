from slack_bolt import App

import logging
import os

logging.basicConfig(level=logging.DEBUG)


SLACK_SIGNING_SECRET = "8f6df989e592f201b58f2431232defd5"
SLACK_BOT_TOKEN = "xoxb-1737245288757-1844648244052-zB4AGowqIqzhchY7L50jHwIk"

app = App(
    token=SLACK_BOT_TOKEN,
    signing_secret=SLACK_SIGNING_SECRET
)


@app.middleware  # or app.use(log_request)
def log_request(logger, body, next):
    logger.debug(body)
    return next()


@app.command("/hello-bolt-python")
def hello_command(ack, body):
    user_id = body["user_id"]
    ack(f"Hi <@{user_id}>!")


@app.event("app_mention")
def event_test(body, say, logger):
    logger.info(body)
    say("What's up?")


@app.event("app_home_opened")
def update_home_tab(client, event, logger):
  try:
    # views.publish is the method that your app uses to push a view to the Home tab
    client.views_publish(
        # the user that opened your app's app home
        user_id=event["user"],
        # the view object that appears in the app home
        view={
            "type": "home",
            "callback_id": "home_view",

            # body of the view
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "*Welcome to your _App's Home_* :tada:"
                    }
                },
                {
                    "type": "divider"
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "This button won't do much for now but you can set up a listener for it using the `actions()` method and passing its unique `action_id`. See an example in the `examples` folder within your Bolt app."
                    }
                },
                {
                    "type": "actions",
                    "elements": [
                        {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "Click me!"
                            }
                        }
                    ]
                }
            ]
        }
    )

  except Exception as e:
    logger.error(f"Error publishing home tab: {e}")


@app.error
def global_error_handler(error, body, logger):
    logger.exception(error)
    logger.info(body)


# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 80)))
