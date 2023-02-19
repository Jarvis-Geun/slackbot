from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import datetime
import sys


date = datetime.datetime.now()
tomorrow = datetime.date.today() + datetime.timedelta(days=1)

days = ["월", "화", "수", "목", "금", "토", "일"]
tomorrow_month = tomorrow.month
tomorrow_day = tomorrow.day
tomorrow_weekday = days[tomorrow.weekday()]

today_weekday = days[date.weekday()]
if today_weekday == "토" or today_weekday == "일":
    print("Exit: Today is weekend!")
    sys.exit()

if tomorrow_weekday == "토":
    tomorrow_weekday = "월"
    tomorrow_day += 2

elif tomorrow_weekday == "일":
    tomorrow_weekday = "월"
    tomorrow_day += 1

# ID of channel you want to post message to
channel_id = "<id of channel> ex. #channel"
message = "<type message>"

myToken = "<token of the app>"
client = WebClient(token=myToken)

try:
    # Call the chat.postMessage method using the WebClient
    # The client passes the token you included in initialization    
    result = client.chat_postMessage(
        channel=channel_id,
        text=message
        # You could also use a blocks[] array to send richer content
    )

    # timestamp for reply to the thread
    ts_path = "<path of timestamp>"
    with open(ts_path, "a") as f:
        f.write(result['ts'] + '\n')
        print(result['ts'])

except SlackApiError as e:
    print(f"Error: {e}")
