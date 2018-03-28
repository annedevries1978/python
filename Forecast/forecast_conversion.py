
import pprint
'''
    Data uit forecast bestand van Baxi omzetten naar een voor SAP leesbaar format
    De kolomnamen beginnen bij regel 14
    Eerste item begint op regel 15
    Vanaf regel 67 begint een nieuwe pagina
'''
pp = pprint.PrettyPrinter()
start_line = 14  # start regel vanaf de data gelezen moet worden
last_line = 102  # laatste regel
forecast_data = []  # list om de data in op te slaan
file = 'PSPSCD75RX (2).txt'


def get_number_of_pages():
    # returns a list with line number where new page data starts
    page_counter = 0
    page = []
    with open(file, newline='') as f:
        for i, line in enumerate(f, start=1):
            if line[135:139] == 'Page':
                page.append(i+12)
    return page


def get_column_headers():
    line_counter = 0
    with open('PSPSCD75RX (2).txt', newline='') as f:
        for line in f:
            line_counter += 1
            if line_counter == 14:  # eerste regel met kolomnamen
                customer_item = line[:16]
                rubitech_item = line[16:46]
                aantallen = line[155:163]
                datum = line[165:173]
                forecast_data.append([customer_item, rubitech_item, aantallen, datum])
                return [customer_item, rubitech_item, aantallen, datum]


def get_new_line_items():
    # geeft de regelnummers waarin een nieuw item begint
    start_line_new_item = [15]  # regel met eerste item
    with open('PSPSCD75RX (2).txt', newline='') as f:
        for i, line in enumerate(f, start=1):
            if line == ' \r\n' and start_line < i:
                start_line_new_item.append(i+1)
    for x in start_line_new_item:
        print("Nieuw item startregel:", x)
    return start_line_new_item


def get_item_numbers():
    #  per nieuwe regel de item nummers ophalen.
    items = []
    line_counter = 0
    new_line_number = get_new_line_items()
    with open('PSPSCD75RX (2).txt', newline='') as f:
        for line in f:
            line_counter += 1
            for x in range(len(new_line_number)):
                if line_counter == new_line_number[x]:
                    customer_item = line[:16]
                    rubitech_item = line[16:46]
                    items.append([customer_item, rubitech_item])
        return items


def forecast_values():
    line_counter = 0
    new_line_number = get_new_line_items()
    with open('PSPSCD75RX (2).txt', newline='') as f:
        for line in f:
            line_counter += 1
            for x in range(len(new_line_number)):
                if x < 3:
                    if new_line_number[x] <= line_counter < new_line_number[x+1]:
                        forecast_data.append(get_item_numbers()[x] + [line[155:163]] + [line[165:173]])


print("De headers zijn\n", get_column_headers())
print(get_number_of_pages())
print("Dit zijn de item nummers", get_item_numbers())