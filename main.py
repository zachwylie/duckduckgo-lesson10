import requests
from bs4 import BeautifulSoup

url_ddg = "https://api.duckduckgo.com"


def ddg_search(query):
    resp = requests.get(url_ddg + f"/?q={query}&format=json")
    rsp_data = resp.json()
    relatedTopics = rsp_data['RelatedTopics']

    list_of_presidents = []

    for topic in relatedTopics:
        html_result = topic['Result']
        soup = BeautifulSoup(html_result, 'html.parser')
        president_name = soup.find('a').text
        lastname = president_name.split(" ")[-1]
        list_of_presidents.append(lastname)


    return list_of_presidents


if __name__ == "__main__":
    print(ddg_search("presidents of the united states"))
