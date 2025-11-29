import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
print("Server starting...")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Allow socket reuse to prevent "Address already in use" errors
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    print(f"Server listening socket: {s.getsockname()}")
    s.listen()

    # Accept client connection
    conn, addr = s.accept()
    with conn:
        while True:
            # Receive data from client
            data = conn.recv(1024)
            if not data:
                break

            # Decode the received string and remove whitespace
            received_string = data.decode().strip()
            print(f'Received string "{received_string}"')

            # Check if string contains only digits
            if not received_string.isdigit():
                print("Invalid Input, Exiting Server Application")
                # Send error message to client
                conn.sendall("Not A Number error".encode())
                break

            # Check if input is already a single digit
            if len(received_string) == 1:
                print("Digit sum is a single digit, Exiting Server Application")
                # Send the single digit back to client
                conn.sendall(received_string.encode())
                break

            # Calculate digit sum by adding each digit
            digit_sum = 0
            for digit_char in received_string:
                digit_sum += int(digit_char)

            digit_sum_str = str(digit_sum)
            print(f"Sending Digit Sum result: {digit_sum}")

            # Send result back to client
            conn.sendall(digit_sum_str.encode())

            # If the result is a single digit, terminate
            if len(digit_sum_str) == 1:
                print("Digit sum is a single digit, Exiting Server Application")
                break