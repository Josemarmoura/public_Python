# FlightATC by Josemar Moura, on 2023-Fev-23
import os; os.system('cls')
import time
luggage = u"\U0001F9F3" # icon
airplane2 = u'\U0001F6E7'

print('The Control Tower requests some information.')
#print('Are you ready? Answer: [Y] or [N]\n')
#question1 = input()
question1 = input('Are you ready? Answer: [Y] or [N]\n')
os.system('cls')
if question1 == 'Y' or question1 == 'y':
    #print('Yes') #delete this line
##
    print(chr(9992)+'   Flight B12 has taken off [Y] or [N]?')
    b12 = input()
    if b12 == 'Y' or b12 == 'y':
        os.system('cls')
        print("We need to check the temperature.")
        temp = int( input("How many degree celsius are?") )
        #temp = int(temp_in)
        if temp >= -55 and temp <= -35:
            os.system('cls')
            print("It is a bad weather"+chr(10071))
            print("We need to redirect"+chr(10071))
            time.sleep(3)
        elif temp < -55:
            print(chr(9924)) # 
            print("Oh my god! It's freezing here. I am dying... Helpe me.")
            time.sleep(3)
        else:
            os.system('cls')
            print(f"Taxi the {airplane2}  to Gate G12 and prepare to get off the airplaine.")
            print("")
            rtpdr = input("Do you have a RT-PDR covid test?")
            if rtpdr == 'Y' or rtpdr == 'y':
                print(f"OK. You can go pick up your luggage {luggage}. Bye.")
                time.sleep(3)
            elif rtpdr == 'N' or rtpdr == 'n':
                print("You need to do a RT-PDR test.")
                print("Go to the RT-PDR area.")
                time.sleep(3)
            else:
                print("I did not understand. Bye")
                time.sleep(2)

    elif b12 == 'N' or b12 == 'n':
        print("Don't permit to flight A12 to land.")
        print("Re-start the program.")
        time.sleep(3)
##
elif question1 == 'N' or question1 == 'n':
    print(chr(9785)+"  I am sorry. See you later. Bye.")
    time.sleep(3)
else:
    print(chr(9940))
    print("You did't write a valid answer!")
    print("Re-start the program.")
    time.sleep(3)

