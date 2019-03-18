def build_twit_stats():
    STATS_FILE = './tweets.csv'
    STATE = {
        'replies': 0,
        'from_web': 0,
        'from_phone': 0,
        'lines_parts': [],
        'total_tweets': 0
    }
    read_data(STATE, STATS_FILE)
    get_stats(STATE)
    print_results(STATE)


def get_percentage(n, total):
    return (n * 100) / total


def read_data(state, source):
    f = open(source, 'r')

    lines = f.read().strip().split("\"\n\"")
    for line in lines:
        state['lines_parts'].append(line.strip().split(','))
    state['total_tweets'] = len(lines)


def inc_stat(state, st):
    state[st] += 1


def get_stats(state):
    for i in state['lines_parts']:
        if (i[1] != '""'):
            inc_stat(state, 'replies')
        if (i[4].find('Twitter Web Client') > -1):
            inc_stat(state, 'from_web')
        else:
            inc_stat(state, 'from_phone')


def print_results(state):
    print("-------- My twitter stats -------------")
    print("%s%% of tweets are replies" % (get_percentage(state['replies'], state['total_tweets'])))
    print("%s%% of tweets were made from the website" % (get_percentage(state['from_web'], state['total_tweets'])))
    print("%s%% of tweets were made from my phone" % (get_percentage(state['from_phone'], state['total_tweets'])))


if __name__ == '__main__':
    # import profile
    # profile.run('build_twit_stats()')
    import cProfile
    import pstats

    profiler = cProfile.Profile()
    profiler.enable()

    build_twit_stats()

    profiler.create_stats()
    stats = pstats.Stats(profiler)
    stats.strip_dirs().sort_stats('cumulative').print_stats()
