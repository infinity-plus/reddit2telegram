#encoding:utf-8

import os

import channels_stuff


def main(sub, channel, tags):
    channel_dir = os.path.join('channels', channel.lower())
    if os.path.isdir(channel_dir):
        print('Directory already exists.')
        return
    os.makedirs(channel_dir)
    with open(os.path.join(channel_dir, '__init__.py'), 'w'):
        pass
    with open(os.path.join(channel_dir, 'app.py'), 'w') as app_file:
        app_file.write('''#encoding:utf-8

subreddit = '{sub_name}'
t_channel = '@{channel_name}'


def send_post(submission, r2t):
    return r2t.send_simple(submission)
'''.format(sub_name=sub, channel_name=channel))

    with open(os.path.join(channel_dir, 'tags.txt'), 'w') as tags_file:
        tags_file.write(tags.lower())

    return '| [/r/{sub_name}](https://www.reddit.com/r/{sub_name}/) | [@{channel_name}](https://t.me/{channel_name}) | 1 hour |'.format(
        sub_name=sub, channel_name=channel
    )


def run_script(channel):
    os.system(f'python supplier.py --sub {channel.lower()}')


def add_to_git(channel):
    os.system(f'git add channels/{channel.lower()}/*')


def commit(channel):
    os.system('git commit -a -m "@{channel_name}"'.format(channel_name=channel.lower()))


def old_fashioned_way():
    subreddit_name = input('Subreddit name: ')
    channel_name = input('Channel name: ')
    tags = input('#Tags #in #that #way: ')

    print('Submodule is created.')
    print(main(subreddit_name, channel_name, tags))
    print(channel_name.lower())

    print('Run the bot for the first time.')
    run_script(channel_name)
    print('Done.')

    for _ in range(10):
        yes = input('Ready to commit? ')
        if yes == 'y':
            print('Add to git.')
            add_to_git(channel_name)
            print('Done. Will commit.')
            commit(channel_name)
            print('Done.')
            break


def med_fashioned_way():
    subreddit_name = input('Subreddit name: ')
    channel_name = input('Channel name: ')
    tags = input('#Tags #in #that #way: ')

    print('Submodule is created.')
    channels_stuff.set_new_channel(channel_name, subreddit=subreddit_name, tags=tags.lower())
    print(channel_name.lower())

    print('Run the bot for the first time.')
    run_script(channel_name)
    print('Done.')

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--old', action='store_true')
    args = parser.parse_args()

    if args.old:
        old_fashioned_way()
    else:
        med_fashioned_way()
