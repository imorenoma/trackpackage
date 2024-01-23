
import querys

def main():
    print('\n')
    print("------------------------------")    
    print("Chose the proper option")
    print("------------------------------",'\n')

    print("1. Insert package Track number")
    print("2. Move date delivery")
    print("3. Cancel delivery")
    print("4. List of track numbers")
    print("5. Exit app")

    print('\n')

    options = {
        '1': querys.insert_data(),
        # '2': app.modify_data(),
        # '3': app.delete_data(),
        # '4': app.send_query(),
        # '5': app.send_query(),
        # '6': app.exit()
    }

    try:
        input_option = input("Select yor option: ")
        
        if input_option == '1':
            print(options["1"],)

    except KeyboardInterrupt:
        print('\n')
        print("Clossing App ...")
        print("Bye")
        print('\n')

if __name__ == "__main__":
    main()