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
    data_str = input("Please enter your height in cm ")
    print(f"Your height is  {data_str}cm")

    data_str = input("Please enter your weight in lb ")
    print(f"Your weight is  {data_str}lb")

    data_str = input("Please enter your Age ")
    print(f"Your Age is  {data_str}")

get_female_data()