#encoding:utf-8

from utils import get_url
from utils import SupplyResult


subreddit = 'chemicalreactiongifs'
t_channel = '@r_chemicalreactiongifs'
footer = f'by {t_channel}'


def send_post(submission, r2t):
    what, url = get_url(submission)
    title = submission.title
    link = submission.shortlink
    text = f'{title}\n{link}\n\n{footer}'
    if what == 'gif' and r2t.dup_check_and_mark(url) is True or what != 'gif':
        return SupplyResult.DO_NOT_WANT_THIS_SUBMISSION
    else:
        return r2t.send_gif_img(what, url, text)
