#By Josemar Moura. Feb2023.
 
import os; os.system('cls') # comment this line after finished.
import random as rd
import time 
def light():
    lighttraffic_input = input('What is the light color: (R)ed, (O)range or (G)reen? ')
    light_color = str.capitalize (lighttraffic_input[0])
    return(light_color)
#    print(light_color) # comment this line after finished.

def people():
    random_num_total_people = rd.randint(0,3) 
    return(random_num_total_people)

def timer(t):

    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(f'  Whait for {timer} seconds, before to go.', end="\r")
        time.sleep(1)
        t -= 1
t=5  
    
xcolor = light()
people_on_street = people()
def stop_go():
    if xcolor == "R":
        print("Stop")
    elif xcolor == "O":
        print("Slow down and Be Careful.")

    elif xcolor == "G" and people_on_street == 0:
        print("Go.")
    elif xcolor == "G" and people_on_street != 0:
        print(f"It's Green, but you need to wait for the {people_on_street} people to pass.")
        #print(f"  gWhait for {timer(t)} seconds before to go.")
        print(f'{timer(t)} ... Now you can go! Bye, bye!        ')

    else:
        print("Be careful! I can't see the light traffic color!")

stop_go()
