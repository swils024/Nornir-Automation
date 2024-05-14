from nornir import InitNornir
from nornir_scrapli.tasks import send_commands
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")


def ping(task) -> None:
    cmd_list = [
        "ping vrf MGMT 192.168.1.193",
        "ping vrf MGMT 192.168.1.194",
        "ping vrf MGMT 192.168.1.195",
        "ping vrf MGMT 192.168.1.196",
        "ping vrf MGMT 192.168.1.197",
        "ping vrf MGMT 192.168.1.198",
        "ping vrf MGMT 192.168.1.199",
        "ping vrf MGMT 192.168.1.200",
        "ping vrf MGMT 192.168.1.254",
        "ping vrf MGMT 8.8.8.8",
        "ping vrf MGMT 8.8.4.4",
    ]
    task.run(task=send_commands, commands=cmd_list)


if __name__ == "__main__":
    results = nr.run(task=ping)
    print_result(results)
