class IPAddress:
    def __init__(self, ipaddress):
        if isinstance(ipaddress, str):
            try:
                parts = [int(part) for part in ipaddress.split('.')]
            except ValueError:
                raise ValueError("Invalid IP address string formate")

        elif isinstance(ipaddress, (list, tuple)):
            parts = list(ipaddress)

        else:
            raise TypeError("The 'ipaddress' argument must be a string, list, or tuple.")

        if len(parts) != 4:
            raise ValueError("An IP address must consst of four parts")

        for part in parts:
            if not isinstance(part, int) or not (0 <= part <= 255):
                raise ValueError(f"Each part of the IP addrss must be an int in the range 0 to 255")

        self.parts = tuple(parts)

    def __str__(self):
        return ".".join(map(str, self.parts))

    def __repr__(self):
        ip_string = str(self)
        return f"IPAddress('{ip_string}')"

try:
    ip1_str = "192.168.1.38"
    ip1 = IPAddress(ip1_str)
    print(f"IP address created from string: {ip1_str}")

    ip2_list = [10, 0, 5, 255]
    ip2 = IPAddress(ip2_list)
    print(f"IP address created from list: {ip2_list}")

    print("")

    print("print(ip1):", ip1)
    print("repr(ip1):", repr(ip1))


    print("print(ip2):", ip2)
    print("repr(ip2):", repr(ip2))

except ValueError as e:
    print(f"Error: {e}")