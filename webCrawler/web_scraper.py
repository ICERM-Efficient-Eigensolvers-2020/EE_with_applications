#copy right to: https://www.thepythoncode.com/article/extract-all-website-links-python
import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import colorama
import networkx as nx
import matplotlib.pyplot as plt


# init the colorama module
colorama.init()
GREEN = colorama.Fore.GREEN
GRAY = colorama.Fore.LIGHTBLACK_EX
RESET = colorama.Fore.RESET

# initialize the set of links (unique links)
internal_urls = set()
external_urls = set()

def is_valid(url):
    """
    Checks whether `url` is a valid URL.
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def get_all_website_links(url, max_urls):
    """
    Returns all URLs that is found on `url` in which it belongs to the same website
    """
    global diG
    global url_dict
    global idx
    global root
    # all URLs of `url`
    urls = set()
    children = set()
    # domain name of the URL without the protocol
    domain_name = urlparse(url).netloc
    parent = url_dict[url]
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None:
            # href empty tag
            continue

        # join the URL if it's relative (not absolute link)
        href = urljoin(url, href)
        parsed_href = urlparse(href)
        # remove URL GET parameters, URL fragments, etc.
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
        if not is_valid(href):
            # not a valid URL
            continue

        if domain_name not in href:
            # external link
            if href not in external_urls:
                #print(f"{GRAY}[!] External link: {href}{RESET}")
                external_urls.add(href)
            continue

        #found out the internal link

        #new child
        #add some filters to make this rank more meaningful

        if href.endswith('.pdf'):
            continue
        if href not in url_dict.keys():
            idx = idx + 1
            if idx >= max_urls:
                continue
            diG.add_node(idx)
            url_dict[href] = idx

            #prepare new internal_urls to crawl
            if urls != url:
                urls.add(href)
            else:
                print("WHHHHHAAAAT")
            internal_urls.add(href)
        #connection added
        child = url_dict[href]
        diG.add_edge(parent, child)
        children.add(href)
        #print(f"{GREEN}[*] Internal link: {href}{RESET}")

    return urls, children


# number of urls visited so far will be stored here
total_urls_visited = 0

def crawl(url, max_urls):

    """
    Crawls a web page and extracts all links.
    You'll find all links in `external_urls` and `internal_urls` global set variables.
    params:
        max_urls (int): number of max urls to crawl, default is 30.
    """
    global diG
    global url_dict
    global total_urls_visited
    global idx

    total_urls_visited += 1

    if total_urls_visited > max_urls:
        print("!!!Let's dance!!!!")
    else:
        links, children = get_all_website_links(url, max_urls)
        for link in links:
            crawl(link, max_urls=max_urls)

def scraper(url, max_urls):
    global idx
    global diG
    global url_dict
    global total_urls_visited
    global root
    diG = nx.DiGraph()
    url_dict = {}
    idx = 0

    url_dict[url] = idx
    diG.add_node(idx)
    root = url
    crawl(url, max_urls=max_urls)

    print("[+] Total Internal links:", len(internal_urls))
    print("[+] Total External links:", len(external_urls))
    print("[+] Total URLs:", len(external_urls) + len(internal_urls))

    domain_name = urlparse(url).netloc

    # save the internal links to a file
    with open(f"{domain_name}_internal_links.txt", "w") as f:
        for internal_link in internal_urls:
            print(internal_link.strip(), file=f)

    # save the external links to a file
    with open(f"{domain_name}_external_links.txt", "w") as f:
        for external_link in external_urls:
            print(external_link.strip(), file=f)

    #adjacency matrix
    A = nx.to_numpy_matrix(diG)
    return A, diG, url_dict

