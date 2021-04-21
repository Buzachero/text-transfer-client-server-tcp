# text-transfer-client-server-tcp
Application client/server that handles text transfer between them. 

The text that is transferred is located in client/server files, configured in the properties.

### Configuration
All the application's properties can be configured in constants.py

```
PREFIX_IP_ALLOWED: prefix of the client ip address allowed to communicate with the server
AUTHORIZATION_KEY: authorization secret key for client/server communication
CLIENT_FILE_PATH: file path of the client where text is sent or received to/from the server
SERVER_FILE_PATH: file path of the server where text is sent or received to/from the client
SUCCESS_AUTH_REPLY = server success reply
FAILURE_AUTH_REPLY = server failure reply
SERVER_HOST: host of the server
PORT: listen port of the server
SECONDS_BEFORE_CLOSE_CONN = number of seconds before the server close the TCP connection
```

### Description
Client/server of the application communicate using the TCP protocol. 

The client firstly send an option number to the server, indicating:
<ul>
<li>Client wants to send data to the server;</li>
<li>Client wants to receive data from the server;</li>
</ul>

And then, according to the option, the client:
<ul>
<li>Sends text to the server from the file located at <i><b>CLIENT_FILE_PATH</b></i>;</li>
<li>Receives text from the server from the file located at <i><b>SERVER_FILE_PATH</b></i>;</li>
</ul>

For more security, an <i><b>authorization_key</b></i> and <i><b>client prefix ip address allowed</b></i> were added, so that every data client sends to the server, the server can check if the client ip address is allowed to send data, as well as if the <i><b>authorization key</b></i> matches with the expected.
If one of these conditions fail, the server reject the message and stop its processing.
