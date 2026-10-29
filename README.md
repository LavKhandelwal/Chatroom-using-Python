Python Socket Programming Chatroom

About the Project:

This project is a simple, terminal-based chatroom application developed using Python socket programming and multithreading. It allows multiple clients to connect to a central server, join the chatroom using their nicknames, and exchange messages in real time. The server broadcasts messages to connected clients and notifies users when someone joins or leaves the chatroom.

Features:

- Multi-client communication: Supports multiple clients connecting to one server.


- Nickname identification: Users can join the chatroom using their chosen nicknames.


- Real-time messaging: Messages are transmitted using TCP socket connections.


- Message broadcasting: Messages are distributed to connected clients.


- Join notifications: Displays a message when a user joins the chatroom.


- Leave notifications: Notifies other users when a client disconnects.


- Multithreading: Uses Python threads to handle multiple client connections concurrently.


- Localhost communication: Runs on the same computer by default.



Technologies Used:

- Python 3


- Socket Programming for network communication using TCP.


- Threading for handling multiple clients concurrently.


Project Structure:

├── chatroom.py

└── README.md


 
 Requirements:

- Python 3 installed on your system.


- Visual Studio Code or another Python-compatible editor.


- A terminal or command prompt.


No additional Python packages are required.


How to Run the Project:


1. Clone the Repository


```bash
git clone https://github.com/<your-username>/<your-repository>.git
```


Navigate to the project directory:

```bash
cd <your-repository>
```


Alternatively, download the project and open its folder in VS Code.


### 2. Start the Server


Open a terminal and run:


```bash
python chatroom.py
```


On Windows, you can also use:

```bash
py chatroom.py
```

When prompted, enter:

```text
server
```

The terminal displays:

```text
Server is listening...
```

Keep the server running while clients connect.


3. Connect the First Client


Open a second terminal in the same project folder and run:

```bash
python chatroom.py
```

Enter:

```text
client
```

When prompted for a nickname, enter a name such as:

```text
Alice
```


4. Connect More Clients


Open additional terminals and repeat the client steps. Use different nicknames, such as `Bob` or `Charlie`, to simulate multiple users.


5. Start Chatting


Type a message in a client terminal and press Enter. Messages are broadcast through the server to connected clients.


Example Output:


Server Terminal


```text
Server is listening...
Connected with ('127.0.0.1', 54321)
Nickname is Alice
Connected with ('127.0.0.1', 54322)
Nickname is Bob
```


Client Terminal


```text
Enter your nickname: Alice
Connected to the chatroom!
Bob joined the chat!
Alice: Hello everyone!
Bob: Hi Alice!
```

*Note: Port numbers and the order of displayed messages may vary.*


How It Works:


Server:


1. Creates a TCP socket and binds it to the configured host and port.


2. Listens for incoming client connections.


3. Accepts connections and receives each client's nickname.


4. Maintains lists of connected clients and their nicknames.


5. Broadcasts messages to connected clients.


6. Starts a separate thread to handle messages from each client.


7. Removes disconnected clients and announces their departure.


Client:

1. Prompts the user to enter a nickname.


2. Connects to the server using the configured host and port.


3. Starts a thread to receive and display incoming messages.


4. Starts another thread to read user input and send messages.


5. Continues communicating until the connection is closed.


Configuration"

The server address and port are configured near the beginning of `chatroom.py`:

```python
HOST = '127.0.0.1'
PORT = 12345
```

- `HOST`: The loopback IP address, which allows communication on the same computer.
- `PORT`: The TCP port used by the chatroom.


For communication between different computers, the host and network configuration must be changed appropriately, and firewall rules may need to permit the connection.


Testing:

[Test Case | Expected Result]


Start the server | Server begins listening for connections. 


Connect a client | Client establishes a connection with the server. 


Enter a nickname | Server receives and records the nickname. 


Send a message | Server broadcasts the message to connected clients. 


Connect another client | The new client joins the chatroom. 


Disconnect a client | Server attempts to remove the client and notify others. 


Limitations:



- The application runs in the terminal and does not have a graphical user interface.


- By default, communication is limited to the local computer.


- The server uses shared client lists without explicit thread synchronization.


- Message broadcasting and disconnection handling are basic and may require improvements for reliability.


- Messages are not encrypted, and the application does not implement user authentication.



Future Enhancements:



- Develop a graphical user interface.


- Add private messaging between users.


- Implement secure communication and user authentication.


- Improve error handling and thread synchronization.


- Add file sharing and chat history.


- Support communication over a local network or the internet.


License:
This project is intended for educational purposes. 
