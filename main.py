import csv
import pandas as pd

CSV_FILE = "contact_data.csv"

def display_data():
    print("--------------------")
    print(pd.read_csv(CSV_FILE))
    print("--------------------")

def add_data():
    data_id = input("Enter id:\n")
    name = input("Enter name:\n")
    email = input("Enter email:\n")
    gender = input("Enter gender(male/female):\n")
    dob = input("Enter dob(dd-mm-yy):\n")
    address = input("Enter address:\n")
    phone = input("Enter phone:\n")
    list = [data_id, name, email, gender, dob, address, phone]
    with open(CSV_FILE, 'a') as f_obj:
        csv.writer(f_obj).writerow(list)
        f_obj.close()

def delete_row(row_id):
    df = pd.read_csv(CSV_FILE, index_col='id').drop(row_id)
    df.to_csv(CSV_FILE, index=True)

choice = -1
while(choice!=0):
    choice = int(input("\n---Choose operation to perform---\n1. Display Data\n2. Add Data\n3. Delete Data\n0. Exit\n\nEnter operation number:\n"))
    match choice:
        case 1:
            display_data()
        case 2:
            add_data()
        case 3:
            delete_row(int(input("Enter id to delete:\n")))
        case 0:
            exit()
        case _:
            print("***Incorrect choice entered!***")