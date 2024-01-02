import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "**Please Drink Water Now!!**",
            message ="Your Daily limit to drink water is 5.4 Liters. So please intake 350 ml now.",
            app_icon = "E:\MY SPACE\PROJECTS\Desktop Notification for drinking water\icon.ico",
            timeout = 25
        )
        time.sleep(60*60)