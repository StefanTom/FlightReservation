#This program makes reservations for flights

#Header

def reserve_seat(flight):
    
    print("-----------------------------------------")
    print("\nMake a reservation: ")
    print("\n-----------------------------------------")
    
    row_choice = 0
    column_choice = 0
    
    reserve_name = input("Please enter first name: ")
    reserve_lastname = input("Please enter last name: ")
    class_name = "INFOTC1040"
    
    name_length = int(len(reserve_name))
    class_name_length = int(len(class_name))
    lastname_length = int(len(reserve_lastname))


    name_range = name_length + class_name_length

    list1 = []
    
    count=0
    for name_char in range(0,name_range-1):
        list1.append(reserve_name[count])
        list1.append(class_name[count])
        count+=1
        if (count == name_length-1):
            break
    flight_tick = ''.join(list1) + '1040'
            
    call_flightmap(flight)
    
    while True:
        while True:
            row_choice = int(input("What row would you like? "))

            if row_choice > 10 or row_choice < 1:
                print("Please enter a row in between 1 and 10.")
            else:
                break
            
        while True:
            column_choice = int(input("What column would you like? "))
            
            if column_choice > 5 or column_choice < 1:
                print("Please enter a column in between 1 and 5.")
            else:
                break

        if flight[row_choice-1][column_choice-1] == 'X':
            print("Seat taken. Please choose a different seat.")
            continue
        else:
            flight[row_choice-1][column_choice-1] = 'X'
            call_flightmap(flight)
            print("Your flight ticket is: ", flight_tick)
            break

            

def call_flightmap(flight):

    for lines in flight:
        print(lines)
    return


def initial_map():
    
    flight = [['0']*5 for row in range(10)]

    file_reservation = open("reservations.txt","r")

    for line in file_reservation:
        data = line.split(",")
        row = int(data[1])
        column = int(data[2])
        flight[row][column] = "X"

    file_reservation.close()
    
    return flight

def admin_login(flight):
    print("-----------------------------------------")
    print("\nAdmin Login\n")
    print("-----------------------------------------")

    file_open = open("passcodes.txt","r")

    user_list=[]

    for line in file_open:
        user_list.append(line.rstrip('\n'))
    hot_input = True
    while hot_input:
        login_user = input("\nPlease enter username: ")
        login_pass = input("Please enter password: ")
        if login_user != user_list[0] or login_pass != user_list[1]:
            print("---------------------------------------------------------")
            print("\nIncorrect Login. Please enter again.\n")
            print("---------------------------------------------------------")
            continue
        if login_user == user_list[0] and login_pass == user_list[1]:
            print("\n-------------------------------------------------------")
            print("Welcome to admin access of InfoTC Airlines Terminal")
            print("---------------------------------------------------------")
            print("\nLoading flight seating chart...")
            call_flightmap(flight)
            print("\nTotal Flight Sales: ")

            cost_matrix = [[500, 200, 500, 200, 500] for row in range(10)]

            total_sales = 0

            for row in range(len(flight)):
                for seat in range(len(flight[row])):
                    if flight[row][seat] == 'X':
                        total_sales += cost_matrix[row][seat]

            print("Total Sales: ", total_sales)
            

            print("\n---------------------------------------------------------")
            file_open.close()
            print("You are now logged out.")
            print("---------------------------------------------------------")
            break
    

def main():
    print("\n---------------------------------------")
    print("Welcome to 1040 Flight Reservation System")
    print("-----------------------------------------")
    print("\n1. Admin Log-In")
    print("2. Reserve a seat")
    print("3. Exit")
    print("\n---------------------------------------")
    bad_input = True
    while bad_input:
        try:

            flight = initial_map()
            
            option_select = input("\nPlease select option 1, 2, or 3: ")

            if option_select == "1":
                admin_login(flight)
            elif option_select == "2":
                reserve_seat(flight)
            elif option_select == "3":
                print("\n---------------------------------------------------------")
                print("Thank you for flying with INFOTC airlines\nExiting...")
                print("---------------------------------------------------------")
                break
            elif option_select > "3":
                print("Number is too large. Please select 1, 2, or 3.")
                continue
            elif option_select < "1":
                print("Number is too small. Please select 1, 2, or 3.")
                continue
        except Exception as err:
            print("The following error occured: ", err, "\nPlease enter input again")
main()
