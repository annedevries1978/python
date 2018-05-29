import xlsxwriter
import os 
from tkinter import *
from tkinter import ttk, messagebox
from tkinter import filedialog 
from xlsxwriter.utility import xl_rowcol_to_cell
from datetime import datetime, date
import preparation

'''
Load a forecast file fro customer and load the data into an excel file
Using a GUI instead of the comandline to specify filenames 
'''
#check if files exist:
#preparation.file_check()

week_numbers = [i+1 for i in range(52)]
week_num = datetime.strftime(date.today(), '%W')
week_row = week_numbers[int(week_num)-1:] + week_numbers[:int(week_num)-1]

def product_list():
    product_list = preparation.get_number_of_items()
    return product_list


def get_file():
    try:
        filename = filedialog.askopenfilename(filetypes =
                                              (("Text File", "*.txt"),
                                               ("All Files","*.*")),
                                             title = "Choose a file.",
                                             initialdir=os.environ['HOME'])
        source_file.set(filename)
        return filename
    except ValueError:
        pass


def save_as():
    try:
        dest_file = filedialog.asksaveasfilename(filetypes=(("Excel", "*.xlsx"),
                                                           ("All Files","*.*")),
                                                defaultextension=".xlsx",
                                                initialdir=os.environ['HOME'])
        destination_file.set(dest_file)
    except ValueError:
        pass


def get_data():
    data = preparation.prepare_data(source_file.get())
    return data


def insert_week_nums(worksheet):
    print("inserting weeks")
    row = 0
    col = 1
    for week in week_row:
        worksheet.write(row, col, week)
        col += 1


def insert_products(p_list, worksheet):
    print("Inserting products")
    row = 1
    col = 0
    for product in p_list:
        worksheet.write(row, col, product)
        row += 1


def insert_forecast(worksheet2, data):
    row = 0
    for line in data:
        col = 0
        for item in line:
            worksheet2.write(row, col, item)
            col += 1
        row += 1


def insert_formula(worksheet):
    num_of_products = len(product_list())
    # Start at second row
    row = 1
    for y in range(num_of_products):
        col = 1 # for each loop reset col to 1
        product_cell = xl_rowcol_to_cell(row, 0)
        print(product_cell)
        for x in range(1,53):
            cell = xl_rowcol_to_cell(0, col)
            worksheet.write_formula(row, col,"=SUMIFS(forecast_data!$B:$B,"+
                                    "forecast_data!$A:$A,"+product_cell+
                                    ",forecast_data!$D:$D,"
                                    +cell+')')
            col += 1
        row += 1


def create_workbook():
    workbook = xlsxwriter.Workbook(destination_file.get())
    worksheet = workbook.add_worksheet()
    worksheet2 = workbook.add_worksheet("forecast_data")
    data = get_data()
    insert_week_nums(worksheet)
    insert_products(product_list(), worksheet)
    insert_forecast(worksheet2, data)
    insert_formula(worksheet)
    workbook.close()
    messagebox.showinfo("Message", "Upload file created")

def create_file():
    create_workbook()


def close_window():
    mainframe.destroy()
    root.destroy()


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
ttk.Label(lf, text="Forecast file").grid(column=1, row=1, sticky=W, padx=5, pady=5)
ttk.Label(lf, text="Output file name").grid(column=1, row=2, sticky=W, padx=5, pady=5)


ttk.Button(lf, text="Browse", command=get_file).grid(column=3, row=1, sticky=(W, E))
ttk.Button(lf, text="Save File", command=save_as).grid(column=3, row=2, sticky=(W, E))
ttk.Button(lf2, text="Start",command=create_file).grid(column=1, row=4, sticky=(W,E))
ttk.Button(lf2, text="Cancel", command=close_window).grid(column=2, row=4, sticky=(W, E))

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
for child in lf.winfo_children(): child.grid_configure(padx=5, pady=5)
for child in lf2.winfo_children(): child.grid_configure( padx=5, pady=5)


mainframe.pack()
source_file_entry.focus()


root.mainloop()
