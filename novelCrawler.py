import requests, bs4, time

url = "NOVEL TITLE URL"
htmlFile = requests.get(url)
htmlFile.encoding = "gbk"
objSoup = bs4.BeautifulSoup(htmlFile.text, "lxml")

bookAuthor = objSoup.find("meta", property="og:novel:author")
bookTitle = objSoup.find("meta", property="og:novel:book_name")
bookDescription = objSoup.find("meta", property="og:description")
'''
print("作者：", bookAuthor["content"])
print("書名：", bookTitle["content"])
print("描述：", bookDescription["content"].strip())
'''
openfile = open(bookTitle["content"] + "目錄.txt", mode="a")
print("作者：", bookAuthor["content"], file=openfile)
print("書名：", bookTitle["content"], file=openfile)
print("描述：", bookDescription["content"].strip(),"\n", file=openfile)
openfile.close()

storys = objSoup.find("div", "listmain")
story = storys.find_all("dt")
print(story[1].text)
print()
sto = storys.find_all("dd")
sto = sto[12:]
for ch in sto:
    openfile = open(bookTitle["content"] + "目錄.txt", mode="a")
    print(ch.text, file=openfile)
    openfile.close()
print("目錄儲存成功")

for page in range(10142391, 10142392):
    storyContent=""
    chapter_url = url + str(page) + ".html"
    htmlFile2 = requests.get(chapter_url)
    htmlFile2.encoding = "gbk"
    objSoup2 = bs4.BeautifulSoup(htmlFile2.text, "lxml")
    title = objSoup2.find("h1")
    storyContent = storyContent + title.text + "\n"
    contents = objSoup2.find("div", id="content")
    for content in contents:
        if type (content) == bs4.element.NavigableString:
            txt = content.strip()
            if type(txt) == str and txt !="":
                storyContent = storyContent + txt + "\n\n"
    fn = title.text
    with open(fn + ".txt", "a", encoding="utf-8") as obj:
        obj.write(storyContent)
    print("小說 %s 儲存成功" % title.text)
    #time.sleep(0.5)
