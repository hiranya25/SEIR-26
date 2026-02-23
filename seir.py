import sys
import requests
from bs4 import BeautifulSoup

def main():
    if len(sys.argv) < 2:
        return
    site= sys.argv[1]
    res= requests.get(site)
    page= res.text
    bs=BeautifulSoup(page,"html.parser")
    if bs.title is not None:
        print("Title:")
        t= bs.title.text.strip()
        print(t)
    else:
        print("Title not found")

    if bs.body:
        body_text =bs.body.get_text(separator=" ",strip=True)
        print("Page Body:")
        print(body_text)
    else:
        print("Body not found")
        
    all_link=[]
    for a in bs.find_all("a"):
        link_val= a.get("href")
        if link_val is not None and link_val not in all_link:
            all_link.append(link_val)
    print("\nAll Links:")
    for i in all_link:
        print(i)
if __name__ == "__main__":
    main()

