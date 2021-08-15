import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Calorie-Calculator')


def get_female_data():
    """
    get all data filled in by user
    """
    while True:
        print("Please user numbers only, no words\n")

        data_info = input("Please enter your height in cm ")
        print(f"Your height is  {data_info}cm\n")

        data_info = input("Please enter your weight in lb ")
        print(f"Your weight is  {data_info}lb\n")

        data_info = input("Please enter your Age ")
        print(f"Your Age is  {data_info}\n")

        female_data = data_info.split(",")

        if numbers_to_int(female_data):
            print("Data is valid")
            print(f"{data_info}")
            break
    
    return female_data


def numbers_to_int(values):
    """
    create all inputs from users into intergers
    """
    try:
        [int(values) for values in values]
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    
    return True


data = get_female_data()