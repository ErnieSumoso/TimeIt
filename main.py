import datetime


def set_data_collection_type():
    collect_type = input('Choose your data collection type (T = time of the day, C = counting hours & minutes)\n')
    while collect_type not in ['t', 'T', 'c', 'C']:
        collect_type = input('That is not right, try again (T = time of the day, C = counting hours & minutes)\n')
    return 't' if collect_type in ['t', 'T'] else 'c'


def collect_data_by_count():
    time_sum, sleeping = 0.0, False
    wake_up_time = ask_for_time('At what time did you woke up? '
                                'Enter 1 or 2 numbers: hour (0-23) and minutes (0-59)\n')
    print(f'So you woke up at {wake_up_time}')
    time_sum += wake_up_time.hour + wake_up_time.minute / 60
    while time_sum <= 24.0 and not sleeping:
        activity_name, hours, minutes = get_activity_data('What did you do next & for how many hours and minutes? '
                                                          'Enter 1 or 2 numbers: hours (0-23) and minutes (0-59)\n')
        print(f'So you did {activity_name} for {str(hours)} hours and {str(minutes)} minutes')
        time_sum += hours + minutes / 60
        current_time = datetime.time(int(time_sum), int((time_sum - int(time_sum)) * 60))
        print(f'It is {current_time} now.')


def collect_data_by_time():
    pass


def get_activity_data(msg, wrong_msg='That is not right, please try again\n'):
    activity_name, hours, minutes, done = '', 0, 0, False
    while not done:
        try:
            activity_data = input(msg).split()
            activity_name = activity_data[0]
            hours = int(activity_data[1])
            minutes = int(activity_data[2]) if len(activity_data) > 2 else 0
            done = True
        except (KeyError, ValueError):
            print(wrong_msg)
    return activity_name, hours, minutes


def ask_for_time(msg, wrong_msg='That is not right, please try again\n'):
    done, input_time = False, datetime.time()
    while not done:
        try:
            input_time = input(msg)
            numbers = input_time.split()
            hour = int(numbers[0])
            minutes = int(numbers[1]) if len(numbers) > 1 else 0
            input_time = datetime.time(hour, minutes)
            done = True
        except (KeyError, ValueError):
            print(wrong_msg)
    return input_time


if __name__ == '__main__':
    collection_type = set_data_collection_type()
    if collection_type == 't':
        collect_data_by_time()
    else:
        collect_data_by_count()
