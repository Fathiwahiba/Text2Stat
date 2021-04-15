import requests
from bs4 import BeautifulSoup

links = []
nbr = []

url1 = 'http://www.ump.ma/fr/actualite'

response1 = requests.get(url1)

if response1.ok:
    soup1 = BeautifulSoup(response1.text, 'lxml')
    uls = soup1.findAll('ul', class_='pagination')
    for ul in uls:
        for li in ul.findAll('li'):
            nbr.append(li)
            index = len(nbr)-2
            notreLi = nbr[index]

    notreA = notreLi.find('a')
    nombre = notreA.text

    url2 = 'http://www.ump.ma/fr/actualite?page=1'
    response2 = requests.get(url2)

    if response2.ok:
        soup2 = BeautifulSoup(response2.text, 'lxml')
        divs = soup2.findAll('div', class_='caption')
        for div in divs: #on a 9
            a = div.find('a')
            link = a['href'] #pour chaque div des 9 on recupere le href dans a
            links.append(link) #on les met dans une liste 

        for l in links: #on parcoure la liste contenant les 9 liens
            url3 = l
            response3 = requests.get(url3)

            if response3.ok:
                soup3 = BeautifulSoup(response3.text, 'lxml')
                article = soup3.find('article')
                h1 = article.find('h1')
                
            output = open('result.txt', 'a', encoding='utf-8')
            output.write(h1.text)
            output.write("\n")
            output.close()
