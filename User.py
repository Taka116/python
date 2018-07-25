import csv
class User:
    def __init__(self, userlocation, usercuisine, userprice):
        self.location = userlocation
        self.cuisine = usercuisine
        self.price = userprice
        self.listpreference = [userlocation, usercuisine, userprice]

    def writecsv(self):
        with open("confirmation.txt", "a") as file:
            file.write('\n')
            file.write("---------------This is your User Profile---------------  \n")
            file.write("These are your current preferences\n")
            file.write("Location preference : {}\nFood Type preference : {}\nPrice preference : {}\n".format(self.location,self.cuisine,self.price))
            file.close()

    def __str__(self):
        return "User preferences are {0}, {1}, and {2}.".format(self.location, self.cuisine, self.price)

    def getLocation(self):
        return str(self.location)

    def getPrice(self):
        return str(self.price)

    def getCuisine(self):
        return str(self.cuisine) 

