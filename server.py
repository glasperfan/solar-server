from flask import Flask
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
app = Flask(__name__)

@app.route("/")
def hello():
    url = "http://dx.qsl.net/propagation/propagation.html"
    print(url)
    driver = webdriver.Chrome()
    driver.get(url)
    elem = driver.find_element_by_xpath("//*")
    html = elem.get_attribute("outerHTML")
    # html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    print(soup)
    for entry in soup.find_all("td"):
        print(entry)
    return "Hello World!"

hello()

# if __name__ == "__main__":
#     app.run()