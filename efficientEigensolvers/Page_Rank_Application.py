import ../WebCrawler/scraper.scraper as scraper
import Page_Rank_Utils as pru


def web_scrawler_application(url, max_urls, weight=0.15, func):
    A, diG = scraper(url, max_urls)
    M = pru.stochastic_transition_matrix_from_G(diG, weight, False)
    return func(M)

if __name__ == '__main__':

    print("###ICERM domain test###")
    import argparse

    parser = argparse.ArgumentParser(description="Link Extractor Tool with Python")
    parser.add_argument("url", help="The URL to extract links from.")
    parser.add_argument("-m", "--max-urls", help="Number of max URLs to crawl, default is 30.", default=30, type=int)
    parser.add_argument("func", help="The eigensolver to be tested.")

    args = parser.parse_args()
    url = args.url
    max_urls = args.max_urls
    func = args.func

    """comment this out and change your func if you don't want to use shell
    url = "https://icerm.brown.edu"
    max_urls = 100
    func = ###change me###
    """
    web_scrawler_application(url, max_urls, func)