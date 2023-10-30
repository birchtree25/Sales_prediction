import tkinter
from tkinter import ttk
from tkinter import messagebox
import os
import openpyxl

def enter_data():
    # print("Hi Mom!")
    item_id = item_identifier_entry.get()
    item_weight = item_weight_entry.get()
    item_MRP = item_MRP_entry.get()
    item_fat_content = item_fat_content_combobox.get()
    item_type = item_type_combobox.get()
    item_visiblity_flt = float(item_visiblity_entry.get())/100
    item_visiblity = str(item_visiblity_flt)
    outlet_identifier = outlet_identifier_entry.get()
    outlet_est_yr = outlet_est_yr_entry.get()
    outlet_size = outlet_size_combobox.get()
    outlet_Location_Type = outlet_Location_Type_combobox.get()
    outlet_Type = outlet_Type_combobox.get()
    
    #ERROR MESSAGES
    if item_id and item_weight and item_MRP and item_fat_content and item_type and item_visiblity and outlet_identifier and outlet_est_yr and outlet_Location_Type and outlet_size and outlet_Type:
        print(" Item ID:", item_id , "\n", "Item Weight:", item_weight , "\n" , "Item MRP:" , item_MRP )
        print(" Item Fat Content:", item_fat_content , "\n", "Item Type:", item_type , "\n" , "Item Visiblity:" , item_visiblity ,"\n")
        # print("nope")
        print(" Outlet ID:", outlet_identifier , "\n", "Outlet Est. Year:", outlet_est_yr , "\n" , "Outlet Size:" , outlet_size )
        print(" Outlet Location Type:", outlet_Location_Type , "\n", "Outlet Type:", outlet_Type)


        filepath = "D:\pythonDS\CP\data_entries.xlsx"

        if not os.path.exists(filepath):
            workbook = openpyxl.Workbook()
            sheet = workbook.active 
            heading = ["Item_Identifier", "Item_Weight", "Item_Fat_Content", "Item_Visibility", "Item_Type", "Item_MRP", "Outlet_Identifier", "Outlet_Establishment_Year", "Outlet_Size", "Outlet_Location_Type","Outlet_Type"]
            sheet.append(heading)
            workbook.save(filepath)
        workbook = openpyxl.load_workbook(filepath)
        sheet = workbook.active
        sheet.append([item_id, item_weight, item_fat_content, item_visiblity, item_type, item_MRP, outlet_identifier, outlet_est_yr, outlet_size, outlet_Location_Type, outlet_Type])
        workbook.save(filepath)

    else:
        # print("nope")
        tkinter.messagebox.showwarning(title = "Error", message = "Fill in all the details")

window = tkinter.Tk()
window.title("Data Entry")

frame = tkinter.Frame(window)
frame.pack()


#ITEM INFO FRAME
iteminfolabel = tkinter.LabelFrame(frame,text = "Item Info.")
iteminfolabel.grid(row = 0, column=0, padx =20, pady= 20)


item_identifier_label = tkinter.Label(iteminfolabel, text = "Item ID")
item_identifier_label.grid(row = 0, column=0)
item_weight_label = tkinter.Label(iteminfolabel, text = "Item Weight")
item_weight_label.grid(row=0, column=1)

item_identifier_entry = tkinter.Entry(iteminfolabel)
item_identifier_entry.grid(row=1, column=0)
item_weight_entry = tkinter.Entry(iteminfolabel)
item_weight_entry.grid(row=1, column=1)

item_MRP_lable = tkinter.Label(iteminfolabel, text = "Item MRP")
item_MRP_entry = tkinter.Entry(iteminfolabel)
item_MRP_lable.grid(row=0, column=2)
item_MRP_entry.grid(row =1, column=2)

item_fat_content_lable = tkinter.Label(iteminfolabel, text = "Fat Content")
item_fat_content_combobox = ttk.Combobox(iteminfolabel, values= ["Low_Fat", "Regular"])
item_fat_content_lable.grid(row=2, column=0)
item_fat_content_combobox.grid(row=3, column= 0)

item_type_lable = tkinter.Label(iteminfolabel, text = "Item Type")
item_type_combobox = ttk.Combobox(iteminfolabel, values= ["Fruits and Vegetables", "Snack Foods", "Household", "Frozen Foods", "Dairy", "Canned", "Baking Goods", "Health and Hygiener", "Soft Drinks", "Meat", "Hard Drinks", "Breads", "Starchy Foods", "Breakfast","Seafood", "Others"])
item_type_lable.grid(row=2, column=1)
item_type_combobox.grid(row=3, column= 1)

item_visiblity_label = tkinter.Label(iteminfolabel, text = "Item Visiblity")
item_visiblity_label.grid(row= 2, column= 2)
item_visiblity_entry = tkinter.Entry(iteminfolabel)
item_visiblity_entry.grid(row=3, column=2)

for widget in iteminfolabel.winfo_children():
    widget.grid_configure(padx= 10, pady=5)


#OUTLET INFO FRAME
outletinfolabel = tkinter.LabelFrame(frame,text = "Outlet Info.")
outletinfolabel.grid(row = 1, column=0, padx =20, pady= 20)

iteminfolabel = tkinter.LabelFrame(frame,text = "Item Info.")
iteminfolabel.grid(row = 0, column=0, padx =20, pady= 20)


outlet_identifier_label = tkinter.Label(outletinfolabel, text = "Outlet ID")
outlet_identifier_label.grid(row = 0, column=0)
outlet_est_yr_label = tkinter.Label(outletinfolabel, text = "Est. Year")
outlet_est_yr_label.grid(row=0, column=1)

outlet_identifier_entry = tkinter.Entry(outletinfolabel)
outlet_identifier_entry.grid(row=1, column=0)
outlet_est_yr_entry = tkinter.Entry(outletinfolabel)
outlet_est_yr_entry.grid(row=1, column=1)

outlet_size_lable = tkinter.Label(outletinfolabel, text = "Outlet_Size")
outlet_size_combobox = ttk.Combobox(outletinfolabel, values= ["Small", "Medium", "High"])
outlet_size_lable.grid(row=0, column=2)
outlet_size_combobox.grid(row=1, column= 2)

outlet_Location_Type_lable = tkinter.Label(outletinfolabel, text = "Outlet Location Type")
outlet_Location_Type_combobox = ttk.Combobox(outletinfolabel, values= ["Tier 1", "Tier 2", "Tier 3"])
outlet_Location_Type_lable.grid(row=2, column=0)
outlet_Location_Type_combobox.grid(row=3, column= 0)

outlet_Type_lable = tkinter.Label(outletinfolabel, text = "Outlet Type")
outlet_Type_combobox = ttk.Combobox(outletinfolabel, values= ["Grocery Store", "Supermarket Type1", "Supermarket Type2", "Supermarket Type3"])
outlet_Type_lable.grid(row=2, column=1)
outlet_Type_combobox.grid(row=3, column= 1)

for widget in outletinfolabel.winfo_children():
    widget.grid_configure(padx= 10, pady=5)


#EXCEL ENTRY BUTTON
buttonframe = tkinter.LabelFrame(frame, text = "Excel Input")
buttonframe.grid(row = 2, column=0, padx = 10, pady =10)

button = tkinter.Button(buttonframe, text = "Enter into Excel", command= enter_data)
button.grid(row = 0, column=0, padx = 5)

for widget in buttonframe.winfo_children():
    widget.grid_configure(padx= 10, pady=5)

window.mainloop()