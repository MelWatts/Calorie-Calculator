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

        data_weight_str = input("Please enter your weight in kg  \n")
        print(f"Your weight is  {data_weight_str}kg\n")

        data_height_str = input("Please enter your height in cm \n")
        print(f"Your height is  {data_height_str}cm\n")

        data_age_str = input("Please enter your Age \n")
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
    print("The number of calories you need just\
        for your body to function is called your\
        basal metabolic rate, or BMR.\
        If you know your BMR,you can better determine\
        your caloric needs for healthy weight loss.\
        Calculating your BMR...\n")


def top():

    """
    Run all functions
    """
    data = get_female_data()
    female_data = [int(num) for num in data]
    update_worksheet(female_data)


print("Welcome ladies to the calorie calculator for woman")
top()

"""
Formula to work out BMR for a woman \
https://www.garnethealth.org/news/basal-metabolic-rate-calculator
"""


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
    """
    Returns the users BMR using data entered
    """
    calorie_calculator = SHEET.worksheet('female').get_all_values()
    row = calorie_calculator[-1:][0]
    bmr = 448 + (10 * int(row[0])) + (3 * int(row[1])) - (5 * int(row[2]))
    print(bmr)
    SHEET.worksheet('female').update_cell(len(calorie_calculator), 4, bmr)


def test_all_deficit():
    calorie_calculator = SHEET.worksheet('female').get_all_values()[1:]
    print(calorie_calculator)

    i = 1
    for row in calorie_calculator:
        i += 1
        deficit = 448 + (10 * int(row[0])) + (3 * int(row[1])) - (5 * int(row[2])) + 200
        print(deficit)
        SHEET.worksheet('female').update_cell(i, 5, deficit)


def test_calorie_deficit():
    """
    Returns the users Calorie Deficit using data entered +
    200 extra calories for activities.
    """
    calorie_calculator = SHEET.worksheet('female').get_all_values()
    row = calorie_calculator[-1:][0]
    deficit = 448 + (10 * int(row[0])) + (3 * int(row[1])) - (5 * int(row[2])) + 200
    print(deficit)
    SHEET.worksheet('female').update_cell(len(calorie_calculator), 5, deficit)


def test_all_surplus():
    calorie_calculator = SHEET.worksheet('female').get_all_values()[1:]
    print(calorie_calculator)

    i = 1
    for row in calorie_calculator:
        i += 1
        surplus = 448 + (10 * int(row[0])) + (3 * int(row[1])) - (5 * int(row[2])) + 500
        print(surplus)
        SHEET.worksheet('female').update_cell(i, 6, surplus)


def test_calorie_surplus():
    """
    Returns the users Calorie Deficit using data entered
    + 500 extra calories for extra activities.
    """
    calorie_calculator = SHEET.worksheet('female').get_all_values()
    row = calorie_calculator[-1:][0]
    surplus = 448 + (10 * int(row[0])) + (3 * int(row[1])) - (5 * int(row[2])) + 500
    print(surplus)
    SHEET.worksheet('female').update_cell(len(calorie_calculator), 6, surplus)


test_single_row()

print("Calculating your Calorie deficit...\n")
test_calorie_deficit()

print("Calculating your Calorie surplus...\n")
test_calorie_surplus()
