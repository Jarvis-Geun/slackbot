from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


def send_message(client, channel_id, message, ts_path):
    try:
        # Call the chat.postMessage method using the WebClient
        # The client passes the token you included in initialization    
        result = client.chat_postMessage(
            channel=channel_id,
            text=message,
            # You could also use a blocks[] array to send richer content
        )
        ts_path = "<path of the timestamp>"
        with open(ts_path, "a") as f:
            f.write(result['ts'] + '\n')
            print(result['ts'])

    except SlackApiError as e:
        print(f"Error: {e}")


if __name__=="__main__":
    myToken = "<token of the app>"
    channel_id = "<id of the channel> ex. #channel"
    message = "<type message>"
    ts_path = "<path of timestamp>"

    client = WebClient(myToken)

    send_message(client=client, channel_id=channel_id, message=message, ts_path=ts_path)