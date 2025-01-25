class bookingshow:
    def __init__(self):
        self.menu = { '1':'Add Booking' , '2':'View Booking' , '3':'Delete Booking' , '4':'Exit' }
        self.seats = {'vip':10, 'premium':20, 'economy':30}
        self.bookings = {}
        self.booking_id = 0
    def menuitems(self):
        while True:
            self.menu_display()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_booking()
            elif choice == '2':
                self.view_booking()
            elif choice == '3':
                self.delete_booking()
            elif choice == '4':
                break
            else:
                print("Invalid choice")
    def menu_display(self):
        for key,menuname in self.menu.items():
            print(key,menuname)
    def add_booking(self):
        self.booking_id += 1
        name = input("Enter your name: ")
        show = input("Enter show name: ")
        showtime = input("Enter show time: ")
        for seattype,seats in self.seats.items():
            print(seattype,seats)
        seattype = input("Enter seat type: ")
        seat_books = int(input("Enter number of seats: "))
        if self.seats[seattype] > 0:
            self.seats[seattype] -= seat_books
            self.bookings[self.booking_id] = [name,show,showtime,seattype,seat_books]
        else:
            print("No seats available")
    def view_booking(self):
        for booking_id,booking in self.bookings.items():
            print(booking_id,booking)
    def delete_booking(self):
        booking_id = int(input("Enter booking id to delete: "))
        del self.bookings[booking_id]
        print("Booking deleted")

if __name__ == "__main__":
    b1=bookingshow()
    b1.menuitems()
