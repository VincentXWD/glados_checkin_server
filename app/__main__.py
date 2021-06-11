import sys
import time
import schedule
from .glados_checkin import main

cookie = sys.argv[1]


def job():
    main(cookie)


schedule.every().day.at("04:00").do(job)
schedule.every().day.at("10:00").do(job)
schedule.every().day.at("16:00").do(job)
schedule.every().day.at("22:00").do(job)


if __name__ == '__main__':
    job()
    s_t = 60 * 60 * 6
    while True:
        schedule.run_pending()
        time.sleep(1)
