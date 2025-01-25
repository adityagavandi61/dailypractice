class coffiestore:
    def __init__(self):
        self.coffie = {'Espresso': 2.5, 'Latte': 3.0, 'Cappuccino': 3.5,
                       'Mocha': 4.0, 'Macchiato': 4.5, 'Americano': 5.0, 'Affogato': 5.5}
        print("Welcome to the Coffee Store")
        self.menu()

    def menu(self):
        while True:
            print("1. View Coffee")
            print("2. Buy Coffee")
            print("3. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.view_coffee()
            elif choice == 2:
                self.buy_coffie()
            elif choice == 4:
                break
            else:
                print("Invalid choice. Try again.")

    def buy_coffie(self):
        coffee = input("Enter the name coffee: ")
        if coffee in self.coffie:
            quantity = int(input("Enter quantity of coffie: "))
            print(f"Price: {self.coffie[coffee]*quantity}")
            print("Coffee bought successfully.")
        else:
            print("Invalid coffee name. Try again.")

    def view_coffee(self):
        for coffee, price in self.coffie.items():
            print(f"\nCoffee: {coffee}. Price: {price}\n")
        print("-------------------------------")


if __name__ == "__main__":
    coffiestore = coffiestore()
