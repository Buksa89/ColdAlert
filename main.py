#!/usr/bin/env python3
from datetime import datetime
import os
import sys
import telegram_send
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import alerts


if __name__ == '__main__':
    cold_alert = alerts.ColdAlert()
    if cold_alert.alert():
        telegram_send.send(messages=[cold_alert.alert()])

    with open(os.path.join(sys.path[0],'log'),'a') as file_object:
        file_object.write(f'{datetime.now().strftime("%y-%m-%d %H:%M:%S")}: {cold_alert.log}\n')
