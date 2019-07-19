command=""
started = False
while command !="quit":
    command = input("> ").lower()
    if command=="start":
        if started:
            print("Car is alredy started!")
        else:
            started = True
            print("Car started...")
    elif command== "stop":
        if not started:
            print("Car is alredy stopped!")
        else:
            started = False
            print("Car stopped.")
    elif command =="help":
        print("""
start - to strat the car
stop - to stop the car
quit - to quit
        """)
    else:
        print("Sorry, I don't understand that!")