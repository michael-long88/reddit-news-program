# reddit-news-program

Flask web app designed to grab and display the top 10 reddit.com/r/news stories from the last 24 hours.
  
Using `PRAW`, the application first grabs the top 10 submissions from r/news which supplies the submission title and the URL 
for the actual news article. Then, using `BeautifulSoup`, the app scrapes the article to grab the story text and the story image 
if available. 
  
The data is then presented to the user in a web page with the title (hyperlinked to the article itself), the image, and a brief
description (appends "..." to anything with a lenght over 200).
