import nmap
import mysql.connector

# Create an instance of the nmap.PortScanner class
nm = nmap.PortScanner()

# Perform a scan on the local area network
nm.scan(hosts='192.168.1.0/24', arguments='-sS')

# Connect to the MySQL server
cnx = mysql.connector.connect(user='username', password='password', host='hostname', database='dbname')
cursor = cnx.cursor()

# Iterate over the hosts found in the scan
for host in nm.all_hosts():
    # Get the results of the scan for the current host
    host_result = nm[host]

    # Iterate over the open ports found for the host
    for port in host_result['tcp']:
        # Get the state and service name for the current port
        port_state = host_result['tcp'][port]['state']
        service_name = host_result['tcp'][port]['name']

        # Insert the data into the MySQL database
        query = "INSERT INTO port_scan (host, port, state, service) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (host, port, port_state, service_name))

# Commit the changes to the database
cnx.commit()

# Close the cursor and connection
cursor.close()
cnx.close()
This program uses the nmap library to perform a scan on the local area network with the 192.168.1.0/24 address range and saves the results to a MySQL database. You need to replace the variables username,password, hostname and dbname with your mysql credentials.
It's important to note that this is a simple example and in practice you should handle exceptions and


