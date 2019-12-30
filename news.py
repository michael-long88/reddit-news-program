import os
import praw
import requests
from bs4 import BeautifulSoup
import time

CLIENT_ID = os.environ.get('PRAW_CLIENT_ID')
CLIENT_SECRET = os.environ.get('PRAW_SECRET')
USERNAME = os.environ.get('PRAW_USERNAME')
PASSWORD = os.environ.get('PRAW_PASSWORD')
USER_AGENT = os.environ.get('PRAW_USER_AGENT')


def get_top_10() -> list:
    submissions = get_top_10_submissions()
    top_10 = get_top_10_images_and_descriptions(submissions)

    return top_10


def get_top_10_submissions() -> list:
    top_10 = []
    reddit_instance = praw.Reddit(client_id=CLIENT_ID,
                                  client_secret=CLIENT_SECRET,
                                  user_agent=USER_AGENT)

    for submission in reddit_instance.subreddit('news').top('day', limit=10):
        top_10.append(submission)

    return top_10


def get_top_10_images_and_descriptions(submissions) -> list:
    start_time = time.time()
    top_10_with_preview = []
    for submission in submissions:
        response = requests.get(submission.url)
        beautiful_soup = BeautifulSoup(response.content, 'html.parser')
        story = get_article_story(beautiful_soup)
        image_url = get_image_url(beautiful_soup)
        top_10_with_preview.append({
            'title': submission.title,
            'description': story,
            'image': image_url,
            'url': submission.url
        })

    print(f"total run time: {time.time() - start_time}")
    return top_10_with_preview


def get_article_story(soup) -> str:
    article = soup.find_all('p')
    article_story = "".join([text.get_text() for text in article])
    if len(article_story) > 200:
        article_story = article_story[:200] + "..."
    return article_story


def get_image_url(soup) -> str:
    image_meta = soup.find('meta', attrs={'property': 'og:image'})
    image_url = image_meta['content']
    return image_url
