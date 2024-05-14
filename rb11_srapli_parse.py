"""
rb11_srapli_parse.py uses the scrapli plugin to run show commands

pp nr.inventory.hosts["MGMT-196"]["facts"]["version"]
pp nr.inventory.hosts["MGMT-196"]["facts"]["version"]["chassis_sn"]
pp nr.inventory.hosts["MGMT-196"]["facts"]["version"]["uptime"]
"""

from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
from rich import print as rprint


SH_VER = "show version"

nr = InitNornir(config_file="config.yaml")


def parse_result1(task, preset) -> None:
    result = task.run(task=send_command, command=preset)
    task.host["facts"] = result
    # task.host["facts"] = result.scrapli_response.genie_parse_output()


if __name__ == "__main__":
    results = nr.run(task=parse_result1, preset=SH_VER)
    print_result(results)
