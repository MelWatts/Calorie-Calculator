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

        data_weight_str = input("Please enter your weight in kg  ")
        print(f"Your weight is  {data_weight_str}kg\n")

        data_height_str = input("Please enter your height in cm ")
        print(f"Your height is  {data_height_str}cm\n")

        data_age_str = input("Please enter your Age ")
        print(f"Your Age is  {data_age_str}\n")

        female_data = data_weight_str, data_height_str, data_age_str     

        if validate_entry(female_data):
            print("Data is Valid")
            print(female_data)
            break

    return female_data


def validate_entry(values):
    """
    create all inputs from users into intergers
    """
    try:
        [int(value) for value in values]
        if len(values) != 3:
            raise ValueError(
                f"Exactly 3 values required, you provided {len(values)}")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def update_worksheet(data):
    """
    Receives a list of integers to be inserted into a worksheet
    Update the relevant worksheet with the data provided
    """
    print("Updating worksheet...\n")
    worksheet_to_update = SHEET.worksheet("female")
    worksheet_to_update.append_row(data)
    print("Calculating your BMR...\n")


def top():

    """
    Run all functions
    """
    data = get_female_data()
    female_data = [int(num) for num in data]
    update_worksheet(female_data)


print("Welcome ladies to the calorie calculator for woman")
top()


def test_all_rows():
    calorie_calculator = SHEET.worksheet('female').get_all_values()[1:]
    print(calorie_calculator)

    i = 1
    for row in calorie_calculator:
        i += 1
        bmr = 448 + (10 * int(row[0])) + (3 * int(row[1])) - 5 * int(row[2])
        print(bmr)
        SHEET.worksheet('female').update_cell(i, 4, bmr)


def test_single_row():
    calorie_calculator = SHEET.worksheet('female').get_all_values()
    row = calorie_calculator[-1:][0]
    bmr = 448 + (10 * int(row[0])) + (3 * int(row[1])) - 5 * int(row[2])
    print(bmr)
    SHEET.worksheet('female').update_cell(len(calorie_calculator), 4, bmr)


test_single_row()
