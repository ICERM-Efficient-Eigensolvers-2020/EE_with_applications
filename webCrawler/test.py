import web_scraper

if __name__ == '__main__':

    url = "https://www.thepythoncode.com"
    max_urls = 50
    A, diG = web_scraper.scraper(url, max_urls)
    print(A)