"""
runbook3_srapli_show.py uses the scrapli plugin to run show commands
"""

from nornir import InitNornir
from nornir_scrapli.tasks import (
    send_command,
    send_commands,
    send_commands_from_file,
    send_interactive,
)
from nornir_utils.plugins.functions import print_result

RB_TIMER = "show archive config rollback timer"
ROUTE = "show run | include ip route"
CONFIRM = "configure confirm"
CANCEL = "configure revert now"
SH_SCP = "show run | include ip scp server enable"
TCL_PING = "tclsh ping.tcl"
ARC = "show run | include archive"
COMMIT_FLASH = "copy running-config startup-config"
SH_EEM = "show event manager policy registered"

nr = InitNornir(config_file="config.yaml")


def interactive1(task) -> None:
    commands = [
        ("debug ip icmp", f"{task.host}#"),
        ("ping vrf MGMT", "Protocol [ip]:"),
        ("ip", "Target IP address:"),
        ("192.168.1.254", "Repeat count [5]:"),
        ("5", "Datagram size [100]:"),
        ("100", "Timeout in seconds [2]:"),
        ("2", "Extended commands [n]:"),
        ("n", "Sweep range of sizes [n]:"),
        ("n", f"{task.host}#"),
        ("undebug all", f"{task.host}#"),
        ("send log 6 Configured by scrapli interative prompt", f"{task.host}"),
    ]
    task.run(task=send_interactive, interact_events=commands)


def interactive2(task) -> None:
    commands = [
        ("configure terminal", f"{task.host}(config)"),
        ("no ip domain lookup", f"{task.host}(config)"),
        ("end", f"{task.host}"),
        ("send log 6 Configured by scrapli interative prompt ", f"{task.host}"),
    ]
    task.run(task=send_interactive, interact_events=commands)


def prompt() -> str:
    commands = input("Enter comma-separated commands:")
    return commands.split(",")


def show_command0(task) -> None:
    for cmd in command_list:
        task.run(task=send_command, command=cmd)


def show_command1(task) -> None:
    task.run(task=send_command, command=SH_EEM)


def show_command2(task) -> None:
    cmd_list = ["show ntp associations", "show ntp status"]
    for cmd in cmd_list:
        task.run(task=send_command, command=cmd)


def show_command3(task) -> None:
    cmd_list = ["show ntp associations", "show ntp status"]
    task.run(task=send_commands, commands=cmd_list)


def show_command4(task) -> None:
    task.run(task=send_commands_from_file, file="show_commands.txt")


def parse_result1(task) -> None:
    result = task.run(task=send_command, command="show version")
    task.host["facts"] = result.scrapli_response.genie_parse_output()


if __name__ == "__main__":
    # Change to 'command_list = prompt()' when calling show_command0
    command_list = None
    results = nr.run(task=show_command1)
    print_result(results)
