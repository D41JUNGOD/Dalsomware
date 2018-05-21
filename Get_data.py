import requests,re
from bs4 import BeautifulSoup

def get_key():
    URL = "http://ransom.dothome.co.kr/key"
    r = requests.get(URL)
    soup = BeautifulSoup(r.text,'html.parser')
    key = re.sub('<.+?>|&nbsp| |\t|\r|\n;', '', str(soup.find("body")) , 0, re.I|re.S)
    key = re.sub('&nbsp;| |\t|\r|\n', '', key)
    return key

def get_kill():
    URL = "http://ransom.dothome.co.kr/kill"
    r = requests.get(URL)
    soup = BeautifulSoup(r.text,'html.parser')
    kill_switch = re.sub('<.+?>', '', str(soup.find("body")) , 0, re.I|re.S)
    kill_switch = re.sub('&nbsp;| |\t|\r|\n', '', kill_switch)
    return kill_switch
