import praw

# Read-only instance
reddit_read_only = praw.Reddit(client_id="anJb3mWjKA1Qy3uz5FPUFg",         # your client id
                               client_secret="wiA-tmhSQTApuzMSocuw4_1_0B8WpQ",    # your client secret
                               user_agent="491_Scraper")   # your user agent


subreddit = reddit_read_only.subreddit("AskNetsec")

# Display the name of the Subreddit
print("Display Name:", subreddit.display_name)

# Display the title of the Subreddit
print("Title:", subreddit.title)

# Display the description of the Subreddit
print("Description:", subreddit.description)
