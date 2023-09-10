from datetime import time


def set_data_collection_type():
    collect_type = input('Choose your data collection type (T = time of the day, C = counting hours)\n')
    while collect_type not in ['t', 'T', 'c', 'C']:
        collect_type = input('That is not right, please try again (T = time of the day, C = counting hours)\n')
    return 't' if collect_type in ['t', 'T'] else 'c'


def collect_data_by_time():
    time_sum = 0.0
    wake_up_time = ask_for_time('At what time did you woke up? Write 1 or 2 numbers:\n'
                                '1st: Hour (0-23)\n'
                                '2nd: Minutes (0-59)\n')


def collect_data_by_count():
    pass


def ask_for_time(msg, wrong_msg = 'That is not right, please try again'):
    done, input_time = False, time()
    while not done:
        try:
            input_time = input(msg)
            numbers = input_time.split()
            hour = int(numbers[0])
            minutes = int(numbers[1]) if len(numbers) > 1 else 0
            input_time = time(hour, minutes)
            done = True
        except (KeyError, ValueError):
            print(wrong_msg)
    print(input_time)
    return input_time


if __name__ == '__main__':
    collection_type = set_data_collection_type()
    if collection_type == 't':
        collect_data_by_time()
    else:
        collect_data_by_count()


