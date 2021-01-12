import datetime as dt

def record_check(record):
    with open('records.txt', 'r', encoding='UTF-8') as line:
        line = line.readline().split()
        if record > int(line[1]):
            line[0], line[1] = '.'.join((str(dt.date.today())).split('-')), str(record)
        line = ' '.join(line)
    with open('records.txt', 'w', encoding='UTF-8') as li:
        print(li.write(line))