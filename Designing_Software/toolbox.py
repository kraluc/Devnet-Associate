import random
import string


def generate_device_name(device, description):
    """ This function generates a name
    of a VNF running in RTP datacenter
    """
    datacenter = 'RTP'
    devices = {'firewall': 'Cisco_ASAv', 'router': 'Cisco_CSR-1000v'}

    device_type = devices[device]
    name = f"{device_type}--{description}__{datacenter}"

    return name


def is_ipv4_address(ip):
    """ Return True if ipv4 address,
    False if not
    """
    octets = ip.split('.')

    if len(octets) != 4:
        return False
    elif any(not octet.isdigit() for octet in octets):
        return False
    elif any(int(octet) < 0 for octet in octets):
        return False
    elif any(int(octet) > 255 for octet in octets):
        return False

    return True


if __name__ == "__main__":
    characters = string.ascii_lowercase
    description = ''.join(random.choice(characters) for i in range(10))
    device = ['router', 'firewall'][random.randrange(0,2)]
    print(generate_device_name(device, description))