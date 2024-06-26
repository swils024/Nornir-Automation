"""
rb12_srapli_parse.py uses the scrapli plugin to run show commands
"""
import sys
import textfsm
from tabulate import tabulate

#template = sys.argv[1]
#output_file = sys.argv[2]
template = "templates/sh_clock.template"
output_file = "output/sh_clock.txt"

with open(template) as f, open(output_file) as output:
    re_table = textfsm.TextFSM(f)
    header = re_table.header
    result = re_table.ParseText(output.read())
    print(result)
    print(tabulate(result, headers=header))
    