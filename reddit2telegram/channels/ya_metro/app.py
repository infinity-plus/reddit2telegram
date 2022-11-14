#encoding:utf-8

from urllib.parse import urlparse

from utils import get_url, weighted_random_subreddit
from utils import SupplyResult


t_channel = '@ya_metro'
subreddit = weighted_random_subreddit({'Subways': 0.6,
    'LondonUnderground': 0.4,
    'Trams': 0.3
})


def send_post(submission, r2t):
    what, url = get_url(submission)
    title = submission.title
    link = submission.shortlink
    text = f'{title}\n{link}'

    if what == 'text':
        if submission.score < 4:
            return SupplyResult.DO_NOT_WANT_THIS_SUBMISSION
        punchline = submission.selftext
        text = '{title}\n\n{body}\n\n{link}'.format(
            title=title, body=punchline, link=link)
        return r2t.send_text(text, disable_web_page_preview=True)
    elif what == 'album':
        base_url = submission.url
        text = f'{title}\n{base_url}\n\n{link}'
        r2t.send_text(text)
        return r2t.send_album(url)
    elif what == 'other':
        domain = urlparse(url).netloc
        if domain in ('www.youtube.com', 'youtu.be') or submission.score >= 4:
            text = f'{title}\n{url}\n\n{link}'
            return r2t.send_text(text)
        else:
            return SupplyResult.DO_NOT_WANT_THIS_SUBMISSION
    elif what in ('gif', 'img'):
        return r2t.send_gif_img(what, url, text)
    else:
        return SupplyResult.DO_NOT_WANT_THIS_SUBMISSION
