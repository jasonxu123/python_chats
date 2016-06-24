from bs4 import BeautifulSoup       # download BeautifulSoup first: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
from random import randint
import re
import string
                                    # REMEMBER TO CHANGE THIS LINE TO RIGHT DIRECTORY
soup = BeautifulSoup(open("/path-to/<facebook's_unzipped_folder>/html/messages.htm"), "html.parser")
arr = soup.find_all("p")
nametags = soup.find_all("span", "user")
timetags = soup.find_all("span", "meta")                    # get all useful data (returns list with tags still included)
aliases = {"Mr. Bean": "Person: 0"}

long_p = ""
for l in xrange(len(arr)-1, -1, -1):                        # backwards since chats printed in reverse order
    real = nametags[l].get_text(' ', strip=True)
    if real not in aliases:
        aliases[real] = "Person: " + str(len(aliases))      # put all useful data into 1 large string
    fake = real                     # UNCOMMENT LINE BELOW FOR NAME HIDING
    # fake = aliases[real]
    timestamp = timetags[l].get_text(' ', strip=True)
    str3 = arr[l].get_text(' ', strip=True)                 # format: Person, Time, Message, EOM → 1 per line
    long_p += fake + "\nTime: " + timestamp + "\n" + str3 + "\n"
    long_p += "--------------------------------------------- EOM ---------------------------------------------\n"

long_talk = re.sub('</?(p|span.*)>', '', long_p)            # remove all tags, turn IDs into random 9 digit number
long_talk = re.sub('[^0-9][0-9]{9}[^0-9]', '\n'+str(randint(100000000, 999999999))+'\n', long_talk)
printable = set(string.printable)                           # remove non-ASCII characters
long_talk = filter(lambda x: x in printable, long_talk)

f = open("/path-to/preferred/directory/test.txt", "w")      # create text document of all chats: test.txt
f.write(long_talk)
f.close()
