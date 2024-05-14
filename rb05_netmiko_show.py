"""
runbook5_netmiko_show.py uses the netmiko plugin to run show commands
"""

from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")


def show_command1(task) -> None:
    task.run(
        task=netmiko_send_command,
        command_string="show interfaces description | include up",
    )


def show_command2(task) -> None:
    cmd_list = [
        "show interfaces description | include up",
        "show version | include uptime",
        "show logging | include %SYS-5-CONFIG_I",
        "show archive config differences",
    ]
    for cmd in cmd_list:
        task.run(task=netmiko_send_command, command_string=cmd)


if __name__ == "__main__":
    results = nr.run(task=show_command2)
    print_result(results)
