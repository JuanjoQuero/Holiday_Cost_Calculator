#First I get user inputs and assign variables to them. 
city_flight = input("Please enter destination city (New York/Los Angeles/Rio de Janeiro/Mexico City) : ")

#I've decided to add this block of code just after the city selection to avoid an invalid selection from user. 
city_list = ['new york', 'los angeles', 'rio de janeiro', 'mexico city']

if city_flight.lower() not in city_list:
    print ("That's not a valid destination.")
    city_flight = input("Please enter destination city (New York/Los Angeles/Rio de Janeiro/Mexico City) : ")

#Function used for input validation, instead of comments to explain it I am going to use a docString,
#following Jonathan LLoyd(reviewer) recommendations.
def input_validation(prompt:int):
    """This function check user input if it values correctly

    Args:
        prompt (str): Prompt to use

    Raises:
        ValueError: Error if input is less than 0 or greater than 30

    Returns:
        int: Valid input value
    """
    while True:
        try:
            user_input: int = int(input(prompt))
            if user_input < 0 or user_input > 30:
                raise ValueError("Invalid input!")
            return user_input
        except ValueError:
            print("Invalid input!")

#Create another 2 variables for number of hotel nights and number of car rental days,
#using the input_validation function to check user input.
num_nights = input_validation("Please enter number of holiday nights in hotel: ")
rental_days = input_validation("Please enter number of days renting a car: ")

#Now I can define functions to calculate different options for your holidays.
#Note that price for hotel stay, flights and car rental has been assigned ramdonly,
#it can be change if required.
def hotel_cost(num_nights: int):
    """This function calculates cost for the hotel nights.

    Args:
        num_nights (int): nights of hotel

    Returns:
        int: price for the stay
    """
    stay_cost = num_nights * 180
    return stay_cost

def plane_cost(city_flight):
    """This function calculates cost for the flight

    Args:
        city_flight (str): name of the city you are flying to

    Returns:
        int: price for your flight
    """
    if city_flight.lower() == "new york":
        flight_cost = 363
        return (flight_cost)
    
    elif city_flight.lower() == "los angeles":
        flight_cost = 379
        return (flight_cost)
    
    elif city_flight.lower() == "rio de janeiro":
        flight_cost = 772
        return (flight_cost)
    
    elif city_flight.lower() == "mexico city":
        flight_cost = 679
        return (flight_cost)

def car_rental(rental_days: int):
    """This function calculate the price for renting a car

    Args:
        rental_days (int): days renting a car

    Returns:
        int: price for your car rental
    """
    rental_cost = rental_days * 69
    return (rental_cost)

def holiday_cost(hotel_cost: int, plane_cost: int, car_rental: int):
    """This function will call functions: hotel_cost, plane_cost and car_rental
    to calculate the total cost for your holidays.

    Args:
        hotel_cost (int): cost for hotel
        plane_cost (int): cost for flight
        car_rental (int): cost for car rental

    Returns:
        int: total price for your holidays
    """
    total_cost: int = hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)
    return total_cost

#We can print the results calling the differents functions.
print (f"Hotel cost : {(hotel_cost(num_nights))}")
print (f"Plane cost : {(plane_cost(city_flight))}")
print (f"Car rental cost : {(car_rental(rental_days))}")
print (f"Total price of your holidays : {holiday_cost(hotel_cost, plane_cost, car_rental)}")
