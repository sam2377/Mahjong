import random
import math
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

#################################################################
tile_dict = {
    "0p": 0,
    "1p": 1, 
    "2p": 2,
    "3p": 3,
    "4p": 4, 
    "5p": 5,
    "6p": 6,
    "7p": 7, 
    "8p": 8,
    "9p": 9,
    "0m": 10,
    "1m": 11, 
    "2m": 12,
    "3m": 13,
    "4m": 14, 
    "5m": 15,
    "6m": 16,
    "7m": 17, 
    "8m": 18,
    "9m": 19,
    "0s": 20,
    "1s": 21, 
    "2s": 22,
    "3s": 23,
    "4s": 24, 
    "5s": 25,
    "6s": 26,
    "7s": 27, 
    "8s": 28,
    "9s": 29,
    "1z": 30,
    "2z": 31,
    "3z": 32,
    "4z": 33,
    "5z": 34,
    "6z": 35,
    "7z": 36,
#################
    0: "0p",
    1: "1p",
    2: "2p",
    3: "3p",
    4: "4p", 
    5: "5p",
    6: "6p",
    7: "7p", 
    8: "8p",
    9: "9p",
    10: "0m",
    11: "1m", 
    12: "2m",
    13: "3m",
    14: "4m", 
    15: "5m",
    16: "6m",
    17: "7m", 
    18: "8m",
    19: "9m",
    20: "0s",
    21: "1s", 
    22: "2s",
    23: "3s",
    24: "4s", 
    25: "5s",
    26: "6s",
    27: "7s", 
    28: "8s",
    29: "9s",
    30: "1z",
    31: "2z",
    32: "3z",
    33: "4z",
    34: "5z",
    35: "6z",
    36: "7z"   
}

def query(inhand_list) :

    inhand = ""
    for i in range(len(inhand_list)) :
        inhand = inhand + inhand_list[i]

    url = "http://tenhou.net/2/?q=" + inhand

    options = Options()
    options.add_argument("--headless")       # define headless
    driver = webdriver.Chrome(chrome_options=options)     # open Chrome Explorer

    driver.get(url)

    html = driver.page_source       # get html

    soup = BeautifulSoup(html, 'html.parser')
    result = soup.find("textarea")
    result_str = str(result)
    parse_str = result_str.split(inhand)[1].split("</textarea>")[0].strip()
    
    print("inhand: " + inhand)
    print(parse_str)
    #print(type(parse_str))

    driver.close()

def numto34(num) :
    if num >= 0 and num <= 35 : 
        if num == 19 :
            return 0
        else :
            return math.floor(num/4) + 1
    elif num >= 36 and num <= 71 :
        if num == 55 :
            return 10
        else :
            return math.floor((num-36)/4) + 11
    elif num >= 72 and num <= 107 :
        if num == 91 :
            return 20
        else :
            return math.floor((num-72)/4) + 21
    elif num >= 108 and num <= 135 :
        return math.floor((num-108)/4) + 30

if __name__ == "__main__":
    inhand_num = []
    inhand_num34 = []
    inhand_str = []
    for i in range(14):
        while True :
            x = random.randint(0, 135)
            if x not in inhand_num:
                inhand_num.append(x)
                break
    inhand_num.sort()
    #print(inhand_num)

    for i in range(len(inhand_num)) :
        inhand_num34.append(numto34(inhand_num[i]))
        inhand_str.append(tile_dict[inhand_num34[i]])
    print(inhand_num34)
    print(inhand_str)
    query(inhand_str)
        
    


