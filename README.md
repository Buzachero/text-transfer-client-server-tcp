# text-transfer-client-server-tcp
Client/server application that handles text transfer between them. 

The text that is transferred is located in client/server files, configured in the properties.

### Configuration
All the application's properties can be configured in constants.py

```
AUTHENTICATION_KEY: authentication secret key for client/server communication
CLIENT_FILE_PATH: file path of the client where text is sent or received to/from the server
SERVER_FILE_PATH: file path of the server where text is sent or received to/from the client
SUCCESS_AUTH_REPLY: authentication successful reply from the server
FAILURE_AUTH_REPLY: authentication failure reply from the server
SERVER_HOST: host of the server
PORT: listening port of the server
```

### Description
The communication between client and server is done by the usage of TCP protocol.

After successful authentication (described below), the client firstly send an option number to the server, indicating:
<ul>
<li>Client wants to send data to the server;</li>
<li>Client wants to receive data from the server;</li>
</ul>

And then, according to the option, the client:
<ul>
<li>Sends text to the server from the file located at <i><b>CLIENT_FILE_PATH</b></i>;</li>
<li>Receives text from the server from the file located at <i><b>SERVER_FILE_PATH</b></i>;</li>
</ul>

For more security, an <i><b>authentication key</b></i> was added, so that every client connecting to the server, the server can check if the <i><b>authentication key</b></i> matches with the expected.
If not, the server replies with <i><b>FAILURE_AUTH_REPLY</b></i> message to the client, and waits again for the client to send a valid <i><b>authentication key</b></i>. If client sends a valid <i><b>authentication key</b></i>, the server replies back <i><b>SUCCESS_AUTH_REPLY</b></i> message.

