import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titleline')
subtexts = soup.select('.subtext')

res2 = requests.get('https://news.ycombinator.com/?p=2')
soup2 = BeautifulSoup(res2.text, 'html.parser')
links2 = soup2.select('.titleline')
subtexts2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtexts = subtexts + subtexts2



def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subtexts):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.a.get('href', None)
        vote = subtexts[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))            
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)

pprint.pp(create_custom_hn(mega_links, mega_subtexts))


    
