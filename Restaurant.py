import webbrowser
import time

class Restaurant():
    def __init__(self, name, location, food_type, avg_price):
        self.name = name
        self.location = location
        self.food_type = food_type
        self.avg_price = avg_price

    def __str__(self):
        return self.name + " | " + self.location + " | " + self.food_type + " | " + "¥"+self.avg_price

    def arrangement(self):
        message = "Dear Customer \n" + "Your reservation at " + self.name + " was successfully arranged. \n" + "We hope you enjoy your time there.\n" + "Thank you for using our service."
        wfile = open("confirmation.txt", "w")
        wfile.write(message)
        wfile.close()


class Reservation():
    def __init__(self, restaurants):
        self.restaurants = restaurants
        self.num_of_res = len(restaurants)

    def sort(self):
        print("Which restaurant do you want to go? \n")
        print("   Name | Location | Foodtype | Price   ")
        letters = ["A", "B", "C"]
        for restaurant in self.restaurants:
            index = self.restaurants.index(restaurant)
            print(letters[index] + ". " + restaurant.__str__())

        print("\nType Either ", end="")
        for i in range(self.num_of_res):
            if i == self.num_of_res-1:
                print(letters[i])
            else:
                print(letters[i] + " or ", end="")

        user_input = input("Please Enter: ").capitalize()

        while user_input not in (letters[0:self.num_of_res]):
            print("You typed something wrong!")
            user_input = input("Please Enter: ").capitalize()
        print("\nyour input was: ", user_input)

        reservation_restaurant = self.restaurants[letters.index(user_input)]
        #open browser of selected restaurant str(reservation_restaurant).split(" ")[0]
        time.sleep(2)
        search = str(reservation_restaurant).split("|")[0]+" "+str(reservation_restaurant).split("|")[1]
        webbrowser.open_new_tab("https://www.google.com.tr/search?q="+ search)
        time.sleep(3)

        confirmation = input("\nAre you sure you want to reserve restaurant " + user_input + "? y/n: ")
        while confirmation not in ("y", "n"):
            print("You typed something wrong!")
            confirmation = input("\nAre you sure you want to reserve restaurant " + user_input + "? y/n: ")
        if confirmation == "y":
            return reservation_restaurant
        else:
            return "Thank you for using our service."

