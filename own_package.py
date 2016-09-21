import random

month = 0
destination = 1
price = 2
package_details = 3
number_of_passengers = 4
cancellation_fee = 5

package = [
#MONTH       #DESTINATION   #PRICE        #PACKAGE_DETAILS    #NUMBER_OF_PASSENGERS    #CANCELLATION_FEE
["JUNE",       "Hawaii",      1000,   "Hotel & Flight",             4,                   200],
["JULY",       "Chicago",     398,    "Flight",                     1,                   65],
["AUGUST",     "Miami",       600,    "Hotel & Flight",             2,                   120],
["SEPTEMBER",  "New York",    425,    "Hotel",                      1,                   89],
["OCTOBER",    "Seattle",     150,    "Flight",                     1,                   73],
["NOVEMBER",   "Portland",    560,    "Hotel & Flight",             2,                   80],
["DECEMBER",   "San Diego",   325,    "Flight",                     2,                   100],
]

def menu_options():
    print ('1) Print a RANDOM DESTINATION')
    print ('2) Print the 3 cheapest package deals; lowest -> highest')
    print ('3) Print packages with ONLY Flights')
    print ('4) Print packages within your price budget')
    print ('6) Print the total price of ALL packages')
    print ('0) EXIT PROGRAM!')
    
def welcome_message():
    print ('-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')
    print ('                   WELCOME TO THE PACKAGE SELECTOR                             ')
    print ('\n-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')
if __name__ == "__main__":
     print ('\n')
     welcome_message()
     choice = ''
     while (choice != '0'):
         menu_options()
         choice = str(input('Select from the options above: '))
         print ('\n-------------------------------------------------------------------')
         print ('\n')
         
         if (choice == '1'):
             random_package = ['Hawaii','Chicago','Miami','New York','Seattle','Portland','San Diego']
             print (random.choice(random_package))
             print ('\n')
             print ('*******************************************************************\n')
         
         elif (choice == '2'):
             print (package[4][destination],"   $",package[4][price])
             print (package[6][destination]," $",package[6][price])
             print (package[1][destination],"   $",package[1][price])
             print ('\n')
             print ('*******************************************************************\n')
             
         elif (choice == '3'):
             print (package[1][destination])
             print (package[4][destination])
             print (package[6][destination])
             print ('\n')
             print ('*******************************************************************\n')
             
         elif (choice == '4'):
             package_min = int(input('Enter the LOWEST amount you are willing to pay: '))
             package_max = int(input('Enter the HIGHEST amount you are willing to pay: '))
             for i in range(len(package)):
                 if package[i][2] >= package_min and package[i][2] <= package_max:
                     print package[i][1], package[i][2]

         elif (choice == '6'):
             print ('TOTAL FOR ALL PACKAGES:\n')
             print ("$", package[0][price] + package[1][price] + package[2][price] + package[3][price] +
                    package[4][price] + package[5][price] + package[6][price])
             print ('\n')
             print ('*******************************************************************\n')
             
         elif (choice == '0'):
            print ('END OF PROGRAM.......END OF PROGRAM')
            print ('END OF PROGRAM.......END OF PROGRAM')
            print ('END OF PROGRAM.......END OF PROGRAM')
            print ('END OF PROGRAM.......END OF PROGRAM')
            
         else:
            print ('INVALID INPUT; DOUBLE-CHECK YOUR SELECTION')
            print ('\n')
            print ('*******************************************************************\n')
