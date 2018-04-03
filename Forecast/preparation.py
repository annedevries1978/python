import csv

file = 'PSPSCD75RX (1).txt'
target = 'target.txt'
upload_file = 'upload.txt'


def get_last_line():
    last_line = 0
    with open(file, newline='') as f:
        for i, line in enumerate(f, start=1):
            last_line = i
    return last_line


def get_number_of_pages():
    # returns a list with line number where new page data starts
    page = []
    with open(file, newline='') as f:
        for i, line in enumerate(f, start=1):
            if line[135:139] == 'Page':
                page.append(i)
    return page


def create_file():
    # works only for 2 pages
    # TODO: more than 2 pages
    page_list = get_number_of_pages()
    with open(file, newline='') as f:
        with open(target, 'w') as t:
            for i, line in enumerate(f, start=1):
                if 'End of Report' not in line and line != ' \r\n':
                    if i > page_list[0]+10 and i < page_list[1]:
                        t.write(line)
                    elif i > page_list[1] + 11:
                        t.write(line)

def adjust_file():
    # add item numers to lines with only quantities
    with open(target, newline='') as t:
        with open(upload_file, 'w') as u:
            item_line = ""
            for line in t:

                if line[:1] != " ":
                    u.write(line)
                    item_line = line
                else:
                    u.write(item_line[:16]+item_line[16:46]+item_line[46:155]+line[155:173]+'\n')


def get_number_of_items():
    items = []
    with open(target, newline='') as t:
        for line in t:
            if line[:1] != ' ':
                items.append(line[16:46])
    return items


def create_upload():
    lines = 20 * "="
    print(lines)
    pages = get_number_of_pages()
    print("Pages start at lines:")
    print(lines)
    for i in pages:
        print("Page", i)
    print(lines)
    print("Last line is:", get_last_line())
    print(lines)
    create_file()
    items = get_number_of_items()
    print("Items\n",lines, sep='')
    for i, item in enumerate(items):
        if i  > 0:
            print(i, item)

    adjust_file()


create_upload()

def create_csv():
    with open(upload_file, newline='') as u:
        with open("csv_file.txt",'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, dialect='excel-tab')
            for line in u:
                csv_writer.writerow([line[16:46], line[155:163], line[165:173]])

create_csv()