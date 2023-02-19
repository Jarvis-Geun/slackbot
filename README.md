# slackbot

`-` Reference
- [Python으로 Slack Bot 만들기](https://wooiljeong.github.io/python/slack-bot/)
- [[Youtube] 슬랙 앱 추가하여 사용해보기](https://www.youtube.com/watch?v=6FHoF39zQ-0&ab_channel=%EB%8F%99%EB%B9%88%EB%82%98)
- [Slack | Bolt for Python](https://slack.dev/bolt-python/concepts)

## Requirements
- Python 3.6 이상
- [슬랙봇 앱 만들고 토큰 발행하기](https://wooiljeong.github.io/python/slack-bot/)
- `$ pip install slackclient`


## client.chat_postMessage
- [[Slack api] chat.postMessage](https://api.slack.com/methods/chat.postMessage)

```python
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


# ID of the channel you want to send the message to
channel_id = "<ID of the channel>"
message = "Hello World!"
myToken = "<token of the slack app>"
client = WebClient(token=myToken)

try:
    # Call the chat.postMessage method using the WebClient
    result = client.chat_postMessage(
        channel=channel_id, 
        text=message
    )
    logger.info(result)

except SlackApiError as e:
    logger.error(f"Error posting message: {e}")
```

## crontab
`-` Reference
- [리눅스 크론탭(Linux Crontab) 사용법](https://jdm.kr/blog/2)
- [EasyCron](https://www.easycron.com/faq/What-cron-expression-does-easycron-support)

```shell
crontab -e
```
```shell
# minute(0-59) | hour(0-23) | day(1-31) | month(1-12) | weekday(0-6)
# every weekdays at 08:00 AM
0 8 * * 1-5 <path of python> <path of python file>
```