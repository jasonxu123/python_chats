from bs4 import BeautifulSoup
from random import randint
import re
import string

soup = BeautifulSoup(open("/Users/jasonxu123/Downloads/facebook-jasonxu7146557/html/messages.htm"), "html.parser")
arr = soup.find_all("p")
nametags = soup.find_all("span", "user")
timetags = soup.find_all("span", "meta")
aliases = {"Mr. Bean": "Person: 0"}

long_p = ""
for l in xrange(len(arr)-1, -1, -1):
    real = nametags[l].get_text(' ', strip=True)
    if real not in aliases:
        aliases[real] = "Person: " + str(len(aliases)+1)
    fake = aliases[real]
    timestamp = timetags[l].get_text(' ', strip=True)
    str3 = arr[l].get_text(' ', strip=True)
    long_p += fake + "\nTime: " + timestamp + "\n" + str3 + "\n"
    long_p += "--------------------------------------------- EOM ---------------------------------------------\n"

long_talk = re.sub('</?(p|span.*)>', '', long_p)
long_talk = re.sub('[^0-9][0-9]{9}[^0-9]', '\n'+str(randint(100000000, 999999999))+'\n', long_talk)
printable = set(string.printable)
long_talk = filter(lambda x: x in printable, long_talk)

f = open("/Users/jasonxu123/Documents/test.txt", "w")
f.write(long_talk)
f.close()
