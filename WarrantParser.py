
import requests
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from Warrant import Warrant

def get_url(url):
    return requests.get(url)

def main():

    try:

        underlying = 'CAC 40'
        rootUrl = "https://www.boursorama.com"
        mainBaseUrl = f"{rootUrl}/bourse/produits-de-bourse/levier/warrants/resultats?warrant_filter%5BunderlyingType%5D=&warrant_filter%5BunderlyingName%5D%5B%5D={underlying}&warrant_filter%5Bdelta%5D%5B%5D=0&warrant_filter%5Bdelta%5D%5B%5D=100&warrant_filter%5Bsearch%5D="

        response = get_url(mainBaseUrl)
        soup = BeautifulSoup(response.text, 'lxml')

        links = soup.find_all('span', class_='c-pagination__content')
        link = links[-1]
        maxPageIndex = int(link.text)
        listPageURLs = []
        for i in range(maxPageIndex):
            listPageURLs.append(f"{mainBaseUrl}&page={i+1}")

        with ThreadPoolExecutor() as pool:
            responses = list(pool.map(get_url, listPageURLs))

        warrantList = []
        instrumentURLList = []

        for response in responses:

            soup = BeautifulSoup(response.text, 'lxml')

            quotes = soup.find_all('tr', class_='c-table__row')
            quoteList = [quote.text.replace('\n', '') for quote in quotes]
 
            for warrantIndex in range(1, len(quoteList)-1):
                try:
                    warrantList.append(Warrant(quoteList[warrantIndex]))
                except Exception as e:
                    print('Instrument instanciation exception', e)

            instrumentDetails = soup.find_all('a', class_='c-link c-link--animated / o-ellipsis', href=True)

            for instrument in instrumentDetails:
                instrumentURLList.append(f"{rootUrl}{instrument['href']}")
 
        for warrant in warrantList:
            print(warrant)
        print(len(warrantList))           

        with ThreadPoolExecutor() as pool:
            responses = list(pool.map(get_url, instrumentURLList))

        for response in responses:

            try:

                warrantISIN = response.url.split('/')[-1][3:]

                soup = BeautifulSoup(response.text, 'lxml')
                quotes = soup.find_all('li', class_='c-list-info__item')
                quoteList = [quote.text for quote in quotes]

                spot, quotity = None, None
                for quote in quoteList:
                    items = quote.replace('\n', '').split()
                    if items[0] == 'Spot': spot = float(items[1])
                    if items[0] == 'Parité': quotity = int(items[1])

                for warrant in warrantList:
                    if(warrant.ISIN == warrantISIN): 
                        warrant.UnderlyingSpot = spot
                        warrant.Quotity = quotity

            except:

                pass

        for warrant in warrantList:
            print(warrant)
        print(len(warrantList))           

    except Exception as e:
        
        print('Global exception', e)

if __name__ == "__main__" : main()