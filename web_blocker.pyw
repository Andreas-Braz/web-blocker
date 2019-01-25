import time
from datetime import datetime as dt

hosts_test = r"hosts_test"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
sites_list = ["https://www.facebook.com", "facebook.com"] #add sites you wish to block


while True:

    if dt(dt.now().year,dt.now().month,dt.now().day,8) \
            < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,19): #change the hours as it is convenient for you.
        #print("working hours")

        with open(hosts_test, "r+") as file:
            content = file.read()
            for site in sites_list:
                if site in content:
                    pass
                else:
                    file.write(redirect + " " + site + "\n")

    else:
        with open(hosts_test, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(site in line for site in sites_list):
                    file.write(line)
            file.truncate()
        #print("Feierabend")

    time.sleep(5)