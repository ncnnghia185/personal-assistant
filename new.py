# importing requests package
import requests
from output_module import output
from internet_connect import check_internet_connection


def get_new():
    # BBC news api
    # following query parameters are used
    # source, sortBy and apiKey
    if check_internet_connection():
        query_params = {
            "source": "bbc-news",
            "sortBy": "top",
            "apiKey": "5468d3f2bab749d9af30bd08f7325c5d"
        }
        main_url = " https://newsapi.org/v1/articles"

        # fetching data in json format
        res = requests.get(main_url, params=query_params)
        open_bbc_page = res.json()

        # getting all articles in a string article
        article = open_bbc_page["articles"]

        # empty list which will
        # contain all trending news
        results = []

        for ar in article:
            results.append(ar["title"])

        for i in range(len(results)):
            # printing all trending news
            output(str(i + 1) + " " + results[i])
    else:
        return "Check your connection"

# Driver Code
