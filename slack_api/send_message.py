from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


def send_message(client, channel_id, message, ts_path=None):
    if ts_path != None:
        # Load timestamp for reply
        with open(ts_path, "r") as f:
            message_ts = f.readlines()[-1]
            print(message_ts)
    
    try:
        # Call the chat.postMessage method using the WebClient
        # The client passes the token you included in initialization    
        result = client.chat_postMessage(
            channel=channel_id,
            text=message,
            # thread_ts=message_ts
            # You could also use a blocks[] array to send richer content
        )
        # print(result['ts'])
        # ts_path = "<path of the timestamp>"
        # with open(ts_path, "a") as f:
        #     f.write(result['ts'] + '\n')

    except SlackApiError as e:
        print(f"Error: {e}")


if __name__=="__main__":
    myToken = "<token of the app>"
    channel_id = "<id of the channel> ex. #channel"
    message = "<type message>"
    # ts_path = "<path of timestamp>"

    client = WebClient(myToken)

    send_message(client=client, channel_id=channel_id, message=message, ts_path=None)