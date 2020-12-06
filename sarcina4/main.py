from selenium import webdriver
from conf import *
from time import sleep
import re
browser = webdriver.Chrome("D:\Projects\Pythn_Projects\sarcina4\chromedriver.exe")

keys = [('LXV', 'POR'), ('XCII', 'UWR')]
browser.get("https://www.instagram.com/accounts/login/")
browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]').click()
sleep(1)
browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(login)
browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()
sleep(4)
browser.find_element_by_xpath('//html/body/div[4]/div/div/div/div[3]/button[1]').click()

links = set()
dict = set()

browser.get("https://www.instagram.com/best_chisinau/?hl=ru")
SCROLL_PAUSE_TIME = 4

# Get scroll height
last_height = browser.execute_script("return document.body.scrollHeight")
i = 0
while True:
    print(f"i={i}/35")
    i += 1
    if i >=35:
        break
    page_source = browser.page_source
    regular = r"([A-Z]+): ([A-Z]+)"
    c = re.findall(regular, page_source)
    for j in c:
        if j[0] not in dict:
            dict.add(j[0])
            keys.append(j)

    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = browser.execute_script("return document.body.scrollHeight")
    last_height = new_height

# print(keys)
# print(len(dict))


def value(r):
        if (r == 'I'):
                return 1
        if (r == 'V'):
                return 5
        if (r == 'X'):
                return 10
        if (r == 'L'):
                return 50
        if (r == 'C'):
                return 100
        if (r == 'D'):
                return 500
        if (r == 'M'):
                return 1000
        return -1


def romanToDecimal(str):
        res = 0
        i = 0

        while (i < len(str)):

                # Getting value of symbol s[i]
                s1 = value(str[i])

                if (i + 1 < len(str)):

                        # Getting value of symbol s[i + 1]
                        s2 = value(str[i + 1])

                        # Comparing both values
                        if (s1 >= s2):

                                # Value of current symbol is greater
                                # or equal to the next symbol
                                res = res + s1
                                i = i + 1
                        else:

                                # Value of current symbol is greater
                                # or equal to the next symbol
                                res = res + s2 - s1
                                i = i + 2
                else:
                        res = res + s1
                        i = i + 1

        return res

new = []
for i in keys:
    new.append((romanToDecimal(i[0]), i[1]))

print(keys)
new.sort(key=lambda x: x[0])
print(new)
j = 0
for i in new:
        if j+1 != i[0]:
                print(i[0]-1)
                j+=1
        j += 1
print('')
for i in new:
        print(i[1],end='')
print('\n')