# dns

Install and configure dns on your system.

|Travis|GitHub|Quality|Downloads|
|------|------|-------|---------|
|[![travis](https://travis-ci.com/robertdebock/ansible-role-dns.svg?branch=master)](https://travis-ci.com/robertdebock/ansible-role-dns)|[![github](https://github.com/robertdebock/ansible-role-dns/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-dns/actions)|[![quality](https://img.shields.io/ansible/quality/21885)](https://galaxy.ansible.com/robertdebock/dns)|[![downloads](https://img.shields.io/ansible/role/d/21885)](https://galaxy.ansible.com/robertdebock/dns)|

## Example Playbook

This example is taken from `molecule/resources/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: Converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.dns
```

The machine may need to be prepared using `molecule/resources/prepare.yml`:
```yaml
---
- name: Prepare
  hosts: all
  gather_facts: no
  become: yes

  roles:
    - role: robertdebock.bootstrap
    - role: robertdebock.core_dependencies
```

For verification `molecule/resources/verify.yml` run after the role has been applied.
```yaml
---
- name: Verify
  hosts: all
  become: yes
  gather_facts: yes

  vars:
    _nslookup_package:
      Alpine: bind-tools
      Archlinux: dnsutils
      Debian: dnsutils
      RedHat: bind-utils

    nslookup_package: "{{ _nslookup_package[ansible_os_family] }}"

  tasks:
    - name: install nslookup
      package:
        name: "{{ nslookup_package }}"
        state: present

    - name: test resolving www.example.com
      command: nslookup www.example.com 127.0.0.1
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## Role Variables

These variables are set in `defaults/main.yml`:
```yaml
---
# defaults file for dns

# Should the DNS server be a caching DNS server?
dns_caching_dns: yes

# A list of zones and properties per zone.
dns_zones:
  - name: localhost
    soa: localhost
    serial: 1
    refresh: 604800
    rety: 86400
    expire: 2419200
    ttl: 604800
    records:
      - name: "@"
        type: NS
        value: localhost.
      - name: "@"
        value: 127.0.0.1
      - name: "@"
        type: AAAA
        value: ::1

  - name: 127.in-addr.arpa
    ttl: 604800
    records:
      - name: "@"
        type: NS
        value: localhost.
      - name: 1.0.0
        type: PTR
        value: localhost.

  - name: 0.in-addr.arpa
    records:
      - name: "@"
        type: NS
        value: localhost.

  - name: 255.in-addr.arpa
    records:
      - name: "@"
        type: NS
        value: localhost.

  - name: example.com
    ttl: 604800
    ns:
      - name: dns1.example.com.
      - name: dns2.example.com.
    mx:
      - name: mail1.example.com.
        priority: 10
      - name: mail2.example.com.
        priority: 20
    records:
      - name: dns1
        value: 127.0.0.1
      - name: dns2
        value: 127.0.0.1
      - name: www
        value: 127.0.0.1
      - name: dns1
        value: 127.0.0.1
      - name: dns2
        value: 127.0.0.1
      - name: mail1
        value: 127.0.0.1
      - name: mail2
        value: 127.0.0.1

  - name: forwarded.example.com
    type: forward
    dns_zone_forwarders:
      - 1.1.1.1
      - 8.8.8.8

# An optional list of acls to allow recursion. ("any" and "none" are always available.)
dns_allow_recursion:
  - none

# An optional list of IPv4 on which the DNS server will listen. ("any" and "none" are always available.)
dns_options_listen_on:
  - 'any'

# A optional list of IPv6 on which the DNS server will listen. ("any" and "none" are always available.)
dns_options_listen_on_v6:
  - 'any'

# An optional list of IP which are allowed to query the server. ("any" and "none" are always available.)
# Default: "any"
# dns_options_allow_query:
#  - 'any'
#  - '127.0.0.1'

# An optional list of IP which are allowed to run a AXFR query. ("any" and "none" are always available.)
# Default: "none"
# dns_options_allow_transfer:
#   - 'none'
#   - '172.16.0.1'

# An optional setting to congifure the path where the pid file will be created.
# dns_pid_file: '/var/run/named/named.pid'

# An optional setting to forward traffic to other DNS servers.
# dns_options_forwarders:
#   - 1.1.1.1
#   - 8.8.8.8

# Another example thanks to @blaisep.
# dns_zones:
#   - name: lab.controlplane.info
#     ttl: 600
#     ns:
#       - name: ns.lab.controlplane.info.
#     mx:
#       - name: mail1.lab.controlplane.info.
#         priority: 10
#       - name: mail2.lab.controlplane.info.
#         priority: 20
#     records:
#       - name: ns
#         value: 192.168.254.27
#       - name: git
#         value: 192.168.254.19
#       - name: dl380
#         value: 192.168.254.27
#       - name: mail1
#         value: 192.168.123.123
#       - name: mail2
#         value: 192.168.123.123
#   - name: forwarded.lab.controlplane.info
#     ns:
#       - name: forwarded.lab.controlplane.info.
#     records:
#       - name: ns
#         value: 192.168.254.27
#       - name: "@"
#         value: 192.168.123.123
#     dns_zone_forwarders:
#       - 9.9.9.9
#       - 8.8.8.8
```

## Requirements

- Access to a repository containing packages, likely on the internet.
- A recent version of Ansible. (Tests run on the current, previous and next release of Ansible.)

The following roles can be installed to ensure all requirements are met, using `ansible-galaxy install -r requirements.yml`:

```yaml
---
- robertdebock.bootstrap
- robertdebock.core_dependencies

```

## Context

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/drawings/artifacts/dns.png "Dependency")

## Compatibility

This role has been tested on these [container images](https://hub.docker.com/):

|container|tags|
|---------|----|
|alpine|all|
|amazon|2018.03|
|el|7, 8|
|debian|buster, bullseye|
|fedora|31, 32|
|ubuntu|focal, bionic, xenial|

The minimum version of Ansible required is 2.8 but tests have been done to:

- The previous version, on version lower.
- The current version.
- The development version.

## Exceptions

Some variarations of the build matrix do not work. These are the variations and reasons why the build won't work:

| variation                 | reason                 |
|---------------------------|------------------------|
| EL | RedHat does not supply `bind` without a subscription. |
| openSuse | Some tasks will not get idempotent. |


## Testing

[Unit tests](https://travis-ci.com/robertdebock/ansible-role-dns) are done on every commit, pull request, release and periodically.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-dns/issues)

Testing is done using [Tox](https://tox.readthedocs.io/en/latest/) and [Molecule](https://github.com/ansible/molecule):

[Tox](https://tox.readthedocs.io/en/latest/) tests multiple ansible versions.
[Molecule](https://github.com/ansible/molecule) tests multiple distributions.

To test using the defaults (any installed ansible version, namespace: `robertdebock`, image: `fedora`, tag: `latest`):

```
molecule test

# Or select a specific image:
image=ubuntu molecule test
# Or select a specific image and a specific tag:
image="debian" tag="stable" tox
```

Or you can test multiple versions of Ansible, and select images:
Tox allows multiple versions of Ansible to be tested. To run the default (namespace: `robertdebock`, image: `fedora`, tag: `latest`) tests:

```
tox

# To run CentOS (namespace: `robertdebock`, tag: `latest`)
image="centos" tox
# Or customize more:
image="debian" tag="stable" tox
```

## License

Apache-2.0


## Author Information

[Robert de Bock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
