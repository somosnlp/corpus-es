import pandas as pd
import newspaper as ns
from bs4 import BeautifulSoup
import requests
from pathlib import Path


def donwload(url, directory):
    print("t...Descargando la imagen: " + url)
    image = requests.get(url)
    is_save = False
    if image.status_code == 200:
        is_save = True
        name_save = directory / url.split("/")[-1]
        with open(name_save, 'wb') as f:
            f.write(image.content)
    return name_save, is_save


def next_link(soup):
    link = soup.find("a", {"class": "next ga"})
    if link is None:
        return None
    return link.get("href")

def scrapy_page(link):
    directorio = Path("images")
    nombres_de_archivos = [archivo.name for archivo in directorio.iterdir() if archivo.is_file()]
    nombres_de_archivos = list(map(lambda x: x.replace(".csv", ""), nombres_de_archivos))
    images_ns = ns.Article(link)
    images_ns.download()
    soup = BeautifulSoup(images_ns.html, 'html.parser')
    images = soup.find_all("img", {"class":  "imagen"})
    print(f"Scraping {link} ... ")
    list_values = [] 
    name_save = link.split("/")[-1].replace(".html", "")
    path = directorio / name_save
    if path.name in nombres_de_archivos:
        return next_link(soup)
    path.mkdir(parents=True, exist_ok=True)
    for image in images:
        url = image.get('src')  
        title = image.get('alt')  
        path_image,is_save = donwload(url, path)  
        values_dict = {'url': url, 'title': title, 'path': path_image,  "is_save ":is_save}  
        list_values.append(values_dict)
    pd.DataFrame(list_values).to_csv(f'images/{name_save}.csv', index=False)
    next = next_link(soup)
    return next

def main():
    read_list = pd.read_csv("links_scrapped_images_2.csv")
    url = "https://www.recetasgratis.net"
    d = ns.Article(url)
    d.download()
    soup = BeautifulSoup(d.html, 'html.parser')
    links = soup.find('div', {'class': 'categorias-home'}).find_all('a', {'class': 'titulo'})
    links = [link.get('href') for link in links]
    links_scrapped = []
    for link in links:
        if link in read_list.values:
            continue
        try:
            print(link)
            link = scrapy_page(link)
            links_scrapped.append(link)
        except Exception as e:
            print(e)
            read_list.values.append(link)
            pd.DataFrame(links_scrapped).to_csv(f'links_scrapped_images_2.csv', index=False)
            return
if __name__ == '__main__':
    main()