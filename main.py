class CinemaHall:
    def init(self, rows, seats_per_row):
        self.rows = rows
        self.seats_per_row = seats_per_row
        self.seating_arrangement = [['S' for j in range(seats_per_row)] for i in range(rows)]
        self.booked_seats = []

    def display_seating_arrangement(self):
        print('Cinema Hall Layout:')
        print('  ' + ' '.join([str(i) for i in range(1, self.seats_per_row+1)]))
        for i in range(self.rows):
            print(str(i+1) + ' ' + ' '.join(self.seating_arrangement[i]))
        print()

    def book_seats(self):
        row_number = int(input('Enter row number: '))
        seat_number = int(input('Enter seat number: '))
        if self.seating_arrangement[row_number-1][seat_number-1] == 'B':
            print('This seat is already booked. Please choose another seat.')
            return
        self.seating_arrangement[row_number-1][seat_number-1] = 'B'
        self.booked_seats.append((row_number, seat_number))
        print('Seat(s) booked successfully!')

    def cancel_booking(self):
        row_number = int(input('Enter row number: '))
        seat_number = int(input('Enter seat number: '))
        if (row_number, seat_number) not in self.booked_seats:
            print('Booking not found. Please enter valid row and seat number.')
            return
        self.seating_arrangement[row_number-1][seat_number-1] = 'S'
        self.booked_seats.remove((row_number, seat_number))
        print('Booking cancelled successfully!')

    def generate_ticket(self, row_number, seat_number):
        print('Ticket Details:')
        print(f'Row Number: {row_number}')
        print(f'Seat Number: {seat_number}')
        print(f'Cinema Hall: My Cinema')
        print(f'Show Timings: 10 AM')
        print(f'Price: $10')
        print('Enjoy the show!')

def main():
    cinema_hall = CinemaHall(rows=5, seats_per_row=10)
    while True:
        print('1. Display Seating Arrangement')
        print('2. Book Seats')
        print('3. Cancel Booking')
        print('4. Exit')
        choice = int(input('Enter your choice: '))
        if choice == 1:
            cinema_hall.display_seating_arrangement()
        elif choice == 2:
            cinema_hall.display_seating_arrangement()
            cinema_hall.book_seats()
        elif choice == 3:
            cinema_hall.cancel_booking()
        elif choice == 4:
            break
        else:
            print('Invalid choice. Please enter a valid choice.\n')

if __name__ == 'main':
    main()