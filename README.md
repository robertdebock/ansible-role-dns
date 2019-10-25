dns
=========

<img src="https://docs.ansible.com/ansible-tower/3.2.4/html_ja/installandreference/_static/images/logo_invert.png" width="10%" height="10%" alt="Ansible logo" align="right"/>
<a href="https://travis-ci.org/robertdebock/ansible-role-dns"><img src="https://travis-ci.org/robertdebock/ansible-role-dns.svg?branch=master" alt="Build status" align="left"/></a>

Install and configure dns on your system.

<img src="https://img.shields.io/ansible/role/d/21885"/>
<img src="https://img.shields.io/ansible/quality/21885"/>

Example Playbook
----------------

This example is taken from `molecule/resources/playbook.yml`:
```yaml
---
- name: Converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - robertdebock.dns
```

The machine you are running this on, may need to be prepared.
```yaml
---
- name: Prepare
  hosts: all
  gather_facts: no
  become: yes

  roles:
    - robertdebock.bootstrap
    - robertdebock.core_dependencies
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

Role Variables
--------------

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
    ns:
      - name: dns1.forwarded.example.com.
      - name: dns2.forwarded.example.com.
    records:
      - name: dns1
        value: 127.0.0.1
      - name: dns2
        value: 127.0.0.1
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
```

Requirements
------------

- Access to a repository containing packages, likely on the internet.
- A recent version of Ansible. (Tests run on the current, previous and next release of Ansible.)

The following roles can be installed to ensure all requirements are met, using `ansible-galaxy install -r requirements.yml`:

```yaml
---
- robertdebock.bootstrap
- robertdebock.core_dependencies

```

This role uses the following modules:
```yaml
---
- command
- file
- get_url
- group
- package
- service
- template
- user
```

Context
-------

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/drawings/artifacts/dns.png "Dependency")


Compatibility
-------------

This role has been tested on these [container images](https://hub.docker.com/):

|container|tag|allow_failures|
|---------|---|--------------|
|alpine|latest|no|
|alpine|edge|yes|
|debian|stable|yes|
|debian|unstable|yes|
|debian|latest|no|
|centos|7|no|
|redhat|7|no|
|centos|latest|no|
|redhat|latest|no|
|fedora|latest|no|
|fedora|rawhide|yes|
|opensuse|latest|no|
|ubuntu|rolling|yes|
|ubuntu|devel|yes|
|ubuntu|latest|no|

This role has been tested on these Ansible versions:

- ansible~=2.7
- ansible~=2.8
- git+https://github.com/ansible/ansible.git@devel

The indicator '\~=' means [compatible with](https://www.python.org/dev/peps/pep-0440/#compatible-release). For example 'ansible\~=2.8' would pick the latest ansible-2.8, for example ansible-2.8.6.




Testing
-------

[Unit tests](https://travis-ci.org/robertdebock/ansible-role-dns) are done on every commit and periodically.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-dns/issues)

To test this role locally please use [Molecule](https://github.com/ansible/molecule):
```
pip install molecule
molecule test
```

To test on Amazon EC2, configure [~/.aws/credentials](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/credentials.html) and set a region using `export AWS_REGION=eu-central-1` before running `molecule test --scenario-name ec2`.

There are many specific scenarios available, please have a look in the `molecule/` directory.

License
-------

Apache-2.0


Author Information
------------------

[Robert de Bock](https://robertdebock.nl/)
