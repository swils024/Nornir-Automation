"""
runbook4_srapli_config.py uses the scrapli plugin to run show commands
"""

from nornir import InitNornir
from nornir_scrapli.tasks import send_config, send_configs, send_configs_from_file
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")


def send_config0(task) -> None:
    task.run(
        task=send_config, config="no ip route vrf MGMT 0.0.0.0 0.0.0.0 192.168.199.2"
    )


def send_config1(task) -> None:
    task.run(task=send_config, config="ip scp server enable")


def send_config2(task) -> None:
    config_list = ["interface Gi0/0", "description LAN: MGMT Network"]
    task.run(task=send_configs, configs=config_list)


def send_config3(task) -> None:
    task.run(task=send_configs_from_file, file="config_commands.txt")


if __name__ == "__main__":
    results = nr.run(task=send_config3)
    print_result(results)
