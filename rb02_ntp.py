"""
runbook2_ntp.py example using Nornir
"""

from nornir import InitNornir
from nornir_scrapli.tasks import send_config
from nornir_utils.plugins.functions import print_result


nr = InitNornir(config_file="config.yaml")


def ntp_config(task):
    task.run(task=send_config, config=f'ntp server vrf MGMT {task.host["ntp_server"]}')


print("===================================")
print("HOSTS")
print("===================================")

[
    print(f"{host} in platform {nr.inventory.hosts[host].platform}")
    for host in nr.inventory.hosts
]

results = nr.run(task=ntp_config)
print_result(results)
