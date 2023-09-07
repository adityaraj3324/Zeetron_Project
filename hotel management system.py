import pandas as pd
import datetime

# Constants
EXCEL_FILE = "hotel_data.xlsx"
RATE_PER_MINUTE = 10

# Function to initialize the Excel file if it doesn't exist
def initialize_excel():
    try:
        df = pd.read_excel(EXCEL_FILE)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Serial", "Name", "Mobile No.", "Email", "Room No.", "Entry Time", "Exit Time", "Total Time (min)", "Amount (INR)"])
        df.to_excel(EXCEL_FILE, index=False)

# Function to check in a guest
def check_in():
    name = input("Enter guest's name: ")
    mobile_no = input("Enter mobile number: ")
    email = input("Enter email address: ")
    room_no = input("Enter room number: ")
    entry_time = datetime.datetime.now()
    
    data = {
        "Serial": len(df) + 1,
        "Name": name,
        "Mobile No.": mobile_no,
        "Email": email,
        "Room No.": room_no,
        "Entry Time": entry_time
    }
    
    df.loc[len(df)] = data
    df.to_excel(EXCEL_FILE, index=False)
    print("Guest checked in successfully!")

# Function to calculate and display the amount to be paid
def calculate_amount(entry_time):
    exit_time = datetime.datetime.now()
    total_time = (exit_time - entry_time).total_seconds() / 60  # in minutes
    amount = total_time * RATE_PER_MINUTE
    return total_time, amount

# Function to check out a guest
def check_out():
    room_no = input("Enter room number for check-out: ")
    guest_data = df[df["Room No."] == room_no]
    
    if guest_data.empty:
        print("No guest found with the specified room number.")
        return
    
    entry_time = guest_data.iloc[0]["Entry Time"]
    total_time, amount = calculate_amount(entry_time)
    
    df.loc[df["Room No."] == room_no, ["Exit Time", "Total Time (min)", "Amount (INR)"]] = [datetime.datetime.now(), total_time, amount]
    df.to_excel(EXCEL_FILE, index=False)
    
    print(f"Guest Name: {guest_data.iloc[0]['Name']}")
    print(f"Mobile No.: {guest_data.iloc[0]['Mobile No.']}")
    print(f"Time Spent in Hotel: {total_time:.2f} minutes")
    print(f"Total Amount to be Paid: {amount:.2f} INR")
    print("Guest checked out successfully!")

# Initialize the Excel file if it doesn't exist
initialize_excel()

# Load the data from the Excel file
df = pd.read_excel(EXCEL_FILE)

while True:
    print("\nHotel Management System")
    print("1. Check-in")
    print("2. Check-out")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == "1":
        check_in()
    elif choice == "2":
        check_out()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")
