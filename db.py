import pandas as pd
import time

def sendToSlack():
    pass


def write(email, name, group, contents):
    global pandas_frame
    now = time.localtime(time.time())
    createdAt = time.strftime('%c', time.localtime(time.time()))
    new_line = pd.DataFrame([email, name, group, contents, createdAt])
    sendToSlack([email, name, group, contents, createdAt])
    new_line.to_csv("submit.csv", mode= "a")


