## Purpose of the Script

This script automates the process of scanning a network to identify connected devices and the services they are running, and then stores these results in a database for later analysis and query. It is useful for network administrators and computer security professionals who need to monitor and manage network infrastructure efficiently.

### Key Script Functions

1. **Network Scan**:

- Use `nmap`, a powerful network scanning tool, to search all devices on a specific network and detect the services and software versions they are running.
- Scanning covers a range of IP addresses and uses advanced techniques to identify active services and software versions with high accuracy.

2. **Generation of Results**:

- Scan results are saved in a file in CSV (comma separated values) format, which makes it easy to organize and analyze the collected data.

3. **Database Storage**:

- Connects to a MariaDB database and loads the scan results into a specific table.
- Storing the results in a database allows for quick and efficient queries, and facilitates integration with other analysis and reporting tools.

### Script Benefits

- **Automation**: The script automates the entire process, from scanning to data storage, saving time and reducing human errors.
- **Continuous Monitoring**: Can be run periodically to maintain an updated view of the network, helping to detect unauthorized changes or potential problems.
- **Security Analysis**: Helps identify services and software versions on the network that could be vulnerable, facilitating the management of security patches and updates.
- **Network Inventory**: Provides a detailed inventory of all devices and services on the network, useful for asset management and capacity planning.

### Typical Use

1. **Network Administrators**: You can use the script to get an overview of the network infrastructure, identify devices and services, and maintain an up-to-date inventory.
2. **Security Professionals**: They can use the data to perform security assessments, identify possible vulnerabilities and plan corrective actions.
3. **Auditors**: They can use the script as part of network audits to verify compliance with security policies and regulations.

### Security Considerations

- **Credential Management**: It is important not to store credentials directly in the code. It is recommended to use safe environment variables or configuration files.
- **Permissions and Access**: Ensure that only authorized personnel can run the script and access the stored results.

### Result
![image](https://github.com/danielcba/nmap-to-database/assets/157246808/bd9d888d-35d8-4111-97c5-3aed501ae9ff)

---

This script is a powerful and versatile tool for network management and security, providing critical information in an automated and efficient manner.
