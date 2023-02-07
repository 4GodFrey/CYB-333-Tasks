command = ""
on = False
while True:
    command = input(">").lower()
    if command == "start":
        if on:
            print("car is already started!")
        else:
            on = True
            print("car started...")
    elif command == "stop":
        if not on:
            print("car is already stopped")
        else:
            on = False
            print("car stopped...")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit = to quit
        """)
    elif command == "quit":
        print("program is terminated.")
        break
    else:
        print("sorry, I don't understand that!")
