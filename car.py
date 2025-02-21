helping = input('>')
i = 0
if helping.upper() == 'HELP':
    print('start - to start the car')
    print('stop - to stop the car')
    print('quit - to exit the game')
    while i < 4:
        command=input('>')
        if command == 'start':
            print('Starting the car: Ready to go!')
        elif command == 'stop':
            print('The car stopped')
        elif command == 'quit':
            break
        else:
            print("i don't understand that")
        i += 1
        

                  