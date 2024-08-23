import pandas as pd
from datetime import datetime

def save_complaint():
    # Gather input from the user
    name = input("Enter your name: ")
    contact = input("Enter your contact number: ")
    address = input("Enter your address: ")
    complaint = input("Enter your complaint details: ")
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


    # Data to be saved
    data = {
        'Timestamp': [timestamp],
        'Name': [name],
        'Contact': [contact],
        'Address': [address],
        'Complaint': [complaint]
    }

    # Load existing data or create a new dataframe
    try:
        df = pd.read_excel("complaints.xlsx")
    except FileNotFoundError:
        df = pd.DataFrame(columns=['Timestamp', 'Name', 'Contact', 'Address', 'Complaint'])

    # Append the new complaint to the dataframe
    df = df._append(pd.DataFrame(data), ignore_index=True)

    # Save the updated dataframe back to the Excel file
    df.to_excel("complaints.xlsx", index=False)

    print("Complaint submitted successfully!")

# Main function
if __name__ == "__main__":
    print("Welcome to the Complaint Submission System")
    save_complaint()

