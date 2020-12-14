from bs4 import BeautifulSoup
import requests


headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/80.0.3987.132 YaBrowser/20.3.1.197 Yowser/2.5 Safari/537.36"
}


def write_to_file(name, value):
    file = "result/"+name+".txt"
    f = open(file, "w")
    f.write(value)
    f.close()


def spbu_get_main(link):

    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")
    a=soup.get_text()
    write_to_file("main_spbu", a)
    return a


def spbu_get_student(link):

    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")
    
    # боковая панель навигации с ссылками в тегах
    navigation = soup.findAll("div", {'class' : "g-hide-sm"})
    ans = ''
    for elem in navigation:
        ans += elem.get_text()
    
    # текст со страницы
    text = soup.findAll("div", {'class' : "editor editor--large"})
    for elem in text:
        ans += elem.get_text()
    write_to_file("student_spbu", ans)    
    return ans
    

def spbu_get_univer(link):

    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")
    ans = ''
    # боковая панель навигации с ссылками в тегах
    navigation = soup.findAll("div", {'class' : "g-hide-sm"})
    for elem in navigation:
    	ans += elem.get_text()
    
    # текст со страницы
    text = soup.findAll("div", {'class' : "editor editor--large"})
    for elem in text:
    	ans += elem.get_text()
    write_to_file("univer_spbu", ans)
    return ans


def web_get_only_text(link):
    req = requests.get(link, headers=headers)
    soup = BeautifulSoup(req.text, "lxml")
    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    print(text)


def msu_get_main(link):

    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")
    a=soup.get_text()
    write_to_file("main_nsu", a)
    return a


def msu_get_science(link):

    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")
    ans=""
    news_list = soup.findAll("div", {'class' : "news-list-item"})
    
    news_list = soup.findAll("li")
    for elem in news_list:
    	ans+=elem.get_text()
    ans+=soup.get_text()
    write_to_file("msu_science", ans)
    return ans


def msu_get_news(link):

    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")
    ans =''
    title = soup.findAll("div", {'class' : "news-list-item-head news-list-item-date-full"})
    for elem in title:
        ans += elem.get_text()
    # print(title.prettify())
    
    # текст со страницы
    text = soup.findAll("div", {'class' : "news-list-item-text"})
    for elem in text:
        ans += elem.get_text()
    write_to_file("msu_news", ans)
    return ans
