# Starting file for LAB 7
# Include your course number, student first and last name, and date in the comment header

# Samantha Browning
# Course 72473
# November 14 2026

# Part ONE
# Modify program to store input / output data for each calculation into CSV file
# Enhance program to create a simple two-dimensional list
# Save the distance, gallons, and calculated MPG in each row of the list in a CSV file
# Name file trips.CSV BUT don't save until user is done inputting values

# Part TWO
# modify write_trips() to write the trip after each input
# read_trips()
# list_trips()

import csv

# create filename for .csv file
filename ="trips.csv"

def write_trips(trip):
    print(trip)
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(trip)

def read_trips():
    trips = []
    with open(filename, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            trips.append(row)
    return trips

def list_trips(trips):
    print("Distance\tGallons\t\tMPG")
    # i is our counter, starting at 0
    for i in range(0, len(trips)):
        trip = trips[i]
        print(str(trip[0]) + "\t\t" + str(trip[1]) + "\t\t" + str(trip[2]))

def get_miles_driven():
    while (miles_driven := float(input("Enter miles driven:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")       
    return miles_driven
          
def get_gallons_used():
    while (gallons_used := float(input("Enter gallons of gas:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")
    return gallons_used
        
def main():
    # display a welcome message
    print("The Miles Per Gallon program")
    print()

    trips = read_trips()
    list_trips(trips)
        
    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
                                 
        mpg = round((miles_driven / gallons_used), 2)
        print(f"Miles Per Gallon:\t{mpg}")
        print()

        # create list for the 3 values of this calculation
        trip = []
        trip.append(miles_driven)
        trip.append(gallons_used)
        trip.append(mpg)
        # now append this entire row to trips list
        trips.append(trip)
        # write this trips row before accepting more data
        write_trips(trip)

        list_trips(trips)
        
        more = input("More entries? (y or n): ")

    print("Bye!")

if __name__ == "__main__":
    main()
