import requests
import time
import datetime

timeopen = datetime.datetime.now()

def view():
    print (timeopen.strftime("%I:%M:%S │ Starting..."))
    print ("""╔═╗┌┐ ┌─┐┬ ┬  ╦  ╦┬┌─┐┬ ┬╔╗ ┌─┐┌┬┐
║╣ ├┴┐├─┤└┬┘  ╚╗╔╝│├┤ │││╠╩╗│ │ │ 
╚═╝└─┘┴ ┴ ┴    ╚╝ ┴└─┘└┴┘╚═╝└─┘ ┴ """)
    print ("━━━━━━━━━━━━━━━━━━━━━━")
    print("Made by @washedgram - Improved by @tobycodessometimes")
    print ("━━━━━━━━━━━━━━━━━━━━━━\n")
    timelink = datetime.datetime.now()
    listingURL = input((timelink.strftime("%I:%M:%S │ ")) + "Link -  ")

    timeviews = datetime.datetime.now()
    viewCount = int(input((timeviews.strftime("%I:%M:%S │ ")) + "Views Count -  "))

    timewatching = datetime.datetime.now()
    print ((timewatching.strftime("%I:%M:%S │ ")) + "Watching ...")
    timeclose = datetime.datetime.now()
    print ((timeclose.strftime("%I:%M:%S │ ")) + "Do not close this window.")

    start_time = time.time()
    for i in range(viewCount):
        r = requests.get(listingURL)
    
    timetaskc = datetime.datetime.now()
    print ((timetaskc.strftime("%I:%M:%S │ ")) + "Task completed! ")
    viewTime = float(time.time() - start_time)
    timetotaltime = datetime.datetime.now()
    print((timetotaltime.strftime("%I:%M:%S │ ")) + "Total time : " + " %s Seconds" % viewTime)
    viewRate = float(viewCount / viewTime)
    timeviewrate = datetime.datetime.now()
    print ((timeviewrate.strftime("%I:%M:%S │ ")) + "View rate  : " +  " %s Views / Second" % viewRate)


if __name__ == '__main__':
  view()

