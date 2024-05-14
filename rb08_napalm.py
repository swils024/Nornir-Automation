"""
runbook8_napalm.py call napalm functions
"""

from nornir import InitNornir
from nornir_napalm.plugins.tasks import (
    napalm_get,
    napalm_ping,
    napalm_get,
    napalm_configure,
    napalm_confirm_commit,
)
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")


def ping(task) -> None:
    task.run(task=napalm_ping, dest="8.8.4.4", vrf="MGMT")


def confirm_commit1(task) -> None:
    task.run(task=napalm_confirm_commit, dry_run=False)


def get1(task) -> None:
    task.run(task=napalm_get, getters=["get_users"])


def get2(task) -> None:
    getters_list = [
        "get_facts",
        "get_environment",
        "get_interfaces",
        "get_interfaces_ip",
    ]
    task.run(task=napalm_get, getters=getters_list)


def configure1(task) -> None:
    task.run(
        task=napalm_configure,
        configuration="ip route vrf MGMT 0.0.0.0 0.0.0.0 192.168.1.254",
        dry_run=False,
    )


def configure2(task) -> None:
    file = "config_commands.txt"
    task.run(task=napalm_configure, filename=file, revert_in=300)


if __name__ == "__main__":
    results = nr.run(task=configure2)
    print_result(results)
