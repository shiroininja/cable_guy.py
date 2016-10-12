""" This is the Module for Morty's 3rd full time job. He only works at this job 3 times a week. This script 
    searches for my favourite youtube channel, gets the list of videos uploaded, and only downloads the newest
    submission.
"""


# Importing the things needed for the job

from __future__ import unicode_literals
import youtube_dl
import time
import os
from datetime import date
import calendar
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GREEN_LED = 22
RED_LED = 19
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)
# Setting up work schedule

my_date = date.today()
day_week = calendar.day_name[my_date.weekday()]
work_days = ['Saturday']
work_today = any(string in day_week for string in work_days)
hajime_day = ['Wednesday']
work_tomorrow  = any(string in day_week for string in hajime_day)
linux_day = ['Friday']
sabbath = any(string in day_week for string in linux_day)
unrested_day = ['Tuesday']
unrested = any(string in day_week for string in unrested_day)

def larry():

    if work_today:

        GPIO.output(GREEN_LED, True)
        GPIO.output(RED_LED, False)
        print("------------------------------------------------------")
        print("Is it that time already? Going to get your favourite shows, boss!")
        print("------------------------------------------------------")
        YDLOptions={
            # Provide any options to YDL you want here, see
            # https://github.com/rg3/youtube-dl/blob/master/youtube_dl/YoutubeDL.py#L117-L265 
            #for options
            'playlist_items':'1,2,3,4,5,6,7' # here you put how far back you want to go in the video list
}

        with youtube_dl.YoutubeDL(YDLOptions) as ydl:
            ydl.download(['put your channels video list url here'])


    if work_tomorrow:

        GPIO.output(GREEN_LED, True)
        GPIO.output(RED_LED, False)
        print("------------------------------------------------------")
        print("Is it that time already? Going to get your favourite shows, boss!")
        print("------------------------------------------------------")
        YDLOptions={
            # Provide any options to YDL you want here, see
            # https://github.com/rg3/youtube-dl/blob/master/youtube_dl/YoutubeDL.py#L117-L265 
            #for options
            'playlist_items':'1,2,3,4,5'

}

        with youtube_dl.YoutubeDL(YDLOptions) as ydl:
            ydl.download(['put your channels video list url here'])

    if sabbath:

        GPIO.output(GREEN_LED, True)
        GPIO.output(RED_LED, False)
        print("------------------------------------------------------")
        print("Is it that time already? Going to get your favourite shows, boss!")
        print("------------------------------------------------------")
        YDLOptions={
            # Provide any options to YDL you want here, see
            # https://github.com/rg3/youtube-dl/blob/master/youtube_dl/YoutubeDL.py#L117-L265 
            #for options
            'playlist_items':'1,2,3,4,5,6,7,8,9,10,11,12,13'

}

        with youtube_dl.YoutubeDL(YDLOptions) as ydl:
            ydl.download(['put your channels videos list url here'])


    if unrested:

        GPIO.output(GREEN_LED, True)
        GPIO.output(RED_LED, False)
        print("------------------------------------------------------")
        print("Is it that time already? Going to get your favourite shows, boss!")
        print("------------------------------------------------------")
        YDLOptions={
            # Provide any options to YDL you want here, see
            # https://github.com/rg3/youtube-dl/blob/master/youtube_dl/YoutubeDL.py#L117-L265 
            #for options
            'playlist_items':'1,2,3,4,5,6,7'

}

        with youtube_dl.YoutubeDL(YDLOptions) as ydl:
            ydl.download(['https://www.youtube.com/user/unrested/videos'])



    else:
        print("\nNot working as a cable guy today!\n")
        GPIO.output(GREEN_LED, False)
        GPIO.output(RED_LED, True)


        






