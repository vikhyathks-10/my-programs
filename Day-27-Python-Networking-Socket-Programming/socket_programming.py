# ============================================================
# MONTH 8 - DAY 27
# PYTHON NETWORKING & SOCKET PROGRAMMING
#
# Programs 136-140
#
# 136. Get Local IP Address
# 137. TCP Client-Server
# 138. Two-Way Communication
# 139. Simple Network File Transfer
# 140. Mini LAN Chat Application
#
# Library:
# socket
#
# How to run:
# python socket_programming.py
# ============================================================

import socket
import os
import threading


# ============================================================
# CONFIGURATION
# ============================================================

HOST = "127.0.0.1"
PORT = 5000

BUFFER_SIZE = 4096


# ============================================================
# PROGRAM 136
# GET LOCAL IP ADDRESS
# ============================================================

def get_local_ip():

    print("\n" + "=" * 60)
    print("             PROGRAM 136 - LOCAL IP")
    print("=" * 60)

    try:

        hostname = socket.gethostname()

        ip_address = socket.gethostbyname(
            hostname
        )

        print(
            f"\nHostname   : {hostname}"
        )

        print(
            f"IP Address : {ip_address}"
        )

        # ----------------------------------------------------
        # Get the IP used for network communication
        # ----------------------------------------------------

        try:

            test_socket = socket.socket(
                socket.AF_INET,
                socket.SOCK_DGRAM
            )

            test_socket.connect(
                ("8.8.8.8", 80)
            )

            network_ip = test_socket.getsockname()[0]

            test_socket.close()

            print(
                f"Network IP : {network_ip}"
            )

        except OSError:

            print(
                "Network IP : Could not determine"
            )

    except socket.error as e:

        print(
            f"\nError: {e}"
        )


# ============================================================
# PROGRAM 137
# TCP SERVER
# ============================================================

def tcp_server():

    print("\n" + "=" * 60)
    print("             PROGRAM 137 - TCP SERVER")
    print("=" * 60)

    server_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    # Allows quick reuse of the port
    server_socket.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_REUSEADDR,
        1
    )

    try:

        server_socket.bind(
            (HOST, PORT)
        )

        server_socket.listen(1)

        print(
            f"\nServer started."
        )

        print(
            f"Listening on {HOST}:{PORT}"
        )

        print(
            "\nWaiting for client..."
        )

        client_socket, client_address = (
            server_socket.accept()
        )

        print(
            f"\nClient connected: "
            f"{client_address}"
        )

        data = client_socket.recv(
            BUFFER_SIZE
        )

        if data:

            message = data.decode(
                "utf-8"
            )

            print(
                f"\nMessage from client: "
                f"{message}"
            )

            response = (
                "Message received by server!"
            )

            client_socket.sendall(
                response.encode(
                    "utf-8"
                )
            )

        client_socket.close()

        server_socket.close()

        print(
            "\nServer closed."
        )

    except OSError as e:

        print(
            f"\nServer error: {e}"
        )

        server_socket.close()


# ============================================================
# PROGRAM 137
# TCP CLIENT
# ============================================================

def tcp_client():

    print("\n" + "=" * 60)
    print("             PROGRAM 137 - TCP CLIENT")
    print("=" * 60)

    message = input(
        "\nEnter message to send to server: "
    )

    client_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    try:

        client_socket.connect(
            (HOST, PORT)
        )

        print(
            "\nConnected to server."
        )

        client_socket.sendall(
            message.encode(
                "utf-8"
            )
        )

        response = client_socket.recv(
            BUFFER_SIZE
        )

        if response:

            print(
                "Server response:",
                response.decode(
                    "utf-8"
                )
            )

    except ConnectionRefusedError:

        print(
            "\nConnection refused."
        )

        print(
            "Make sure the TCP server is running."
        )

    except OSError as e:

        print(
            f"\nClient error: {e}"
        )

    finally:

        client_socket.close()

        print(
            "\nClient closed."
        )


# ============================================================
# PROGRAM 138
# TWO-WAY COMMUNICATION
# ============================================================

