"""
rb10_srapli_save.py uses the scrapli plugin to run show commands
"""

from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

COMMIT_FLASH = "copy running-config startup-config"

nr = InitNornir(config_file="config.yaml")


def show_command(task, preset) -> None:
    task.run(task=send_command, command=preset)


if __name__ == "__main__":
    results = nr.run(task=show_command, preset=COMMIT_FLASH)
    print_result(results)
