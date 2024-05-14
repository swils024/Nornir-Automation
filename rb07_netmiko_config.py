"""
runbook7_netmiko_config.py uses the netmiko plugin to create config
"""

from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")


def send_config1(task) -> None:
    config_list = ["interface GigabitEthernet0/0", "description *** MGMT Network ***"]
    task.run(task=netmiko_send_config, config_commands=config_list)


def send_config2(task) -> None:
    task.run(task=netmiko_send_config, config_file="config_commands.txt")


if __name__ == "__main__":
    results = nr.run(task=send_config2)
    print_result(results)
