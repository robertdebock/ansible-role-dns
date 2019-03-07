dns
=========

[![Build Status](https://travis-ci.org/robertdebock/ansible-role-dns.svg?branch=master)](https://travis-ci.org/robertdebock/ansible-role-dns)

Install and configure dns on your system.

Example Playbook
----------------

This example is taken from `molecule/default/playbook.yml`:
```yaml
---
- name: Converge
  hosts: all
  gather_facts: no
  become: yes
  serial: 30%

  roles:
    - robertdebock.bootstrap
    - robertdebock.dns

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

# An optional setting to forward traffic to other DNS servers.
# dns_options_forwarders:
#   - 1.1.1.1
#   - 8.8.8.8

# To update all packages installed by this roles, set `dns_package_state` to `latest`.
dns_package_state: present

# Some Docker containers do not allow managing services, rebooting and writing
# to some locations in /etc. The role skips tasks that will typically fail in
# Docker. With this parameter you can tell the role to -not- skip these tasks.
dns_ignore_docker: yes

```

Requirements
------------

- Access to a repository containing packages, likely on the internet.
- A recent version of Ansible. (Tests run on the last 3 release of Ansible.)

The following roles can be installed to ensure all requirements are met, using `ansible-galaxy install -r requirements.yml`:

```yaml
---
- robertdebock.bootstrap

```

Context
-------

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/drawings/artifacts/dns.png "Dependency")


Compatibility
-------------

This role has been tested against the following distributions and Ansible version:

|distribution|ansible 2.6|ansible 2.7|ansible devel|
|------------|-----------|-----------|-------------|
|alpine-edge*|yes|yes|yes*|
|alpine-latest|yes|yes|yes*|
|archlinux|yes|yes|yes*|
|centos-6|yes|yes|yes*|
|centos-latest|yes|yes|yes*|
|debian-latest|yes|yes|yes*|
|debian-stable|yes|yes|yes*|
|debian-unstable*|yes|yes|yes*|
|fedora-latest|yes|yes|yes*|
|fedora-rawhide*|yes|yes|yes*|
|opensuse-leap|yes|yes|yes*|
|ubuntu-devel*|yes|yes|yes*|
|ubuntu-latest|yes|yes|yes*|
|ubuntu-rolling|yes|yes|yes*|

A single star means the build may fail, it's marked as an experimental build.

Testing
-------

[Unit tests](https://travis-ci.org/robertdebock/ansible-role-dns) are done on every commit and periodically.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-dns/issues)

To test this role locally please use [Molecule](https://github.com/metacloud/molecule):
```
pip install molecule
molecule test
```

To test on Amazon EC2, configure [~/.aws/credentials](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/credentials.html) and `export AWS_REGION=eu-central-1` before running `molecule test --scenario-name ec2`.

There are many specific scenarios available, please have a look in the `molecule/` directory.

Run the [ansible-galaxy](https://github.com/ansible/galaxy-lint-rules) and [my](https://github.com/robertdebock/ansible-lint-rules) lint rules if you want your change to be merges:

```shell
git clone https://github.com/ansible/ansible-lint.git /tmp/ansible-lint
ansible-lint -r /tmp/ansible-lint/lib/ansiblelint/rules .

git clone https://github.com/robertdebock/ansible-lint /tmp/my-ansible-lint
ansible-lint -r /tmp/my-ansible-lint/rules .
```

License
-------

Apache-2.0


Author Information
------------------

[Robert de Bock](https://robertdebock.nl/) <robert@meinit.nl>
