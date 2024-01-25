import logo
import querys

def print_menu():

    print("------------------------------")    
    print("Select a option")
    print("------------------------------",'\n')

    print("1. Create Registry")
    print("2. Read database")
    print("3. Update delivery")
    print("4. Delete database")
    print("5. Exit app")

    print('\n')        


def main():
    
    logo.print_logo()

    try:
        while True:

            print_menu()

            option = int(input("Select yor option: "))
                
            if option == 1:
                request = querys.create_Registry()

                if request == 2:
                    break
                if request == 1:
                    continue

            elif option == 2:
                request = querys.check_Database()

                if request == 2:
                    break
                if request == 1:
                    continue

            elif option == 3:
                request = querys.update_Data()

                if request == 2:
                    break
                if request == 1:
                    continue

            elif option == 4:
                request = querys.delete_Data()

                if request == 2:
                    break
                if request == 1:
                    continue

            elif option == 5:
                print('\n')
                print("See you soon!", '\n')
                print("Exit app ...", '\n')
                break
            else:
                print("[Error]: Please insert a valid argument")
                print("[Usage]: insert number between 1 and 5")
                continue

    except KeyboardInterrupt:
        print('\n')
        print("Clossing App ...")
        print('\n')

if __name__ == "__main__":
    main()

