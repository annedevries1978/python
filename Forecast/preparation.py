import csv, itertools, pprint
from datetime import datetime 
import os

file = 'PSPSCD75RX (3).txt'  # file from customer with forecast data
target = 'target.txt'  # target file
upload_file = 'upload.txt'  # upload file. used for creating csv file

# check if the target and upload file exists. If not create them.

def get_last_line(source_file):
    # return last line of file
    last_line = 0
    with open(source_file, newline='') as f:
        for i, line in enumerate(f, start=1):
            last_line = i
    return last_line


def get_number_of_pages(source_file):
    # returns a list with line number where new page data starts
    # look for Page in in line
    page = []
    with open(source_file, newline='') as f:
        for i, line in enumerate(f, start=1):
            if line[135:139] == 'Page':
                page.append(i)
    return page


def line_start_numbers(source_file):
    # return a list with where the lines of the pages start
    page_list = get_number_of_pages(source_file)
    start_lines = []
    for i in page_list:
        start_lines.append(i + 11)

    return start_lines


def clear_target():
    open('target.txt', 'w').close()
    # open and closes target file so it is empty


def read_page(source_file):
    # read all lines from the pages.
    # starts reading at the line from line_start_numbers()
    # After the start line a maximum of 51 lines contain data.
    # Data is appended to the target file
    clear_target()
    line_start = line_start_numbers(source_file)
    for line_number in line_start:
        with open(source_file) as f:
            with open(target, 'a') as t:
                for line in itertools.islice(f, line_number, line_number+51):
                    if 'End of Report' not in line and line.isspace() == False:
                        t.write(line)


def adjust_file():
    # add item numbers to lines with only quantities
    with open(target) as t:
        with open(upload_file, 'w') as u:
            item_line = ""
            for line in t:
                if line[:1] != " ":
                    u.write(line)
                    item_line = line
                else:
                    u.write(item_line[:16]+item_line[16:46]+item_line[46:155]+line[155:173]+'\n')


def get_number_of_items():
    # Returns a list with all Rubitech item numbers
    items = []
    with open(target) as t:
        for line in t:
            if line[:1] != ' ':
                items.append(line[16:24])
    return items


def prepare_data(source_file):
    read_page(source_file)
    adjust_file()
    # prepare data for excel writer
    # create a two dimensional list with product, quantity and date
    with open(upload_file) as f:
        data = [[line[16:24], 
                int(line[155:163].replace(',', '')), # convert quantity to int
                 line[165:173]] for line in f]
        for line in data:
            date = datetime.strptime(line[2], '%d/%m/%y')
            week = datetime.strftime(date, '%W')
            # convert week to int and append to line
            line.append(int(week)) 
    return data
