def serquina_menu():
    while True:
        print("\nHello, I'm Zcintilla R. Serquina.")
        print("1. Basic Info")
        print("2. Goals")
        print("3. Motto")
        print("3. Comment from Besa")
        print("4. Comment from Bualat")
        print("5. Comment from Maestre")
        print("6. Comment from Salespara")
        print("7. Exit")
        choice = input("Please choose an option: ")

        match choice: 
            case '1':
              print("Age: 20 years old")
              print("Birthday: October 5, 2004")
              print("Address: Central Signal, Taguig City")
            case '2':
                print("One of my goals is to improve my programming skills,")
                print("and to be a successful UI/UX designer.")
            case '3':
                print("Remember why you started, and never give up.")
            case '4':
                print("Besa's comment: ")
                # TODO: Add your comment here
            case '5':
                print("Bualat's comment: ")
                print("You are a very kind person, Zcintilla.")
            case '6':
                print("Maestre's comment: ")
                # TODO: Add your comment here
            case '7':
                print("Salespara's comment: ")
                # TODO: Add Besa's comment here
            case '8':
                break
            case _:
                print("Invalid choice! Please try again.")