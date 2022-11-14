#encoding:utf-8

from utils import get_url
from utils import SupplyResult

subreddit = 'disneyvacation'
t_channel = '@r_disneyvacation'


def send_post(submission, r2t):
	what, url = get_url(submission)
	if what != 'img':
		return SupplyResult.DO_NOT_WANT_THIS_SUBMISSION
	title = submission.title
	link = submission.shortlink

	text = '{title}\n\n{link}\n{channel}'.format(
		title=title, link=link, channel=t_channel)
	return (
		SupplyResult.DO_NOT_WANT_THIS_SUBMISSION
		if r2t.dup_check_and_mark(url) is True
		else r2t.send_gif_img(what, url, text)
	)
