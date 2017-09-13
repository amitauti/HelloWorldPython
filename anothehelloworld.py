import time
from datetime import datetime

def main():
    print ("Print Date")
    now = datetime.datetime.now()
    print (now.year, now.month, now.day, now.hour, now.minute, now.second)

if __name__ == '__main__':
    main()
