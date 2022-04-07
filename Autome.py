from plyer import notification
import os
import psutil
import ctypes
import time
def Alert():
    notification.notify(
    title = 'Alert',
    message = f'Your Battery is {battery_charge}%',
    app_icon = r'./app_icon.ico',
    # timeout = 10,
    app_name = 'Autome',
    )    
def Hibernate():
    os.system("shutdown /h")    
def Logoff():
    os.system("shutdown /l")    
def Lock():
    os.system("rundll32.exe user32.dll, LockWorkStation")
def Restart():
    os.system("shutdown /r")              
def Shutdown():
    os.system("shutdown /s")        
def Sleep():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")       
def Help():
    print("""         
           _                 _   
     /\   | |               | |  
    /  \  | |__   ___  _   _| |_ 
   / /\ \ | '_ \ / _ \| | | | __|
  / ____ \| |_) | (_) | |_| | |_ 
 /_/    \_\_.__/ \___/ \__,_|\__|""")

    print("""\n\n   Autome allows you to Hibernate, Lock, Logoff, Restart, Shutdown, Sleep your laptop or Alert you when your laptop's battery is at {X} percent.""")
    print("\n     • Select the number before the function you want to run.\n   • Then enter the battery percent when you want to call that function.\n")
def ask_battery_state():
    try:
        battery_state = int(input("\nEnter the battery % >>> "))
        time.sleep(1)

        return battery_state
    except KeyboardInterrupt:
        want_to_exit()
    except ValueError:
        print("please enter valid option or ctrl c to exit")  
        ask_battery_state() 
def get_battery_charge():
    battery = psutil.sensors_battery()    
    percent = battery.percent
    return percent

def main():
    global battery_charge
    battery_charge = get_battery_charge()
    required_battery_charge = ask_battery_state()
    try:
        hide()
        while required_battery_charge != battery_charge:
            battery_charge = get_battery_charge()   
            if required_battery_charge == battery_charge:
                show()
                pass
    except KeyboardInterrupt:
        want_to_exit()
def hide(): 
    ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )
def show():
    ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 1 )

def procedure(option):
    main()
    if option == 1:
        Alert()
    elif option == 2:
        Hibernate()
    elif option == 3:
        Lock()
    elif option == 4:
        Logoff()        
    elif option == 5:
        Restart()
    elif option == 6:
        Shutdown()
    elif option == 7:
        Sleep()
def want_to_exit():
    try:
        ask = input("\nDo you want to exit? [y/n]")
        ask = ask.lower()
        if ask == 'y':
            exit()
        elif ask == 'n':
            main_menu()
        else:
            print("\nInvalid command!")        
            main_menu()
    except:
        exit()        
def main_menu():
    print("\n\n[+] Main Menu")
    options="""
    0:Exit 
    1:Alert
    2:Hibernate
    3:Lock
    4:Logoff
    5:Restart
    6:Shutdown
    7:Sleep
    8:Help"""
    try:
        print(options)
        option = int(input("\n>>> "))
        if option not in range(9):
            print('\nPlease select valid command!')
            main_menu()    
        if option == 0:
            exit()    
        elif option == 8:
            Help()    
            main_menu()
        procedure(option)    

        print("\n\nTask completed!\n\n")
        try:
            input("Press ENTER to continue! ")
        except:
            main_menu()
        main_menu()    
    except ValueError:
        print("\nPlease select valid command!")
        main_menu()
    except KeyboardInterrupt:
        want_to_exit()

print("""
     █████╗ ██╗   ██╗████████╗ ██████╗ ███╗   ███╗███████╗
    ██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗████╗ ████║██╔════╝
    ███████║██║   ██║   ██║   ██║   ██║██╔████╔██║█████╗  
    ██╔══██║██║   ██║   ██║   ██║   ██║██║╚██╔╝██║██╔══╝  
    ██║  ██║╚██████╔╝   ██║   ╚██████╔╝██║ ╚═╝ ██║███████╗
    ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ ╚═╝     ╚═╝╚══════╝
""")


main_menu()
     
