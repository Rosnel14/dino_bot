import time
import random
import schedule
import subprocess

import main
import utils
from bandwidth.bandwidth_client import BandwidthClient


def send_message():
    subprocess.call("osascript message.applescript '%s' '%s'" % (f'{utils.phone_number}',
                                                                 f'{random.choice(utils.message)}'), shell=True)


if __name__ == '__main__':

    # Call the init method
    main.init()
    schedule.every().day.at(utils.scheduled_time).do(send_message)

    while True:
        schedule.run_pending()
        print("Message Sent")
        time.sleep(1)


# This initializes the bandwidth SDK
def init():
    bandwidth_client = BandwidthClient(
        messaging_basic_auth_user_name="{username}",
        messaging_basic_auth_password="{password}",
        voice_basic_auth_user_name="{username}",
        voice_basic_auth_password="{password}"
    )
    voice_client = bandwidth_client.voice_client.client
    messaging_client = bandwidth_client.messaging_client.client
