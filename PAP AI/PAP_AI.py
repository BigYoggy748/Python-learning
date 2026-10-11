import time
from AI_calculator import *

username = []
user = []
def pap_ai():
    print("Hello,")
    time.sleep(1)
    print("I am pap ai your assistant")
    time.sleep(1)

def user_name():
    name = input("What is your name: " )
    username.append(name)
    print("Loading....")
    time.sleep(1)
    greeting()

def main_menu():
    print("                 THE MAIN MENU")
    print("=" * 45)
 
    print("     1. Jollof rice  = #1500")
    print("     2. Fried rice   = #1500")
    print("     3. Coconut rice = #1500")
    print("     4. Oil beans    = #1500")
    print("     5. Rice & stew  = #1500")
    print("     6. Pancake      = #1500")
    print("     7. spagetti     = #1500")
    print("     8. PAP          = #1500")

    print("=" * 45)
    print("Would you like to see the menu?")
    main_menu = input(":")
    user.append(main_menu)

def greeting():
    for i in username:
        print(f"Hello {i}, would you like to see the menu? ").lower().strip()
        user_input = input(":")
        user.append(user_input)

def allocate_user_input():
    for u in user:
        menu1 = u.find("rice")
        menu2 = u.find("oil beans")
        menu3 = u.find("want")
        menu4 = u.find("what")
        menu5 = u.find("rice")
        menu6 = u.find("pap")
        menu7 = u.find("coke")
        menu8 = u.find("milk")
        menu9 = u.find("yes")
        calc = u.find("solve")
        help = u.find("help")


        if menu9 != -1:
            main_menu()

        elif menu1 != -1:
            print("That will be #1500 \n")
            time.sleep(2)
            print("we are preparing your meal \n")
            time.sleep(2)
            print("Yay, your meal is ready.just drop the amount \n")
            time.sleep(2)
            input(":")
            greeting()
        
        elif  menu2 != -1:
            print("That will be #1500 \n")
            time.sleep(2)
            print("we are preparing your meal \n")
            time.sleep(2)
            print("Yay, your meal is ready.just drop the amount \n")
            time.sleep(2)
            input(":")
            greeting()

        elif menu3 != -1:
            print("That will be #1500 \n")
            time.sleep(2)
            print("we are preparing your meal \n")
            time.sleep(2)
            print("Yay, your meal is ready.just drop the amount \n")
            time.sleep(2)
            input(":")
            greeting()

        elif menu4 != -1:
            print("That will be #1500 \n")
            time.sleep(2)
            print("we are preparing your meal \n")
            time.sleep(2)
            print("Yay, your meal is ready.just drop the amount \n")
            time.sleep(2)
            input(":")
            greeting()

        elif menu5 != -1:
            print("That will be #1500 \n")
            time.sleep(2)
            print("we are preparing your meal \n")
            time.sleep(2)
            print("Yay, your meal is ready.just drop the amount \n")
            time.sleep(2)
            input(":")
            greeting()

        elif menu6 != -1:
            print("That will be #1500 \n")
            time.sleep(2)
            print("we are preparing your meal \n")
            time.sleep(2)
            print("Yay, your meal is ready.just drop the amount \n")
            time.sleep(2)
            input(":")
            greeting()

        elif menu7 != -1:
            print("That will be #1500 \n")
            time.sleep(2)
            print("we are preparing your meal \n")
            time.sleep(2)
            print("Yay, your meal is ready.just drop the amount \n")
            time.sleep(2)
            input(":")
            greeting()

        elif menu8 != -1:
            print("That will be #1500 \n")
            time.sleep(2)
            print("we are preparing your meal \n")
            time.sleep(2)
            print("Yay, your meal is ready.just drop the amount \n")
            time.sleep(2)
            input(":")
            greeting()

        elif menu9 != -1:
            print("That will be #1500 \n")
            time.sleep(2)
            print("we are preparing your meal \n")
            time.sleep(2)
            print("Yay, your meal is ready.just drop the amount \n")
            time.sleep(2)
            input(":")
            greeting()

        else:
            time.sleep(3)
            print("sorry we dont have such. \n")
            time.sleep(2)
            print("Your session is being terminated \n")
            time.sleep(2)
            print('Terminating...........')
            time.sleep(2)
            print("TERMINATED \n")
            time.sleep(3)
            print("You PAP 😠")
            break



def main():
    pap_ai()
    user_name()
    allocate_user_input()

main()