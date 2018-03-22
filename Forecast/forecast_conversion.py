import csv
import pprint
'''
    Data uit forecast bestand van Baxi omzetten naar een voor SAP leesbaar format
    De kolomnamen beginnen bij regel 14
    Vanaf regel 67 begint een nieuwe pagina
'''
pp = pprint.PrettyPrinter()
start_line = 14  # start regel vanaf de data gelezen moet worden
last_line = 65  # laatste regel
forecast_data = []  # list om de data in op te slaan


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


def get_new_line_items():
    # geeft de regelnummers waarin een nieuw item begint
    line_counter = 0
    start_line_new_item = [15]  # regel met eerste item
    with open('PSPSCD75RX (2).txt', newline='') as f:
        for line in f:
            line_counter += 1
            if line == ' \r\n' and start_line < line_counter < last_line:
                start_line_new_item.append(line_counter + 1)

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


print(get_new_line_items())
print(len(get_item_numbers()))
pp.pprint(get_item_numbers())
get_column_headers()
forecast_values()
pp.pprint(forecast_data)

