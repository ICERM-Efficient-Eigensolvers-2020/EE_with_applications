import sys, os
import Page_Rank_Utils as pru
from Power_Iteration import PowerMethod
sys.path.append('/Users/yuqingliu/PycharmProjects/icerm_efficient_eigensolver/webCrawler/')
import web_scraper
import networkx as nx
import csv

def Stochastic_matrix_test():
    diG = nx.DiGraph()
    #3 is a dangling node
    diG.add_edge(1,2)
    diG.add_edge(1,3)
    diG.add_edge(1,4)
    diG.add_edge(2,3)
    diG.add_edge(4,3)

    M = pru.stochastic_transition_matrix_from_G(diG, False, 0.15)
    print(M)



def web_scrawler_application(url, max_urls,  func, weight=0.15):

    A, diG, internal_url_dict = web_scraper.scraper(url, max_urls)
    M = pru.stochastic_transition_matrix_from_G(diG, False, weight)
    eigenvec, eigenval = func(M)
    page_rank_dict = {}
    for i, page in enumerate(internal_url_dict):
        page_rank_dict[page] = eigenvec[i]
        print(page)
        print(eigenvec[i])

    page_rank_dict = {k: v for k, v in sorted(page_rank_dict.items(), key=lambda item: item[1], reverse=True)}
    print(page_rank_dict)
    url=url.replace('/','')
    fields = ['Link', 'Page Rank Score']
    with open(f"{url}_page_rank.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
        for k,v in page_rank_dict.items():
            writer.writerow([k,v])
        print(f"dominant eigenvector: {eigenvec}", file=f)
        print(f"dominant eigenvalue: {eigenval}", file=f)


if __name__ == '__main__':

    print("###ICERM domain test###")
    """
    import argparse

    parser = argparse.ArgumentParser(description="Link Extractor Tool with Python")
    parser.add_argument("url", help="The URL to extract links from.")
    parser.add_argument("-m", "--max-urls", help="Number of max URLs to crawl, default is 30.", default=30, type=int)
    parser.add_argument("func", help="The eigensolver to be tested.")

    args = parser.parse_args()
    url = args.url
    max_urls = args.max_urls
    func = args.func
    """
    #comment this out and change your func if you don't want to use shell
    url = "https://icerm.brown.edu/"
    max_urls = 10
    func = PowerMethod

    web_scrawler_application(url, max_urls, func)
    Stochastic_matrix_test()