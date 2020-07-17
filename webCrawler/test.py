import web_scraper
import matplotlib.pyplot as plt
if __name__ == '__main__':

    url = "https://icerm.brown.edu/"
    max_urls = 10
    A, diG, url_dict = web_scraper.scraper(url, max_urls)
    plt.spy(A, markersize=10)
    plt.savefig(f'{max_urls}_scraper')
    plt.show()

    A[1,1] = 0
    plt.spy(A)
    plt.show()
    print(A)