import time 
import keyboard


def current_Time():
 #12-hr Formate..
    print("press Ctrl to choose next choice")
    print("Current Time : ")
    while True:
        current_time = time.strftime('%I:%M:%S %p')   # formatting
        print(current_time , end="\r")
        time.sleep(1)
        
        if keyboard.is_pressed('ctrl'):    # ctrl is used to stop the clock to avoid Infinte loop 
            print("\nclock stopped.\n")
            break


def StopWatch():
    print("\nPress the ENTER button to start or end the StopWatch !")
    input()
    print("StopWatch started ->")
    start = time.time()     #start time noted 
    input()
    print("StopWatch ended ->")
    end = time.time()       #end time noted

    actual_time = end - start       # actual time of stopwatch

    hour = int(actual_time // 3600)            # time converted into full hour ie (quotent) 
    minute = int((actual_time % 3600)//60)     # time is converted into full minutes ie (remainder of hour) 
    second = int(actual_time % 60)             # time is converted into full second ie (remainder of minute)
    print(f"The time is : {hour:02}:{minute:02}:{second:02}")       # to display the time (02 is for formatting)
    


def Timer():
    running_time = 0
    print("Timer started! -> Press ctrl Button to stop.")
    
    while True:
        minutes = running_time // 60       # converting time to minutes
        seconds = running_time % 60        # converting rest time into second
        print(f"\rTimer: {minutes:02}:{seconds:02}", end="", flush=True)      #formate
        time.sleep(1)  
        running_time += 1  

        if keyboard.is_pressed('ctrl'):    # ctrl is used to stop the timer (you can change it for your ease)
            print("\nTimer stopped.\n")
            break


def main():

    while True:
        print("\nChoose the options : ")
        print("1. Current Time.")
        print("2. Timer.")
        print("3. StopWatch.")
        print("4. Exit !!")

        choice = input()

        if choice == '1':
            current_Time()
        elif choice == '2':
            Timer()
        elif choice == '3':
            StopWatch()
        elif choice == '4':
            print("Exiting... \n Thankyou 😋")
            break
        else:
            print("Invalid choice !!! ")

main()