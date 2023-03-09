import praw
import pandas as pd

# Read-only instance
reddit_read_only = praw.Reddit(client_id="anJb3mWjKA1Qy3uz5FPUFg",         # your client id
                               client_secret="wiA-tmhSQTApuzMSocuw4_1_0B8WpQ",    # your client secret
                               user_agent="491_Scraper")   # your user agent


subreddit = reddit_read_only.subreddit("datascience")

posts = subreddit.top("month")
# Scraping the top posts of the current month

posts_dict = {"Title": [], "Post Text": [],
              "ID": [], "Score": [],
              "Total Comments": [], "Post URL": []
              }

for post in posts:
    # Title of each post
    posts_dict["Title"].append(post.title)

    # Text inside a post
    posts_dict["Post Text"].append(post.selftext)

    # Unique ID of each post
    posts_dict["ID"].append(post.id)

    # The score of a post
    posts_dict["Score"].append(post.score)

    # Total number of comments inside the post
    posts_dict["Total Comments"].append(post.num_comments)

    # URL of each post
    posts_dict["Post URL"].append(post.url)

# Saving the data in a pandas dataframe
top_posts = pd.DataFrame(posts_dict)
top_posts

top_posts.to_csv("Top_Posts.csv", index=True)