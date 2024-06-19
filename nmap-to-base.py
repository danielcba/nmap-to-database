import nmap  # Import the nmap library for network scanning
import time  # Import the time library for timing the scan
import mysql.connector  # Import the mysql.connector library for database interaction
from mysql.connector.constants import ClientFlag  # Import ClientFlag constant for connection options
import pyfiglet # Import the pyfiglet library for banner

# Generate the banner
banner = pyfiglet.figlet_format("NmapToMariaDB")
print(banner)

# Define a variable to store the starting time of the scan
starting_point = time.time()

# Create a new PortScanner object from the nmap library
ns = nmap.PortScanner()

# Define the scan parameters:
#  * Target: 192.168.0.1-255 (scans all IPs in the range)
#  * Scan type: TCP SYN scan (-sS)
#  * Version detection intensity: 9 (most aggressive)
#  * Service version detection (-sV)
#  * Only report open ports (-o)
#  * Use promiscuous mode (-PE) for better network visibility
#  * Set scan timing (-T5) to adjust scan speed
ns.scan("192.168.0.1-255 -sC --version-intensity 9 -sS -sV --open -PE -T5")

# Open a file for writing the scan results in CSV format
f = open("/home/username/base-nmap/scan.csv", "w")

# Write the scan results obtained from nmap.csv() function to the file
f.write(ns.csv())

# Close the file after writing
f.close()

# ---------- Database Connection and Data Load ----------
# Establish a connection to the MySQL database
conexion1 = mysql.connector.connect(
    host="localhost",
    user="username",
    passwd="password",  # **WARNING:** Consider not storing credentials directly in code
    database="basenmap",
    allow_local_infile=True,  # Allow loading data from local file (use with caution)
)

# Create a cursor object to execute SQL statements
cursor1 = conexion1.cursor()

# Define the SQL LOAD DATA LOCAL INFILE statement:
#  * Load data from the '/home/dcordoba/Documents/subir-github/base-nmap/scan.csv' file
#  * Into the 'nmap' table in the database
#  * Fields are separated by semicolons (';')
#  * Lines are terminated by newlines ('\n')
#  * Ignore the first line (header row)
cursor1.execute(
    "load data local infile '/home/username/base-nmap/scan.csv' into table nmap FIELDS TERMINATED BY ';' LINES TERMINATED BY '\n' IGNORE 1 LINES"
)

# Commit the changes to the database
conexion1.commit()

# Close the connection and cursor objects
conexion1.close()
cursor1.close()
# ---------- End of Database Section ----------

# Calculate the elapsed time since the scan started
elapsed_time = time.time() - starting_point

# Convert the elapsed time to an integer (seconds)
elapsed_time_int = int(elapsed_time)

# Print a message with the total scan time in seconds with two decimal places
print(f"Scanning completed in {elapsed_time:.2f} seconds")
