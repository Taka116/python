'''
Restaurant Recommendation System
Package author : Shin Mitsuno (97171124-8)
'''
import sys

from WasedaProject.User import User
import csv

#contains the csv file of entire list of restaurants
full_rest_csv = ""
user_pref_csv = ""
res_csv = None

user_pref = []
class RestaurantSeeker(User):
    #initialize restuarant seeker with restaurant csv and csv with user preferences

    def __init__(self, userlocation, usercuisine, userprice, full_rest_csv):
        self.full_res_csv = full_rest_csv
        User.__init__(self, userlocation, usercuisine, userprice)

    def read(self):
        global full_rest_csv
        global res_csv
        try:
            res_csv = open(self.full_res_csv, "r",encoding="utf-8-sig")
            full_rest_csv = csv.reader(res_csv)
        except IOError as e:
        # logging.exception(e)
            print(e.errno)

#Area compare
    def filter(self):
        #filter the full restaurant csv with user preferences
        result = []
        # row contains a row of each restaurant, but first row is the header
        # row[0]= name row[1] =location row[2] = foodtype row[3] =price
        for row in full_rest_csv:
            #Row location matches user preferences location
            if(self.getLocation() == str(row[1]).lower().strip()):
                #if type of food matches
                if(self.getCuisine()== str(row[2]).lower().strip()):
                    result += row
        #restart iterator for restaurant  csv file
        res_csv.seek(0)
        #if less than 3 results add more with related location
        if(len(result) == 0 or int(len(result)/4) < 3):
            for row in full_rest_csv:
                if((self.getLocation() == str(row[1]).lower().strip()) and self.getCuisine()== str(row[2]).lower().strip() ):
                    break
                if (self.getLocation() == str(row[1]).lower().strip()):
                    result += row
                #if results has 3 suggestions finish
                if(int(len(result)/4) == 3):
                    break

            print("All choices may not be the exact food you're looking for, but how about these options? ")
        return result

# Method takes in an list and converts that list into CSV format
def convertToCSV(rec_list):
    #Handle exception
    try:
        pass
        result_csv = open("user_suggestions.csv", 'w')
        #No results returned for suggestion
        if(len(rec_list) == 0):
            print("\nNo results found. Please search again with different preferences")
            sys.exit()
        #if more than 3, top 3
        for i in range(3):
            w = "{},{},{},{}\n".format(rec_list[0],rec_list[1],rec_list[2],rec_list[3])
            result_csv.write(w)
            del rec_list[0:4]
        result_csv.close()
    except IOError as e:
        #logging.exception(e)
        print(e.errno)
    pass

