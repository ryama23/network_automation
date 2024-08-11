#read_hosts.py: reads the "hosts.json", which contains site names and IP addresses
#               in the Ansible hosts style but with the json format and puts only 
#               the valid IP addresses in list. It can then be used for other 
#               tasks such as connecting to network devices.

#Standard libraries.
import json, ipaddress
from pathlib import Path

def is_ipaddr(ipaddr):
    """Returns true if 'ipaddr' is a valid IP address."""
    try:
        ipaddress.IPv4Address(ipaddr)
        return True
    except Exception as err:
        #print(err)
        return False

def is_site(hosts, site):
    """Returns true if 'site' is a valid site."""
    if site in hosts.keys():
        return True
    else:
        return False

def get_ipaddr(hosts, site, ipaddrs):
    """Puts valid IP addresses in the 'ipaddrs' list."""
    for value in hosts[site]:
        if is_ipaddr(value):
            ipaddrs.append(value)
        elif is_site(hosts, value):
            #Recursively searches valid IP addresses.
            get_ipaddr(hosts, value, ipaddrs)
        else:
            print(f"{value} is neither a valid IP address nor a valid site.")

def do_something(ipaddrs):
    """Use the list of IP addresses here."""
    pass

def main():
    """Main function."""

    #Read the hosts file.
    contents = Path('hosts.json').read_text()
    hosts = json.loads(contents)

    #Define the site to look for IP addresses.
    site = 'site_all'

    #Empty list to put IP addresses.
    ipaddrs = []

    #Call the function.
    get_ipaddr(hosts, site, ipaddrs)

    #Use the IP addresses to do something useful.
    do_something(ipaddrs)

if __name__ == "__main__":
    main()