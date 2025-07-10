import requests
from bs4 import BeautifulSoup
from pdfminer.high_level import extract_text, extract_pages
from pdfminer.layout import LAParams
import os

def main():
    if "generated" not in os.listdir():
        os.mkdir("generated")
    if "pdf" not in os.listdir("generated"):
        os.mkdir("generated/pdf")
    if "txt" not in os.listdir("generated"):
        os.mkdir("generated/txt")
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
                    pdf_text = extract_text(f"generated/pdf/{text}.pdf", laparams = LAParams(boxes_flow = -0.9))
                    pdf_text = pdf_text.replace(
"""A5E System Reference Document

""", "")
                    if not os.path.exists(f"generated/txt/{text}.txt"):
                        file1 = open(f"generated/txt/{text}.txt", "x")
                        file1.write(pdf_text)
                        file1.close()

if __name__ == "__main__":
    main()
