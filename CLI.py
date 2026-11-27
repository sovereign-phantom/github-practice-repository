from classPerson import Person

class CLI:
    def __init__(self, person: Person):
        self.person = person

    def run(self):
        while True:
            print("\nOptions:")
            print("1. Spend Money")
            print("2. Earn Money")
            print("3. Show Transactions")
            print("4. Generate Summary Image")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.person.spend_money()
            elif choice == "2":
                self.person.earn_money()
            elif choice == "3":
                self.person.show_transactions()
            elif choice == "4":
                while True:
                    filename = input(
                        "Enter the filename for the summary image. (filename must end with .png)\n"
                        "(press Enter for default 'summary.png'): "
                    )
                    if filename.endswith(".png") or not filename:
                        break
                    else:
                        print("Invalid filename. Please enter a filename ending with .png.")
                if not filename:
                    filename = "summary.png"
                self.person.generate_image(filename)
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")