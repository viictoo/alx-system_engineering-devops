This folder contains screenshots of the completed levels of the command-line-for-the-win challenge
https://cmdchallenge.com/
In addition to completing the project tasks and submitting the required screenshots to GitHub,
I made use of the SFTP (Secure File Transfer Protocol) command-line tool to move the local screenshots 
to the sandbox environment.

Here are the steps to  follow to push using sftp:

    Take the screenshots of the completed levels as mentioned in the general requirements.
    Open a terminal or command prompt on your local machine.
    Use the SFTP command-line tool to establish a connection to the sandbox environment. 
	You will need the hostname, username, and password provided to you for the sandbox environment.
    Once connected, navigate to the directory where you want to upload the screenshots.
    Use the SFTP put command to upload the screenshots from your local machine to the sandbox environment.
    Confirm that the screenshots have been successfully transferred by checking the sandbox directory.
    Once the screenshots are transferred, push the screenshots to GitHub.

Here's an explanation of how SFTP works:
    Connection Establishment:
        The SFTP client initiates a connection to the remote server using the SSH protocol. The server must be configured to support SFTP, and the client must have valid credentials (username and password or SSH key) to authenticate itself.

    Authentication:
        The client sends its credentials to the server for authentication. This step ensures that only authorized users can access the server and perform file transfers.
        Common authentication methods include password-based authentication, public key authentication, or certificate-based authentication.

    Encryption and Secure Channel:
        Once the client is authenticated, SFTP establishes an encrypted channel between the client and the server using the SSH protocol. All data, including file contents, commands, and responses, is encrypted to protect it from eavesdropping and tampering.

    File Operations:
        With the secure channel established, the client can now perform various file operations on the remote server, such as uploading (put) or downloading (get) files, renaming files, creating directories, and deleting files.
        SFTP provides a set of commands similar to traditional FTP, but all the data and commands are transmitted securely through the encrypted channel.

    Data Transfer:
        When a file transfer (upload or download) is initiated, the actual file data is split into smaller packets and encrypted before being sent over the encrypted channel.
        On the receiving end, the data is decrypted and reassembled into the original file.

    Error Handling and Confirmation:
        SFTP includes mechanisms for error handling and confirmation of successful file transfers. If an error occurs during the transfer, the SFTP protocol can detect it, and the client and server can negotiate to retransmit the data.
        The client and server exchange confirmation messages to ensure that the file transfer is complete and successful.

    Connection Termination:
        After the file transfer or other operations are completed, the SFTP client can gracefully close the connection with the server.
        The encrypted channel is closed, and the secure connection is terminated.
