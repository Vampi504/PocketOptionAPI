import random
import time
import dotenv
from pocketoptionapi.stable_api import PocketOption
import logging
import os
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(message)s')

dotenv.DotEnv()

ssid = (r'42["auth",{"session":"a:4:{s:10:\"session_id\";s:32:\"4ca29bc3a2daedfedc32856332fd0f74\";s:10:\"ip_address\";s:13:\"73.211.209.74\";s:10:\"user_agent\";s:111:\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36\";s:13:\"last_activity\";i:1722812253;}ff97db458281e7f5d6f6b26ac6085152","isDemo":0,"uid":79768402,"platform":2}]') #os.getenv("SSID")
print(ssid)
api = PocketOption(ssid)

if __name__ == "__main__":
    api.connect()
    time.sleep(5)

    print(api.check_connect(), "check connect")

    print(api.get_balance())
