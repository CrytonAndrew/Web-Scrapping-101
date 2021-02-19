from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com/")
# print(response.text)

soup = BeautifulSoup(response.text,  "html.parser")
all_articles = soup.find_all(name="a", class_="storylink")
all_upvote_points = soup.find_all(name="span", class_="score")


all_article_titles = [article.getText() for article in all_articles]
all_article_links = [article['href'] for article in all_articles]
all_points = [int(point.getText().split(' ')[0]) for point in all_upvote_points]

print(all_article_titles[all_points.index(max(all_points))])

x = 0
articles_dict = {"Articles": {}}
while x < 30:
    title = all_article_titles[x]
    link = all_article_links[x]
    points = all_points[x]
    dict_article = {
        title: {
            "link": link,
            "points": int(points)
        }
    }
    articles_dict["Articles"].update(dict_article)
    x += 1

# print(articles_dict)

largest = 0




# with open("website.html") as website:
#     contents = website.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
# # Get all the tags
# all_anchor_tags = soup.find_all(name="a")
# for tag in all_anchor_tags:
#     print(tag.getText())  # Get the tags text
#     print(tag.get("href"))  # Get the attributes value
#
#
# # Get a specific tag based on its id or class
# heading = soup.find(name="h1", id="name")
# print(heading.text)
#
# books_heading = soup.find(name="h2", class_="heading")  # class is reserved
# print(books_heading.text)
#
# # Using a hierarchy
# bcad_url = soup.html.body.p.em.a
# print(bcad_url.string)
#
#
# # Using CSS SELECTORS
# url = soup.select_one(selector="p a")  # Getting an a tag that sits inside a p tag
# print(url.string)
#
# all_headings = soup.select(selector=".heading")
# print(all_headings)
#
# last_heading = soup.select_one(selector="#other_pages")
# print(last_heading)
