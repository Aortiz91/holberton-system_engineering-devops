# 0. Simple web stack

**What is a server:** <p>Bundled components that process requests and transfer data. Provides functionality to other clients.

**What is the role of the domain name:** <p>Provide easily recognizable and memorizable names to numerically addressed Internet resources (Abstraction).

**What type of DNS record www is in www.foobar.com:** <p>www is a subdomain that identifies addresses as websites, an alias, in consequence is a CNAME DNS Record.

**What is the role of the web server:** <p>Display website content. Stores, process and deliver webpages. Serves content using HTTP protocol

**What is the role of the application server:** <p>Part of the Web Server that handles the dynamic content of the website that web server can't, and that can use many protocols to serve content.

**What is the role of the database:**<p> Help permanently storing all the necesary data and deliver this data to the authorized users when requested. 

**What is the server using to communicate with the computer of the user requesting the website:**
TCP/IP - HTTP
## Issues with this infrastructure:
**SPOF:** <p>If a part of the infraestructure crashes and causes the entire system to stops, that part is called a Single Point Of Failure. In this model the SPOF are: Router, DNS Server, Web Server, Application Server and Database Server.



# 1. Distributed web infrastructure
**For every additional element, why you are adding it**
<p>   DATABASE MASTER: A second database was already requested but I also need a Master Database which will receive the updates from the web/app server and replicate this to the slave databases from which the each web/app server will read data.
    
**What distribution algorithm your load balancer is configured with and how it works**
<p>
ROUND ROBIN ALGORITHM - , the first client to connect is sent to the first server, the second client goes to the second server, the third client goes back to the first server, the fourth client back to the second server, and so on.
    
**Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both**
<p>

An active-active setup is typically made up of at least two nodes, both actively running the same kind of service simultaneously. In an active-passive setup the passive (failover) server serves as a backup that's ready to take over as soon as the active (primary) server gets disconnected or is unable to serve.
    

**How a database Primary-Replica (Master-Slave) cluster works**
    <p> Master-slave replication enables data from one database server (the master) to be replicated to one or more other database servers (the slaves). The master logs the updates, which then ripple through to the slaves.
    

**What is the difference between the Primary node and the Replica node in regard to the application:**<p> Primary and Replica nodes are created for security purposes but both handle the exact same information.
