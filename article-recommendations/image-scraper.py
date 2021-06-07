from bs4 import BeautifulSoup
import requests
from requests.api import get
import inspect


def get_image(url):
  res = requests.get(url)
  html = res.content
  soup = BeautifulSoup(markup=html, features="html.parser")

  # $(`meta[name=${name}]`).attr('content') ||
  # $(`meta[name="og:${name}"]`).attr('content') ||
  # $(`meta[name="twitter:${name}"]`).attr('content');

  meta = soup.select_one(
      "meta[name=image]") or soup.select_one(
      "meta[name=og\:image]") or soup.select_one(
      "meta[name=twitter\:image\:src]") or soup.select_one(
      "meta[property=image]") or soup.select_one(
      "meta[property=og\:image]") or soup.select_one(
      "meta[property=twitter\:image\:src]")

  return meta.get("content") if meta else ""


url = get_image(
    "https://www.thoughtworks.com/pt/insights/blog/discutindo-devops-na-pratica")
print(url)
