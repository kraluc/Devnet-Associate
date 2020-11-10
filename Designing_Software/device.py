from Designing_Software.toolbox import generate_device_name, is_ipv4_address

class Interface:
    def __init__(self, name, address):
        self.name = name
        self._address = address
        self.state = "Down"

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if not is_ipv4_address(value):
            raise ValueError(f">> {value} is not a valid ipv4 address")
        self._address = value

    def __repr__(self):
        return str(vars(self))


class Device:
    def __init__(self, hostname):
        self.hostname = hostname
        self.motd = None
        self.interface = None

    def show(self, p = None):
        if not p:
            # "return dict of instance attributes
            # {'hostname': 'dev1', 'motd': None}"
            return str(vars(self))
        elif hasattr(self, p):
            return (getattr(self, p))
        else:
            return f">> no attribute '{p}'"


class Router(Device):
    pass
