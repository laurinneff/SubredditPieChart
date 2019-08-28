import praw

reddit = praw.Reddit('bot')
subreddit = reddit.subreddit('all')
for submission in subreddit.stream.submissions():
    print(submission.permalink)

    with open("subreddits.txt", "a") as subsfile:
        subsfile.write('r/' + submission.subreddit.display_name + '\n')