def two_way_server():

    print("\n" + "=" * 60)
    print("        PROGRAM 138 - TWO-WAY SERVER")
    print("=" * 60)

    server_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    server_socket.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_REUSEADDR,
        1
    )

    try:

        server_socket.bind(
            (HOST, PORT + 1)
        )

        server_socket.listen(1)

        print(
            f"\nTwo-way server listening on "
            f"{HOST}:{PORT + 1}"
        )

        print(
            "Waiting for client..."
        )

        client_socket, address = (
            server_socket.accept()
        )

        print(
            f"\nClient connected: {address}"
        )

        while True:

            data = client_socket.recv(
                BUFFER_SIZE
            )

            if not data:

                break

            message = data.decode(
                "utf-8"
            )

            print(
                f"\nClient: {message}"
            )

            if message.lower() == "exit":

                print(
                    "Client ended the communication."
                )

                break

            response = input(
                "Server: "
            )

            client_socket.sendall(
                response.encode(
                    "utf-8"
                )
            )

            if response.lower() == "exit":

                break

        client_socket.close()

        server_socket.close()

        print(
            "\nTwo-way server closed."
        )

    except OSError as e:

        print(
            f"\nServer error: {e}"
        )

        server_socket.close()


def two_way_client():

    print("\n" + "=" * 60)
    print("        PROGRAM 138 - TWO-WAY CLIENT")
    print("=" * 60)

    client_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    try:

        client_socket.connect(
            (HOST, PORT + 1)
        )

        print(
            "\nConnected to two-way server."
        )

        print(
            "Type 'exit' to end communication."
        )

        while True:

            message = input(
                "\nClient: "
            )

            client_socket.sendall(
                message.encode(
                    "utf-8"
                )
            )

            if message.lower() == "exit":

                break

            data = client_socket.recv(
                BUFFER_SIZE
            )

            if not data:

                break

            response = data.decode(
                "utf-8"
            )

            print(
                f"Server: {response}"
            )

            if response.lower() == "exit":

                break

    except ConnectionRefusedError:

        print(
            "\nConnection refused."
        )

        print(
            "Start the two-way server first."
        )

    except OSError as e:

        print(
            f"\nClient error: {e}"
        )

    finally:

        client_socket.close()

        print(
            "\nTwo-way client closed."
        )


def two_way_communication():

    print("\n" + "=" * 60)
    print("          PROGRAM 138 - TWO-WAY")
    print("=" * 60)

    print(
        "\n1. Start Server"
    )

    print(
        "2. Start Client"
    )

    choice = input(
        "\nEnter choice: "
    )

    if choice == "1":

        two_way_server()

    elif choice == "2":

        two_way_client()

    else:

        print(
            "\nInvalid choice."
        )


# ============================================================
# PROGRAM 139
# NETWORK FILE TRANSFER
# ============================================================

def file_transfer_server():

    print("\n" + "=" * 60)
    print("       PROGRAM 139 - FILE SERVER")
    print("=" * 60)

    server_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    server_socket.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_REUSEADDR,
        1
    )

    try:

        server_socket.bind(
            (HOST, PORT + 2)
        )

        server_socket.listen(1)

        print(
            f"\nFile server listening on "
            f"{HOST}:{PORT + 2}"
        )

        print(
            "Waiting for client..."
        )

        client_socket, address = (
            server_socket.accept()
        )

        print(
            f"\nClient connected: {address}"
        )

        # ----------------------------------------------------
        # Receive file name
        # ----------------------------------------------------

        filename_data = client_socket.recv(
            BUFFER_SIZE
        )

        if not filename_data:

            client_socket.close()
            server_socket.close()

            return

        filename = filename_data.decode(
            "utf-8"
        )

        # Prevent path traversal
        filename = os.path.basename(
            filename
        )

        save_filename = (
            "received_" + filename
        )

        print(
            f"\nReceiving file: {filename}"
        )

        # ----------------------------------------------------
        # Send confirmation
        # ----------------------------------------------------

        client_socket.sendall(
            b"READY"
        )

        # ----------------------------------------------------
        # Receive file
        # ----------------------------------------------------

        with open(
            save_filename,
            "wb"
        ) as file:

            while True:

                data = client_socket.recv(
                    BUFFER_SIZE
                )

                if not data:

                    break

                if data == b"FILE_END":

                    break

                file.write(
                    data
                )

        print(
            f"\nFile saved as: "
            f"{save_filename}"
        )

        client_socket.close()

        server_socket.close()

        print(
            "File server closed."
        )

    except OSError as e:

        print(
            f"\nServer error: {e}"
        )

        server_socket.close()


