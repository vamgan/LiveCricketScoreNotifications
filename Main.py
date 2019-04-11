import sys
from time import sleep
import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

toaster = ToastNotifier()
print('Live Cricket Notification Updates - VamGan:')
print('=====================')
url = "http://static.cricinfo.com/rss/livescores.xml"
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")

i = 1
for item in soup.findAll('item'):
    print(str(i) + '. ' + item.find('description').text)
    i = i + 1

links = []
for link in soup.findAll('item'):
    links.append(link.find('guid').text)

print('Enter match number or enter 0 to exit:')
while True:
    try:
        Input = int(input())
    except NameError:
        print('Invalid input. Try Again!')
        continue
    except SyntaxError:
        print('Invalid input. Try Again!')
    if Input < 0 or Input > 100:
        print('Invalid input. Try Again!')
        continue
    elif Input == 0:
        sys.exit()
    else:
        break

url = links[Input - 1]
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')

print("In what intervals you need score notifications?")
timeInterval = int(input())
print("You can minimize your window now!")
while True:
    matchUrl = links[Input - 1]
    r = requests.get(matchUrl)
    soup = BeautifulSoup(r.text, 'lxml')
    score = soup.findAll('title')
    s1 = (score[0].text + '\n')
    toaster.show_toast(s1[0:200], " ",
                       icon_path="ipl.ico",
                       duration=10)
    sleep(timeInterval)
