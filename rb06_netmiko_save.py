"""
runbook6_netmiko_save.py uses the netmiko plugin to save config
"""

from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_save_config
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")


def save_config(task) -> None:
    task.run(task=netmiko_save_config)


if __name__ == "__main__":
    results = nr.run(task=save_config)
    print_result(results)
