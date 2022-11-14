#encoding:utf-8

from urllib.parse import urlparse

from utils import get_url
from utils import SupplyResult


t_channel = '@r_mlp'
subreddit = 'mylittlepony'


def send_post(submission, r2t):
    what, url = get_url(submission)
    title = submission.title
    link = submission.shortlink
    text = f'{title}\n{link}'

    if what == 'text' or what not in ('album', 'other', 'gif', 'img'):
        return SupplyResult.DO_NOT_WANT_THIS_SUBMISSION
    elif what == 'album':
        base_url = submission.url
        text = f'{title}\n{base_url}\n\n{link}'
        r2t.send_text(text)
        return r2t.send_album(url)
    elif what == 'other':
        domain = urlparse(url).netloc
        if domain in ('www.youtube.com', 'youtu.be'):
            text = f'{title}\n{url}\n\n{link}'
            return r2t.send_text(text)
        else:
            return SupplyResult.DO_NOT_WANT_THIS_SUBMISSION
    else:
        return r2t.send_gif_img(what, url, text)
