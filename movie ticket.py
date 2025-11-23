# Simple Movie Ticket Booking System

seats = [
    [0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0],  
    [0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0]   
]

movies = ("1. Avengers", "2. Spider-Man", "3. Titanic", "4. Inception")

def display_seats():
    print("\n" + " " * 10 + "SCREEN HERE")
    print("   " + " ".join([str(i+1) for i in range(6)]))
    print("-" * 25)
    for i in range(5):
        row = ""
        for j in range(6):
            if seats[i][j] == 0:
                row += "[ ] "
            else:
                row += "[X] "
        print(f"Row {i+1}: {row}")
    print("-" * 25)

def book_ticket():
    display_seats()
    
    print("\nAvailable Movies:")
    for movie in movies:
        print(movie)
    
    while True:
        movie_choice = input("\nChoose movie (1-4): ")
        if movie_choice in ["1", "2", "3", "4"]:
            selected_movie = movies[int(movie_choice)-1]
            break
        print("Invalid movie choice!")
    
    
    while True:
        try:
            row = int(input("Enter row (1-5): ")) - 1
            col = int(input("Enter seat number (1-6): ")) - 1
            
            if 0 <= row <= 4 and 0 <= col <= 5:
                if seats[row][col] == 0:
                    seats[row][col] = 1
                    print(f"\nTicket booked successfully!")
                    print(f"Movie: {selected_movie}")
                    print(f"Seat: Row {row+1}, Seat {col+1}")
                    break
                else:
                    print("Sorry, this seat is already booked! Choose another.")
            else:
                print("Invalid row or seat number!")
        except ValueError:
            print("Please enter numbers only!")

def show_booked_seats_count():
    booked = 0
    for row in seats:
        for seat in row:
            if seat == 1:
                booked += 1
    available = 30 - booked
    print(f"\nTotal seats: 30")
    print(f"Booked seats: {booked}")
    print(f"Available seats: {available}\n")


def main():
    print("=== Welcome to Mini Cinema Ticket Booking ===")
    
    while True:
        print("\n1. View seats")
        print("2. Book a ticket")
        print("3. View booking statistics")
        print("4. Exit")
        
        choice = input("\nChoose option (1-4): ")
        
        if choice == "1":
            display_seats()
        elif choice == "2":
            book_ticket()
        elif choice == "3":
            show_booked_seats_count()
        elif choice == "4":
            print("Thank you! Enjoy the movie 🍿")
            break
        else:
            print("Wrong option! Try again.")


main()