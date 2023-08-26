# www.foobar.com Infrastructure

This README explains the process from the client browser to the servers at www.foobar.com.
It covers the enhanced infrastructure to make www.foobar.com secure, serve encrypted traffic, and enable monitoring.

## Infrastructure Overview

We have added several components to the infrastructure to improve security, encryption, and monitoring.

### Components Added

- **Firewalls (3)**: Firewalls act as protective barriers, filtering incoming and outgoing traffic to ensure only authorized communication occurs and to guard against malicious access.

- **SSL Certificate**: An SSL certificate has been installed. It secures the website by encrypting data exchanged between clients and servers, ensuring data privacy and integrity.

- **Monitoring Clients (6)**: Monitoring clients serve as data collectors. They gather information for monitoring services like Sumo Logic, providing insights into server and application performance, and helping to identify and address issues proactively.

### Specifics About the Infrastructure

#### Firewalls

**Why**: Firewalls are added to:
- Control incoming and outgoing traffic, permitting only necessary and authorized communication.
- Enhance security by safeguarding against unauthorized access attempts and malicious traffic.
- Isolate sensitive components from direct external access.

#### Serving Traffic Over HTTPS

**Why**: We serve traffic over HTTPS to:
- Encrypt data transmitted between clients and servers, ensuring confidentiality and data integrity.
- Provide a secure browsing experience for users, protecting sensitive information.
- Prevent eavesdropping and man-in-the-middle attacks.

#### Monitoring

**Why**: Monitoring is essential for:
- Keeping an eye on server and application performance.
- Detecting issues early and responding to them proactively, minimizing downtime.
- Collecting and analyzing data to gain insights into system behavior and make informed decisions.

#### Monitoring Data Collection

**How**: Monitoring clients (data collectors) collect data by:
- Capturing logs, metrics, and events from servers and applications.
- Transmitting this data to monitoring services like Sumo Logic for analysis.
- Generating alerts and reports based on predefined criteria to flag unusual behavior.

#### Monitoring Web Server QPS (Queries Per Second)

**How**: To monitor web server QPS, you can set up monitoring tools to:
- Track the number of incoming HTTP requests per second.
- Analyze server response times and error rates.
- Establish thresholds and alerts that notify you when QPS exceeds predefined limits.

### Issues with the Infrastructure

#### Terminating SSL at the Load Balancer Level

**Issue**: Terminating SSL at the load balancer level poses problems because:
- It necessitates the SSL/TLS decryption and encryption process at the load balancer, potentially overloading it.
- It may expose unencrypted traffic between the load balancer and application servers, posing a security risk.

**Mitigation**: Implement SSL/TLS termination at the application servers to distribute the SSL/TLS workload evenly and securely.

#### Only One MySQL Server Accepting Writes

**Issue**: Having only one MySQL server capable of accepting write operations is problematic because:
- It creates a single point of failure (SPOF) for write operations. If this server fails, write operations become unavailable.
- It limits write scalability and can lead to performance bottlenecks.

**Mitigation**: Implement a Primary-Replica (Master-Slave) MySQL cluster with multiple replica nodes to provide redundancy, scalability, and fault tolerance for write operations.

#### Servers with All the Same Components

**Issue**: Servers with identical components (database, web server, application server) might be problematic because:
- They lack component isolation, making the entire server vulnerable to issues with one component.
- They limit the ability to scale specific components independently based on their resource requirements.

**Mitigation**: Consider separating components onto different servers or containers to allow for more fine-grained scalability and isolation, improving system stability and resource utilization.

## Connection Process (Using Sample IP Addresses)

1. **Client Request**: A user's browser (e.g., IP: 203.0.113.1) initiates an HTTPS request to www.foobar.com.(8.8.8.8)

2. **Firewall Check (Firewall 1)**: The request is first checked by the firewall (e.g., Firewall 1, IP: 192.168.1.101) to ensure it meets security criteria. Authorized traffic passes through.

3. **Load Balancer**: Traffic is directed to the load balancer (IP: 192.168.1.102) to distribute requests evenly.

4. **SSL/TLS Encryption (Load Balancer)**: The load balancer, which is also responsible for SSL termination, decrypts the HTTPS request, processes it, and re-encrypts the response before forwarding it.

5. **Web Server & Application Server (Server)**: The load balancer routes the request to one of the application servers (e.g., Server 1, IP: 192.168.1.103). Both web and application servers respond to the request.

6. **SSL/TLS Encryption (Load Balancer)**: The load balancer re-encrypts the response and sends it back to the client.

7. **Firewall Check (Firewall 1)**: The response passes through the firewall before reaching the client, ensuring ongoing security.

8. **Monitoring Clients**: Monitoring clients (e.g., IP: 192.168.1.104) collect data on server and application performance and transmit it to the monitoring service (Sumo Logic) for analysis.

This process ensures secure, encrypted, and monitored communication between the client browser and the servers at www.foobar.com.
