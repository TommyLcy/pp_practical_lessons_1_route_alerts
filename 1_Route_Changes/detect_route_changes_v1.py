#!/usr/bin/env python

from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result
nr = InitNornir()

result = nr.run(task=netmiko_send_command, command_string="show ip route")
print_result(result)


