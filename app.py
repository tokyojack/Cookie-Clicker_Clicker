import threading
import time
import _thread

import schedule
from mouse import is_pressed, click
from selenium import webdriver

from AverageCPS import AverageCPS

average_cps = AverageCPS()

def handle_cps_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

def handle_click():
    while True:
        if is_pressed(button='left'):
            click(button='left')
            continue

        try:
            driver.find_element_by_id("bigCookie").click()
            average_cps.add_click()
        except:
            continue


if __name__ == '__main__':
    print("starting")

    driver = webdriver.Chrome('./drivers/chromedriver.exe')

    driver.set_page_load_timeout(10)
    driver.get("http://orteil.dashnet.org/cookieclicker/")

    thread1 = threading.Thread(target=handle_cps_scheduler)
    thread1.start()

    thread2 = threading.Thread(target=handle_click)
    thread2.start()
