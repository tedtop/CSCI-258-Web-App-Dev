import socket

# Default connection settings (hit enter for these to use defaults)
HOST = "127.0.0.1"    # The server's hostname or IP address
PORT = 65432          # The port used by the server

print("Digit Sum Client Started")

# Get server IP address from user (allow empty for default)
server_ip = input("Server IP >> ")
if server_ip == "":
    server_ip = HOST

# Get server port from user (allow empty for default)
server_port = input("Server Port >> ")
if server_port == "":
    server_port = PORT
else:
    server_port = int(server_port)

# Get initial digit string from user
current_string = input("Digit Sum starting string >> ")

# Connect to server and start communication
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((server_ip, server_port))

    while True:
        # Send current string to server
        s.sendall(current_string.encode())

        # Receive response from server
        data = s.recv(1024)
        response = data.decode()

        # Check if server returned an error
        if "error" in response.lower():
            print(f"Server returned \"{response}\", Exiting Client Application")
            break

        print(f"Received Digit Sum result: {response}")

        # Check if response is a single digit (exit condition)
        if len(response) == 1:
            print("Server returned a single digit result, Exiting Client Application")
            break

        # Send the response back to server for next calculation
        print(f"Sending {response} to Digit Sum Server")
        current_string = response