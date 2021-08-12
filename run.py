# pip install py_edamam from https://www.youtube.com/watch?v=OWxvX4m_h7c
from py_edamam import PyEdamam
from Keys import edamam_id, edamam_key

e = PyEdamam(nutrition_appid=edamam_id), nutrition_appkey=edamam_key)

def bmr_calculation():
    #get Input
    weightInLbs - int(input("Please enter your weight in lbs: "))
    heightInInches = int(input("Please enter your height in inces: "))