def file_transfer_client():

    print("\n" + "=" * 60)
    print("       PROGRAM 139 - FILE CLIENT")
    print("=" * 60)

    filename = input(
        "\nEnter path of small text file: "
    ).strip()

    if not os.path.isfile(
        filename
    ):

        print(
            "\nFile not found."
        )

        return

    if not filename.lower().endswith(
        ".txt"
    ):

        print(
            "\nPlease select a .txt file."
        )

        return

    filename_only = os.path.basename(
        filename
    )

    client_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    try:

        client_socket.connect(
            (HOST, PORT + 2)
        )

        print(
            "\nConnected to file server."
        )

        # ----------------------------------------------------
        # Send file name
        # ----------------------------------------------------

        client_socket.sendall(
            filename_only.encode(
                "utf-8"
            )
        )

        response = client_socket.recv(
            BUFFER_SIZE
        )

        if response != b"READY":

            print(
                "\nServer did not accept the file."
            )

            client_socket.close()

            return

        # ----------------------------------------------------
        # Send file
        # ----------------------------------------------------

        with open(
            filename,
            "rb"
        ) as file:

            while True:

                data = file.read(
                    BUFFER_SIZE
                )

                if not data:

                    break

                client_socket.sendall(
                    data
                )

        # ----------------------------------------------------
        # End marker
        # ----------------------------------------------------

        client_socket.sendall(
            b"FILE_END"
        )

        print(
            "\nFile sent successfully."
        )

    except ConnectionRefusedError:

        print(
            "\nConnection refused."
        )

        print(
            "Start the file server first."
        )

    except OSError as e:

        print(
            f"\nClient error: {e}"
        )

    finally:

        client_socket.close()

        print(
            "File client closed."
        )


def network_file_transfer():

    print("\n" + "=" * 60)
    print("          PROGRAM 139 - FILE TRANSFER")
    print("=" * 60)

    print(
        "\n1. Start File Server"
    )

    print(
        "2. Start File Client"
    )

    choice = input(
        "\nEnter choice: "
    )

    if choice == "1":

        file_transfer_server()

    elif choice == "2":

        file_transfer_client()

    else:

        print(
            "\nInvalid choice."
        )


# ============================================================
# PROGRAM 140
# MINI LAN CHAT APPLICATION
# ============================================================

def chat_receive_loop(
    connection,
    stop_event,
    name
):

    while not stop_event.is_set():

        try:

            data = connection.recv(
                BUFFER_SIZE
            )

            if not data:

                print(
                    "\nConnection closed."
                )

                stop_event.set()

                break

            message = data.decode(
                "utf-8"
            )

            if message == "CHAT_EXIT":

                print(
                    "\nOther user ended the chat."
                )

                stop_event.set()

                break

            print(
                f"\nOther: {message}"
            )

        except OSError:

            stop_event.set()

            break


def chat_server():

    print("\n" + "=" * 60)
    print("             PROGRAM 140 - CHAT SERVER")
    print("=" * 60)

    server_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    server_socket.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_REUSEADDR,
        1
    )

    try:

        server_socket.bind(
            (HOST, PORT + 3)
        )

        server_socket.listen(1)

        print(
            f"\nChat server listening on "
            f"{HOST}:{PORT + 3}"
        )

        print(
            "Waiting for client..."
        )

        client_socket, address = (
            server_socket.accept()
        )

        print(
            f"\nClient connected: {address}"
        )

        stop_event = threading.Event()

        receive_thread = threading.Thread(
            target=chat_receive_loop,
            args=(
                client_socket,
                stop_event,
                "Server"
            ),
            daemon=True
        )

        receive_thread.start()

        print(
            "\nChat started."
        )

        print(
            "Type 'exit' to leave."
        )

        while not stop_event.is_set():

            message = input(
                "You: "
            )

            if stop_event.is_set():

                break

            if message.lower() == "exit":

                client_socket.sendall(
                    b"CHAT_EXIT"
                )

                stop_event.set()

                break

            client_socket.sendall(
                message.encode(
                    "utf-8"
                )
            )

        client_socket.close()

        server_socket.close()

        print(
            "\nChat server closed."
        )

    except OSError as e:

        print(
            f"\nServer error: {e}"
        )

        server_socket.close()


