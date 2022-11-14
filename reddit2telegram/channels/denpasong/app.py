#encoding:utf-8

from urllib.parse import urlparse

from utils import get_url, weighted_random_subreddit
from utils import SupplyResult


t_channel = '@denpasong'
subreddit = weighted_random_subreddit({
    'denpa': 0.5,
    'denpasong': 0.5,
})


def send_post(submission, r2t):
    what, url = get_url(submission)
    title = submission.title
    link = submission.shortlink
    text = f'{title}\n{link}'

    if (
        what == 'text'
        or what == 'album'
        or what not in ('other', 'gif', 'img')
    ):
        return SupplyResult.DO_NOT_WANT_THIS_SUBMISSION
    elif what == 'other':
        domain = urlparse(url).netloc
        if domain in ('www.youtube.com', 'youtu.be'):
            text = f'{title}\n{url}\n\n{link}'
            return r2t.send_text(text)
        else:
            return SupplyResult.DO_NOT_WANT_THIS_SUBMISSION
    else:
        return r2t.send_gif_img(what, url, text)
