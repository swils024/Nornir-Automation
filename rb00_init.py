from pprint import pprint
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)


def send_command1(device, commands):
    result = {}
    try:
        with ConnectHandler(**device) as telnet:
            # Get the hostname
            hostname = telnet.find_prompt(pattern=r"[A-Za-z]+-\d{3}")
            print(hostname, "-", device["host"], device["port"])
            telnet.enable()
            for command in commands:
                output = telnet.send_command(command)
                result[command] = output
        return result
    except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
        print(error)


if __name__ == "__main__":
    device = [
        {
            "device_type": "cisco_ios_telnet",
            "host": "192.168.1.194",
            "port": 32769,
            "username": "john",
            "password": "demo",
            "secret": "cisco",
        },
        {
            "device_type": "cisco_ios_telnet",
            "host": "192.168.1.194",
            "port": 32770,
            "username": "john",
            "password": "demo",
            "secret": "cisco",
        },
        {
            "device_type": "cisco_ios_telnet",
            "host": "192.168.1.194",
            "port": 32771,
            "username": "john",
            "password": "demo",
            "secret": "cisco",
        },
        {
            "device_type": "cisco_ios_telnet",
            "host": "192.168.1.194",
            "port": 32772,
            "username": "john",
            "password": "demo",
            "secret": "cisco",
        },
        {
            "device_type": "cisco_ios_telnet",
            "host": "192.168.1.194",
            "port": 32773,
            "username": "john",
            "password": "demo",
            "secret": "cisco",
        },
        {
            "device_type": "cisco_ios_telnet",
            "host": "192.168.1.194",
            "port": 32774,
            "username": "john",
            "password": "demo",
            "secret": "cisco",
        },
    ]

    for dev in device:
        # ipdb.set_trace()
        result = send_command1(
            dev, ["configure terminal", "interface GigabitEthernet0/0", "no shutdown"]
        )
