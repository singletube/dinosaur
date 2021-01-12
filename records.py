import datetime as dt
import getpass

def record_check(record):
    with open('records.txt', 'r', encoding='UTF-8') as line:
        line = line.readline().split()
        if record > int(line[2]):
            ia = str(dt.date.today()).split('-')
            ia[0], ia[1], ia[2] = ia[2], ia[1], ia[0][:-2]
            ia = '.'.join(ia)
            line[0], line[1], line[2] = getpass.getuser(), ia,\
                                        str(record)
        line = ' '.join(line)
    with open('records.txt', 'w', encoding='UTF-8') as li:
        print(li.write(line))