from WasedaProject.RestaurantSeeker import RestaurantSeeker, convertToCSV
from WasedaProject.Restaurant import Restaurant, Reservation
import subprocess
import time


try:
    location = str(input("Please enter a location (shibuya,akihabara,shinjyuku) : "))
    food_type = str(input("Please enter your preferred food(sushi,yakiniku,seafood,izakaya,tonkatsu,italian,burger) : "))
    price = str(input("Please enter preferred price : "))
    if (len(location) == 0) or (len(food_type) ==0 ) or (len(price)==0) :
        raise ValueError('\nOne of your inputs seems to be empty! Please try again. ')
except ValueError as e:
    print(e)

rest_seeker = RestaurantSeeker(location,food_type,price,"RestaurantRec.csv")
rest_seeker.read()
convertToCSV(rest_seeker.filter())

listOfRestaurants = []
try:
    with open("user_suggestions.csv", newline='') as f:
        reader = f.readlines()
        for row in reader:
            r = row.strip("\n").split(",")
            restaurant = Restaurant(r[0], r[1], r[2], r[3])
            listOfRestaurants.append(restaurant)
except IOError as e:
    print(e)

r = Reservation(listOfRestaurants)
result = r.sort()
if isinstance(result, Restaurant):
    result.arrangement()
    rest_seeker.writecsv()
    print("\nThank you for using our service. Please check the text file.")


else:
    print(result)

#opens the textfile with confirmation
time.sleep(2)
subprocess.call(['open', '-a', 'TextEdit', "confirmation.txt"])
#p = subprocess.Popen(["notepad.exe", "confirmation.txt"])
