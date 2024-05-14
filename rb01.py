"""
runbook1.py example using Nornir
"""

from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")
print("===================================")
print("HOSTS")
print("===================================")

[
    print(f"{host} in platform {nr.inventory.hosts[host].platform}")
    for host in nr.inventory.hosts
]

results = nr.run(task=send_command, command="who")
print_result(results)
