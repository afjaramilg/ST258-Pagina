from bs4 import BeautifulSoup
import requests
import db
from datetime import date
#puedo poner el link de tal forma que busco lo que quiero desde aqui
# simplemente poner https://listado.mercadolibre.com.co/{tag1}-{tag2}-{tag3}#D[A:tag1%20{tag2}%20{tag3}]  


def products(item,link):
    global records
    title = item.find('h1', attrs={'class':'ui-pdp-title'}).contents[0] #titulo del producto
    seller = item.find('span', attrs={'class':'ui-pdp-color--BLUE'}).contents[0] #vendedor del producto
    price = item.find('span', attrs={'class':'price-tag-fraction'}).contents[0]#precio
    q_a = item.find_all('div', attrs={'ui-pdp-questions__questions-list__item-questions--others-questions'})
    q_a_list=[]#lista de preguntas y respuestas
    for qa in q_a:
        question = qa.find('span', attrs={'class':'ui-pdp-color--BLACK ui-pdp-size--SMALL ui-pdp-family--REGULAR ui-pdp-questions__questions-list__question'})
        answer = qa.find('span', attrs={'class':'ui-pdp-color--GRAY ui-pdp-size--SMALL ui-pdp-family--REGULAR ui-pdp-questions__questions-list__answer-item__separate'})
        if question is not None:
            q = question.contents[0]
        else:
            q = None
        
        if answer is not None:
            a = answer.contents[0]
        else:
            a = None
        q_a_list.append({'question':q,'answer':a})
    product={'title':title,
             'link':link,
             'seller':seller,
             'price':price,
             'q&a':q_a_list,
             'date': str(date.today())}

    db.post_record(product)
    print("Product saved succesfully")
#-#sAEThgbr#tjs8
def main(url):
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',}
    webpage = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "lxml")
    matches = ['xbox', 'series x']
    matches_all = ['xbox', 'series x']
    matches_any = ['series x', 'series s']
    try:
        links = soup.find_all('div',attrs={'class':'andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default'})
        for item in links:

            title = item.find('a')['title'].lower()
            link = item.find('a')['href']
            #lo proximo es meter filtros obligatorios y filtros opcionales
            #si una vez pasan estos filtros lo que hago es guardar los links
            if all(tag in title for tag in matches):
                product = requests.get(link, HEADERS)
                product_soup = BeautifulSoup(product.content,'lxml')
                products(product_soup,link)
            else:
                pass
    except AttributeError:
        print('o shit, something went wrong')

if __name__ == '__main__':
    File = open("out.csv", "a")
    URLS = open("url.txt", "r")
    for link in URLS.readlines():
        main(link)