import slackweb
import os
import serial
import time

url = os.environ["SLACK_OHA"]
slack = slackweb.Slack(url=url)

port = "/dev/cu.usbmodem1421"
current_oha_state = False

# ボード側は500ms間隔でserialにHIGH -> b"1", LOW -> b"0"を送信する
with serial.Serial(port=port, baudrate=9600, timeout=1) as ser:
    while True:
        # time.sleep(0.1)
        flag = ser.readline()
        # switch ON
        if (bytes(b"0") in flag and not current_oha_state):
            current_oha_state = True
            print("oha")
            slack.notify(text="スシ食べたい🍣")

        # switch OFF
        elif (bytes(b"1") in flag and current_oha_state):
            current_oha_state = False
            print("otu")
            slack.notify(text="スシいらない🍣")

        print(flag, current_oha_state)
