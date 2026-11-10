rooms = {
    101: "Available",
    102: "Available",
    103: "Available",
    104: "Available",
    105: "Available"
}

bookings = {}


def view_available_rooms():
    print("\nAvailable Rooms:")

    available_count = 0

    for room_number, status in rooms.items():
        if status == "Available":
            print(room_number)
            available_count += 1

    if available_count == 0:
        print("No rooms are currently available")


def book_room():
    customer_name = input("Enter customer name: ").strip()

    if not customer_name:
        print("Customer name cannot be empty")
        return

    view_available_rooms()

    try:
        room_number = int(input("Enter room number: "))
    except ValueError:
        print("Please enter a valid room number")
        return

    if room_number not in rooms:
        print("Invalid room number")

    elif rooms[room_number] == "Booked":
        print("This room is already booked")

    else:
        rooms[room_number] = "Booked"
        bookings[room_number] = customer_name

        print("\nRoom booked successfully!")
        print("Customer Name:", customer_name)
        print("Room Number:", room_number)


def cancel_booking():
    try:
        room_number = int(input("Enter room number to cancel: "))
    except ValueError:
        print("Please enter a valid room number")
        return

    if room_number not in rooms:
        print("Invalid room number")

    elif rooms[room_number] == "Available":
        print("This room is not booked")

    else:
        print("Booking found for:", bookings[room_number])

        del bookings[room_number]
        rooms[room_number] = "Available"

        print("Booking cancelled successfully")


def view_all_bookings():
    if not bookings:
        print("No bookings available")
        return

    print("\n===== CURRENT BOOKINGS =====")

    for room_number, customer_name in bookings.items():
        print("Room Number:", room_number)
        print("Customer Name:", customer_name)
        print("---------------------------")


def search_booking():
    try:
        room_number = int(input("Enter room number to search: "))
    except ValueError:
        print("Please enter a valid room number")
        return

    if room_number not in rooms:
        print("Invalid room number")

    elif room_number in bookings:
        print("\nBooking Found")
        print("Room Number:", room_number)
        print("Customer Name:", bookings[room_number])

    else:
        print("This room has no booking")


while True:
    print("\n===== HOTEL ROOM BOOKING SYSTEM =====")
    print("1. View Available Rooms")
    print("2. Book a Room")
    print("3. Cancel Booking")
    print("4. View All Bookings")
    print("5. Search Booking by Room Number")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_available_rooms()

    elif choice == "2":
        book_room()

    elif choice == "3":
        cancel_booking()

    elif choice == "4":
        view_all_bookings()

    elif choice == "5":
        search_booking()

    elif choice == "6":
        print("Thank you for using Hotel Room Booking System!")
        break

    else:
        print("Invalid choice. Please try again.")