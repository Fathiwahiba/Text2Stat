import requests
from bs4 import BeautifulSoup


# trouver le nombre de pages contenant les articles
def nbr_pages():
    global notre_li
    nbr = []
    url1 = 'http://www.ump.ma/fr/actualite'
    response1 = requests.get(url1)
    if response1.ok:
        soup1 = BeautifulSoup(response1.text, 'lxml')
        uls = soup1.findAll('ul', class_='pagination')
        for ul in uls:
            for li in ul.findAll('li'):
                nbr.append(li)
                index = len(nbr) - 2
                notre_li = nbr[index]
        notre_a = notre_li.find('a')
        nombre = notre_a.text  # nombre de pages existantes qu'on va parcourir
        n = int(nombre)
        return n




# trouver les liens des articles contenus dans une page
def liens(number):
    global les_liens
    url2 = 'http://www.ump.ma/fr/actualite?page=' + number
    response2 = requests.get(url2)

    if response2.ok:
        soup2 = BeautifulSoup(response2.text, 'lxml')
        divs = soup2.findAll('div', class_='caption')
        les_liens = []
        for div in divs:  # on a 9 div dans une page, chaque div représente un article
            a = div.find('a')
            un_lien = a['href']  # pour chaque div des 9 on recupere le href qui est dans a
            les_liens.append(un_lien)  # on les met dans une liste
    return les_liens




# trouver les titres contenus dans un lien
def titres(lien):
    url3 = lien
    response3 = requests.get(url3)
    les_h = []
    if response3.ok:
        soup3 = BeautifulSoup(response3.text, 'lxml')
        article = soup3.find('article')  # le contenu est dans la balise article
        h1 = article.find('h1')  # on extrait les titres de chaque article
        les_h.append(h1.text)
    return les_h




# globalement,
nombre_pages = nbr_pages()
inbr = 1
while inbr <= nombre_pages:
    istr = str(inbr)
    links = liens(istr)
    for link in links:
        titles = titres(link)
        output = open('p1.txt', 'a', encoding='utf-8')
        for h in titles:
            output.write(h)
            output.write("\n")
        output.close()
    inbr = inbr + 1
