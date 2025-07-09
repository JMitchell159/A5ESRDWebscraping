import requests
from bs4 import BeautifulSoup
from pdfminer.high_level import extract_text
import os

def main():
    url = "https://a5esrd.com"
    r = requests.get(url + "/a5esrd")
    soup = BeautifulSoup(r.content, "html.parser")
    a_sections = soup.find_all('a')
    for link in a_sections:
        href = str(link.get('href'))
        text = "_".join(str(link.string).split(" "))
        if "pdf" in href:
            if True in list(map(lambda x: x in href, ["a5e", "A5E", "DDG", "GPG"])):
                if True not in list(map(lambda x: x in href, ["ogl", "extras"])):
                    sub_url = url + href
                    r1 = requests.get(sub_url, params={"downloadformat": "pdf"})
                    if not os.path.exists(f"generated/pdf/{text}.pdf"):
                        file = open(f"generated/pdf/{text}.pdf", "xb")
                        file.write(r1.content)
                        file.close()
                    pdf_text = extract_text(f"generated/pdf/{text}.pdf")
                    if not os.path.exists(f"generated/txt/{text}.txt"):
                        file1 = open(f"generated/txt/{text}.txt", "x")
                        file1.write(pdf_text)
                        file1.close()

if __name__ == "__main__":
    main()
