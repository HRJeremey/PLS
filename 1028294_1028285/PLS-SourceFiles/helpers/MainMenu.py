import os

def  PrintMenu(options, clear):
    #if clear:
        #os.system("cls")
    for id, info in options.items():   
        for key in info:
            print("[" + str(id) + "]" + " " + str(key))

    __WaitForInput(options)

def __WaitForInput(options):
    try:
        chosen = int(input("Select option: "))
        if chosen == 0 :
            print("No item with id: 0")
            __WaitForInput(options)

        if chosen > len(options.keys()):
            print("Chosen number does not exist in menu! Try again.")
            __WaitForInput()
        else:
            for el, info in options.items():
                for key in info:
                    if (el == chosen):
                        info[key]()
                        return
                    else:
                        break
                    
    except ValueError:
        print("Value must be a number!")
        __WaitForInput(options)



