import requests
import bs4
import threading
import queue
from pprint import pprint
import json


BASE_URL = 'https://ru.wikipedia.org'
FIRST = '/w/index.php?title=Категория:Животные_по_алфавиту&from=А'


class DataColection(threading.Thread):
    def __init__(self, out_queue, liter, link):
        threading.Thread.__init__(self)
        self.liter = liter
        self.link = link
        self.out_queue = out_queue
        print("Initialized thread DataColection " + str(self.liter))

    def run(self):
        try:
            res = requests.get(BASE_URL + self.link)
            soup = bs4.BeautifulSoup(res.text, 'lxml')
            print(self.liter)
            names_lst = soup.find('div', class_='mw-category-group').find_all('li')
            self.out_queue.put({self.liter: [i.find('a').get('title') for i in names_lst]})
            return True
        except:
            return False

def get_wiki_data():
    threads = []
    out_queue = queue.Queue()
    curent_liter = 'q'
    next_href = FIRST
    while curent_liter != 'Я':
        r = requests.get(BASE_URL + next_href)
        soup = bs4.BeautifulSoup(r.text, 'lxml')
        curent_liter = soup.find('div', class_='mw-category-group').find('h3').get_text()
        worker = DataColection(out_queue, liter=curent_liter, link=next_href)
        worker.setDaemon(True)
        worker.start()
        threads.append(worker)
        next_href = soup.find('div', {'id': 'mw-pages'}).find_all('a')[1].get('href')

    for th in threads:
        th.join()
    data_ = {}
    while not out_queue.empty():
        new_d = out_queue.get()
        curkey = list(new_d.keys())[0]
        if curkey in data_.keys():
            data_[curkey] += new_d[curkey]
        else:
            data_[curkey] = new_d[curkey]

    with open('data.json', 'w') as outfile:
        json.dump([{key, len(value)} for key, value in data_.items()], outfile)


if __name__ == '__main__':
    get_wiki_data()