def chat_client():

    print("\n" + "=" * 60)
    print("             PROGRAM 140 - CHAT CLIENT")
    print("=" * 60)

    client_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    try:

        client_socket.connect(
            (HOST, PORT + 3)
        )

        print(
            "\nConnected to chat server."
        )

        print(
            "Type 'exit' to leave."
        )

        stop_event = threading.Event()

        receive_thread = threading.Thread(
            target=chat_receive_loop,
            args=(
                client_socket,
                stop_event,
                "Client"
            ),
            daemon=True
        )

        receive_thread.start()

        while not stop_event.is_set():

            message = input(
                "You: "
            )

            if stop_event.is_set():

                break

            if message.lower() == "exit":

                client_socket.sendall(
                    b"CHAT_EXIT"
                )

                stop_event.set()

                break

            client_socket.sendall(
                message.encode(
                    "utf-8"
                )
            )

    except ConnectionRefusedError:

        print(
            "\nConnection refused."
        )

        print(
            "Start the chat server first."
        )

    except OSError as e:

        print(
            f"\nClient error: {e}"
        )

    finally:

        client_socket.close()

        print(
            "\nChat client closed."
        )


def mini_lan_chat():

    print("\n" + "=" * 60)
    print("              PROGRAM 140 - LAN CHAT")
    print("=" * 60)

    print(
        "\n1. Start Chat Server"
    )

    print(
        "2. Start Chat Client"
    )

    choice = input(
        "\nEnter choice: "
    )

    if choice == "1":

        chat_server()

    elif choice == "2":

        chat_client()

    else:

        print(
            "\nInvalid choice."
        )


# ============================================================
# MAIN MENU
# ============================================================

def display_menu():

    print("\n" + "=" * 65)
    print("       PYTHON NETWORKING & SOCKET PROGRAMMING")
    print("=" * 65)

    print(
        "1. Get Local IP Address"
    )

    print(
        "2. TCP Client-Server"
    )

    print(
        "3. Two-Way Communication"
    )

    print(
        "4. Simple Network File Transfer"
    )

    print(
        "5. Mini LAN Chat Application"
    )

    print(
        "6. Exit"
    )

    print("=" * 65)


# ============================================================
# PROGRAM 137 MENU
# ============================================================

def tcp_client_server():

    print("\n" + "=" * 60)
    print("              PROGRAM 137")
    print("              TCP CLIENT-SERVER")
    print("=" * 60)

    print(
        "\n1. Start Server"
    )

    print(
        "2. Start Client"
    )

    choice = input(
        "\nEnter choice: "
    )

    if choice == "1":

        tcp_server()

    elif choice == "2":

        tcp_client()

    else:

        print(
            "\nInvalid choice."
        )


# ============================================================
# MAIN FUNCTION
# ============================================================

def main():

    print(
        "\nWelcome to Python Networking!"
    )

    print(
        "Month 8 - Day 27"
    )

    while True:

        display_menu()

        choice = input(
            "Enter your choice: "
        ).strip()

        # ----------------------------------------------------
        # Program 136
        # ----------------------------------------------------

        if choice == "1":

            get_local_ip()

        # ----------------------------------------------------
        # Program 137
        # ----------------------------------------------------

        elif choice == "2":

            tcp_client_server()

        # ----------------------------------------------------
        # Program 138
        # ----------------------------------------------------

        elif choice == "3":

            two_way_communication()

        # ----------------------------------------------------
        # Program 139
        # ----------------------------------------------------

        elif choice == "4":

            network_file_transfer()

        # ----------------------------------------------------
        # Program 140
        # ----------------------------------------------------

        elif choice == "5":

            mini_lan_chat()

        # ----------------------------------------------------
        # Exit
        # ----------------------------------------------------

        elif choice == "6":

            print(
                "\nThank you for using "
                "Python Networking!"
            )

            break

        else:

            print(
                "\nInvalid choice."
            )


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":

    main()