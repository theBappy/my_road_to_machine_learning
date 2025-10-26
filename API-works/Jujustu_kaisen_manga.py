import os
import re
import requests
from zipfile import ZipFile
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def get_all_chapter_links():
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    path = "C:\\chromedriver_win32\\chromedriver.exe"

    url = "https://jujmanga.com"

    pattern = r"\b\/manga\/\b"
    print("1/7 Website loading...")

    driver = webdriver.Chrome(path)

    print("2/7 Website loaded...")
    driver.get(url)

    links = driver.find_elements(by=By.TAG_NAME, value="a")
    print("3/7 List elements found...")

    print("4/7 iterating through links...")

    x = []
    for l in links:
        link = l.get_attribute("href")

        if type(link) == str:
            if re.search(pattern, link):
                x.append(link)

        driver.quit()

        content = "\n".join(x)
        print("6/7 writing link to files...")

        with open('links.txt', "w") as f:
            f.write(content)
        f.close()

        print("7/7 writing link to files completed...")

def scrape_data():
    f = open("links.txt", "r")
    chapters = f.readlines()
    f.close()

    chapters = sorted(
        chapters,
        key=lambda x: int(x.split("-")[3].replace("\n", "").replace("/", ""))
    )

    for i in range(len(chapters)):
        chapter = chapters[i]
        chapter = (
            chapter.split("jujutsu-kaisen-")[1]
            .replace("/", "")
            .replace("\n", "")
            .replace("manga", "chapter")
            .replace("-", "_")
        )

        chapter_no = int(chapter.split("_")[1])

        print("********* Chapter No ***********")
        file_paths = []
        r = requests.get(chapters[i])

        soup = BeautifulSoup(r.content, features="html.parser")

        images = soup.find_all("img")

        folder_name = "{}".format(chapter)
        current_directory = os.getcwd()
        final_directory = os.path.join(current_directory, r"{}".format(folder_name))

        if  not os.path.exists(final_directory):
            os.makedirs(final_directory)

        print("\nDownloading images...")

        for i in range(len(images)):
            image = images[i]

        src = image["src"]

        if re.match(r"^https?://", src)

        f_name = "{}/{}_{}.jpg".format(chapter,chapter, i)
        file_paths.append(f_name)

        f = open(f_name, "wb")

        req = requests(url=src, headers={"User-Agent": "Mozilla/5.0"})

        try:
            f.write(urlopen(req).read())
        finally:
            f.close()

def zip_files():
    file_paths = []
    for root, dirs, files in os.walk("./"):
        for f in files:
            f_name = "{}/{}".format(root, f)
            file_paths.append(f_name)
    file_paths = sorted(
        file_paths[4:],
        key=lambda x: (
            int(re.sub("\D", "", x.split("_")[1])),
            int(re.sub("\D", x.split("_")[-1]))
        )
    )
    with ZipFile("Jujutsu_Kaisen.cbz", "w") as zip:
        for file in file_paths:
            msg = "Zipping {}...".format(file)
            print(msg)
            zip.write(file)

if __name__ == "__main__":
    get_all_chapter_links()
    scrape_data()
    zip_files()

    
