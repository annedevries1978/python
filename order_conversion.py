#!python3
from bs4 import BeautifulSoup
import csv

# convert date to yyyymmdd
# date format is yyyy-mm-dd
def convert_date(date):
    date = str(date).replace('-','')
    return date


def create_line_numbers(line):
# line numers in SAP are of length 6
# to upload items we need to convert the line item to length 6
# 1 needs to be 000001
    line = str(line)
    length = len(line)
    number_of_zero_required = 6 - length
    return number_of_zero_required * '0' + line
    
    
with open('PurchaseOrders_1.xml') as fp:
    soup = BeautifulSoup(fp, 'lxml')


def orders():
    orders = soup.find_all('purchaseorder')
    order_list = []
    for order in orders:
        order_date = convert_date(order.orderdate.get_text())
        order_list.append([order['ordernumber'],order_date])
    return order_list
        

# create sales header file
with open('sales_header.txt', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, dialect='excel-tab')
    writer.writerow(('BSTKD', 'BSTDK'))
    writer.writerows(orders())
 

def order_items():
    orders = soup.find_all('purchaseorder')
    order_item_list = []
    line_number = 0
    for order in orders:
        lines = order.find_all('purchaseorderline')
        for line in lines:
            line_number += 1
            date = convert_date(line.receiptdate.get_text())
            order_item_list.append([order['ordernumber'],line.item['code'], 
                  '%.3f' % int(line.quantity.get_text()),
                  date, create_line_numbers(line_number)])
        # reset line number
        line_number = 0
    return order_item_list

                  
# create sales items file   
with open('sales_items.txt', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, dialect='excel-tab')
    writer.writerow(('BSTKD', 'KDMAT', 'WMENGC', 'EDATU', 'POSNR'))
    writer.writerows(order_items())