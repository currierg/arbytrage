from time import sleep, localtime
import os
from datetime import datetime
import requests

import stats

if __name__=="__main__":
    print "Starting to collect stats..."
    while True:
        t = localtime()
        time = ":".join([str(t) for t in [t.tm_hour,t.tm_min,t.tm_sec]])
        print "Collecting stats at "+time


        now = str(datetime.utcnow())
        date = now[:11]
        time = "-".join(now[-15:-7].split(":"))

        filename = "stats/records/"+date+"/"+time+".json"
        dirname = os.path.dirname(filename)

        if not os.path.exists(dirname):
            os.makedirs(dirname)

        # collect and record stats, silently failing if we don't have an internet connection
        try:
            stats.record(*stats.collect(), filename=filename)
        except requests.exceptions.ConnectionError:
            pass

        # sleep for 30 mins
        sleep(1800)