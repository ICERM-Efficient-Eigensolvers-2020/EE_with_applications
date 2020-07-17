import web_scraper

if __name__ == '__main__':

    url = "https://icerm.brown.edu/"
    max_urls = 10
    A, diG = web_scraper.scraper(url, max_urls)
    print(A)