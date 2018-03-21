import csv
import pprint

'''
    Data uit forecast bestand van Baxi omzetten naar een voor SAP leesbaar format
    De kolomnamen beginnen bij regel 14
    Vanaf regel 67 begint een nieuwe pagina
'''
pp = pprint.PrettyPrinter()


def convert_spaces_to_comma():
    with open('C:\\Users\\anv\\Desktop\\baxi.txt', newline='') as f, open('C:\\Users\\anv\\Desktop\\format_test.txt',
                                                                          '+w', newline='') as f2:
        reader = csv.reader(f, delimiter=' ')
        writer = csv.writer(f2)
        for row in reader:
            writer.writerow(row)


def remove_duplicate_comma():
    y = []
    with open('C:\\Users\\anv\\Desktop\\format_test.txt') as f:
        for line in f:
            # loop over characters in de lijn 
            for x in (range(len(line))):
                print(line[x], end='')


def open_forecast_file():
    forecast_data = []
    line_counter = 0
    with open('C:\\Users\\anv\\Downloads\\PSPSCD75RX (2).txt', newline='') as f:
        for line in f:
            line_counter += 1
            if line_counter == 14:  # eerste regel met kolomnamen
                customer_item = line[:16]
                rubitech_item = line[16:46]
                forecast_data.append([customer_item, rubitech_item])
                '''forecast_data.append(line[140:149])  # Order/Forecast
                forecast_data.append(line[155:163])  # aantallen
                forecast_data.append(line[165:173])  # datum'''

            elif line_counter == 15:  # eerste regel met item data
                customer_item = line[:16]
                rubitech_item = line[16:46]
                forecast_data.append([customer_item, rubitech_item])
            elif line_counter > 15 and line not in [' \n\r']:
                forecast_data.append([customer_item, rubitech_item])

            print(line_counter)
    pp.pprint(forecast_data)


open_forecast_file()