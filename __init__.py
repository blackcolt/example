import requests
import time

if __name__ == '__main__':
    r = requests.get('https://ynet.co.il')
    for i in range(1000):
        time.sleep(2)
        print(r.status_code)
        print(r.text)
