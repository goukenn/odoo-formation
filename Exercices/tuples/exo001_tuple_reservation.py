# Tuple exercices
# ## color
# Write a program that stores a color as a tuple of three integers (red, green, blue), each between 0 and 255. Your program must:
# - Ask the user to enter three values (r, g, b)
# - Store them as a tuple
# - Display the color in two formats:
#     - Decimal: RGB(255, 128, 0)
#     - Hexadecimal: #FF8000
# Try to unpack the tuple into three separate variables and display each channel individually

def readColor():
    r, g, b = map(int, input('define color (format: R,G,B)? ').split(','))
    print (f'Decimal: RGB({r},{g},{b})')
    # print (f'Hexadecimal: #{hex(r)[2:]}{hex(g)[2:]}{hex(b)[2:]}')
    print (f'Hexadecimal: #{r:02X}{g:0>2X}{b:0>2X}')
    return tuple()

tuple_list = [readColor() for _ in range(3)]

print( tuple_list)

# ## Cinema
# You are building a seat reservation system for a small cinema. Each seat is identified by a tuple (row, number) — for example ("A", 5) or ("C", 12). The cinema has 4 rows (A, B, C, D) and 8 seats per row. The program runs in the terminal with a menu.
# Requirements:
# - Store all bookings in a dictionary where the key is a seat tuple (row, number) and the value is the guest's name.
# - The seating plan displays a grid of the cinema, marking booked seats with [X] and free ones with [ ].
# - Booking asks for a row, a seat number, and a guest name. Reject the booking if the seat is already taken or doesn't exist.
# - Cancelling asks for a row and seat number, and removes the booking if it exists.
# - Search by name finds all seats booked under a given name (a guest could book multiple seats).
# - Available seats lists all free seat tuples in order.