#encoding:utf-8

from utils import get_url, weighted_random_subreddit


t_channel = '@tamileezham'
subreddit = weighted_random_subreddit({
    'eelam': 1.0,
    # If we want get content from several subreddits
    # please provide here 'subreddit': probability
    # 'any_other_subreddit': 0.02
})


def send_post(submission, r2t):
    what, url, ext = get_url(submission)
    title = submission.title
    link = submission.shortlink
    text = f'{title}\n{link}'

    if what == 'text':
        punchline = submission.selftext
        text = f'{title}\n\n{punchline}\n\n{link}'
        return r2t.send_text(text)
    elif what == 'other':
        base_url = submission.url
        text = f'{title}\n{base_url}\n\n{link}'
        return r2t.send_text(text)
    elif what == 'album':
        base_url = submission.url
        text = f'{title}\n{base_url}\n\n{link}'
        r2t.send_text(text)
        r2t.send_album(url)
        return True
    elif what in ('gif', 'img'):
        if r2t.dup_check_and_mark(url) is True:
            return False
        return r2t.send_gif_img(what, url, ext, text)
    else:
        return False
