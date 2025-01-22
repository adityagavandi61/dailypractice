class Palindrone:
    def __init__(self):
        self.string = str(input("Enter a string: "))

    def reverse_string(self):
        self.rev = ""
        for i in self.string:
            self.rev = i + self.rev
        print("The reverse of the string is: ", self.rev)

    def is_palindrone(self):
        if self.string == self.rev:
            print("The string is a palindrone.")
        else:
            print("The string is not a palindrone.")
    
    def main(self):
        self.reverse_string()
        self.is_palindrone()

if __name__ == "__main__":
    p = Palindrone()
    p.main()