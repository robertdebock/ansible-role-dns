# (c) 2013, Michael DeHaan <michael.dehaan@gmail.com>
# (c) 2017 Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = """
    lookup: random_choice
    author: Michael DeHaan <michael.dehaan@gmail.com>
    version_added: "1.1"
    short_description: return random element from list
    description:
        - The 'random_choice' feature can be used to pick something at random. While it's not a load balancer (there are modules for those),
          it can somewhat be used as a poor man's load balancer in a MacGyver like situation.
        - At a more basic level, they can be used to add chaos and excitement to otherwise predictable automation environments.
"""

EXAMPLES = """
- name: Magic 8 ball for MUDs
  debug:
    msg: "{{ item }}"
  with_random_choice:
    - "go through the door"
    - "drink from the goblet"
    - "press the red button"
    - "do nothing"
"""

RETURN = """
  _raw:
    description:
      - random item
"""
import random

from ansible.errors import AnsibleError
from ansible.module_utils._text import to_native
from ansible.plugins.lookup import LookupBase

class LookupModule(LookupBase):

    def run(self, terms=None, servers=None, zones=None, hostvars=None, grouping=None, **kwargs):
        ret = zones
        for zone in zones:
            zone['ns'] = []
            for server in servers:
                zone['ns'].append({'name': f'{hostvars[server]["ansible_hostname"]}.{zone["name"]}.'})
            if not 'records' in zone:
                zone['records'] = []
            for server in servers:
                if hostvars[server]['ansible_default_ipv4']:
                    zone['records'].append({
                        'name': hostvars[server]["ansible_hostname"],
                        'value': hostvars[server]['ansible_default_ipv4']['address']})
                    if grouping:
                        zone['records'].append({
                            'name': grouping,
                            'value': hostvars[server]['ansible_default_ipv4']['address']})
                if hostvars[server]['ansible_default_ipv6']:
                    zone['records'].append({
                        'name': hostvars[server]["ansible_hostname"],
                        'type': 'AAAA',
                        'value': hostvars[server]['ansible_default_ipv6']['address']})
                    if grouping:
                        zone['records'].append({
                            'name': grouping,
                            'type': 'AAAA',
                            'value': hostvars[server]['ansible_default_ipv6']['address']})
        return ret
