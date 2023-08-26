# Enhanced Infrastructure for www.foobar.com
 We have enhanced the infrastructure to address the requirements and improve reliability and scalability:

## Components Added

### Servers (2)

- **Why**: We've added an additional 2 servers for redundancy and high availability. If one server fails, the other can take over.

### Load Balancer (HAProxy)

- **Why**: The load balancer takes up one server and distributes incoming traffic across remaining servers, ensuring that the infrastructure can handle higher traffic loads and adding redundancy.

- **Distribution Algorithm**: We configure HAProxy with a round-robin distribution algorithm. It evenly distributes requests to each server in a circular manner.

- **Active-Active Setup**: The load balancer is configured in an Active-Active setup. All web servers are actively serving traffic. This ensures that both servers are utilized, improving performance and fault tolerance. In Active-Active, both servers handle requests simultaneously.

### Application Files (Your Code Base) & Database (MySQL)

- **Why**:  All servers continue serving the same content for redundancy with the databases connfigured in a master replica setup

## Specifics About the Infrastructure

### Single Point of Failure (SPOF)

**Issue**: In this setup, there are still single points of failure:
- **Load Balancer**: If the load balancer fails, it can disrupt traffic distribution.
- **Web Server and Application Server**: If either server fails, it can impact availability.

**Mitigation**: To address these SPOF concerns, we might consider:
- Adding redundancy for the load balancer (e.g., use a secondary load balancer).
- Implementing monitoring and automated failover mechanisms to detect server failures and route traffic accordingly.
- Implementing regular backups and a disaster recovery plan.

### Security Issues (No Firewall, No HTTPS)

**Issue**: Security measures like firewalls and HTTPS are missing.
- **No Firewall**: Without a firewall, your infrastructure is more susceptible to unauthorized access and attacks.
- **No HTTPS**: Not using HTTPS puts data transmission between clients and servers at risk of interception or tampering.

**Mitigation**: Improve security by:
- Implementing a firewall to control traffic and protect against unauthorized access.
- Enabling HTTPS with SSL/TLS certificates to encrypt data in transit, enhancing data security and user trust.

### Monitoring

**Issue**: There is no monitoring in place to track the health and performance of servers and applications.

**Mitigation**: Implement a monitoring solution (e.g., Prometheus, Nagios, or a cloud-based solution) to:
- Continuously monitor server health, resource utilization, and application performance.
- Set up alerts to detect issues proactively and respond promptly.

## Database Primary-Replica (Master-Slave) Cluster

### How It Works

In a Primary-Replica (Master-Slave) database cluster:
- The **Primary node (Master)** is the primary database server for read and write operations. It receives the queries from the application and conducts the read/write operation and updates a log file of
    the changes which the replica servers regularly check for and update their records accordingly.
- The **Replica nodes (Slaves)** replicate data from the Primary and can be used for read operations, improving read scalability and redundancy.
- Write operations go to the Primary, ensuring data consistency.

### Difference Between Primary and Replica in Regard to the Application

- **Primary Node**: The Primary handles both read and write operations. It's responsible for maintaining data consistency and integrity, making it crucial for the application's core functionality.
- **Replica Node**: Replica nodes are primarily used for read operations. They help offload read traffic from the Primary, improving read performance and scalability. However, Replica nodes are read-only and do not accept write operations directly.
