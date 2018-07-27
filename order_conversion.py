#!python3
from bs4 import BeautifulSoup
import csv
from tkinter import *
from tkinter import ttk
from tkinter import filedialog 


def get_file():
    try:
        filename = filedialog.askopenfilename(filetypes =
                                              (("Text File", "*.txt"),
                                               ("All Files","*.*")),
                                             title = "Choose a file.")
        source_file.set(filename)
        return filename
    except ValueError:
        pass


def save_as():
    try:
        dest_file = filedialog.asksaveasfilename(filetypes=(("Txt", "*.txt"),
                                                           ("All Files","*.*")))
        destination_file.set(dest_file)
    except ValueError:
        pass
        

def close_window():
    mainframe.destroy()
    root.destroy()

        
def convert_date(date):
    # convert date to yyyymmdd
    # date format is yyyy-mm-dd
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
    

def create_soup(): 
    # create the soup
    with open('PurchaseOrders_1.xml') as fp:
        soup = BeautifulSoup(fp, 'lxml')
    return soup

    
def orders():
    # find all orders and store in list
    orders = create_soup().find_all('purchaseorder')
    order_list = []
    for order in orders:
        order_date = convert_date(order.orderdate.get_text())
        order_list.append([order['ordernumber'],order_date])
    return order_list
        

def sales_header():        
    # create sales header file
    with open('sales_header.txt', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, dialect='excel-tab')
        writer.writerow(('BSTKD', 'BSTDK'))
        writer.writerows(orders())
 

def order_items():
    # find order items and store in list
    orders = create_soup().find_all('purchaseorder')
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

                  
def sales_items():
    # create sales items file   
    with open('sales_items.txt', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, dialect='excel-tab')
        writer.writerow(('BSTKD', 'KDMAT', 'WMENGC', 'EDATU', 'POSNR'))
        writer.writerows(order_items())
 

def create_files():
    sales_header()
    sales_items()
 
# create the upload files
# create_files()


# TODO Create GUI
root = Tk()
root.title("Forecast Conversion Tool")

mainframe = ttk.Frame(root, padding="3 3 3 3")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

source_file= StringVar()
destination_file = StringVar()
destination_dir = StringVar()

lf = ttk.Labelframe(mainframe, text="Input", padding="5 5 5 5") 
lf.grid(columnspan=4, sticky=(W, E))
lf2 = ttk.Labelframe(mainframe)
lf2.grid(columnspan=4, sticky=(W, E))
source_file_entry = ttk.Entry(lf, width=20, textvariable=source_file)
source_file_entry.grid(column=2, row=1, sticky=(W, E))

destination_file_entry = ttk.Entry(lf, width=40, textvariable=destination_file)
destination_file_entry.grid(column=2, row=2, sticky=(W, E))
ttk.Label(lf, text="Input file").grid(column=1, row=1, sticky=W, padx=5, pady=5)
ttk.Label(lf, text="Output file").grid(column=1, row=2, sticky=W, padx=5, pady=5)


ttk.Button(lf, text="Browse", command=get_file).grid(column=3, row=1, sticky=(W, E))
ttk.Button(lf, text="Save As", command=save_as).grid(column=3, row=2, sticky=(W, E))
ttk.Button(lf2, text="Create Upload",command=create_files).grid(column=1, row=4, sticky=(W,E))
ttk.Button(lf2, text="Cancel", command=close_window).grid(column=2, row=4, sticky=(W, E))

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
for child in lf.winfo_children(): child.grid_configure(padx=5, pady=5)
for child in lf2.winfo_children(): child.grid_configure( padx=5, pady=5)


mainframe.pack()
#source_file_entry.focus()

root.mainloop()


# SAP velden toevoegen
