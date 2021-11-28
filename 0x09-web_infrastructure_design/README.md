# 0. Simple web stack

**What is a server:** Bundled components that process requests and transfer data. Provides functionality to other clients.
**What is the role of the domain name:** Provide easily recognizable and memorable names to numerically addressed Internet resources (Abstraction).
**What type of DNS record www is in www.foobar.com:** www is a subdomain that identifies addresses as websites, an alias, in consequence is a CNAME DNS Record.
**What is the role of the web server:** Display website content. Stores, process and deliver webpages. Serves content using HTTP protocol
**What is the role of the application server:** Part of the Web Server that handles the dynamic content of the website that web server can't, and that can use many protocols to serve content.
**What is the role of the database:** Help permanently storing all the necessary data and deliver this data to the authorized users when requested. 
**What is the server using to communicate with the computer of the user requesting the website:**
TCP/IP - HTTP
## Issues with this infrastructure:
**SPOF:** If a part of the infraestructure crashes and causes the entire system to stops, that part is called a Single Point Of Failure. In this model the SPOF are: Router, DNS Server, Web Server, Application Server and Database Server.

