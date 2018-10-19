dns
=========

[![Build Status](https://travis-ci.org/robertdebock/ansible-role-dns.svg?branch=master)](https://travis-ci.org/robertdebock/ansible-role-dns)

Ability to configure DNS and records.

[Unit tests](https://travis-ci.org/robertdebock/ansible-role-dns) are done on every commit and periodically.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-dns/issues)

To test this role locally please use [Molecule](https://github.com/metacloud/molecule):
```
pip install molecule
molecule test
```
There are many scenarios available, please have a look in the `molecule/` directory.

Context
--------
This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/drawings/artifacts/dns.png "Dependency")

Requirements
------------

Bootstrap a system (many flavors) to use Ansible, likely the first role to depend on.
Access to internet to download ftp://ftp.internic.net/domain/named.root.

Role Variables
--------------

Have a look at defaults/main.yml:
```
dns_zones:
  - name: example.com
    ttl: 3600
    ns:
    - name: dns1.example.com.
    - name: dns2.example.com.
    mx:
    - name: mail1.example.com.
      priority: 10
    - name: mail2.example.com.
      priority: 20
    records:
    - name: www
      ttl: 60
      value: 127.0.0.1
    - name: dns1
      value: 127.0.0.1
    - name: dns2
      value: 127.0.0.1
    - name: mail1
      value: 127.0.0.1
    - name: mail2
      value: 127.0.0.1
```
- zones.name (example.com) is mandatory to identify the domain.
- zones.name.ttl (3600) is optional, defaults to 604800
- zones.name.ns is optional for reversed (in-addr.arpa) zones, but mandatory for regular zones.
- zones.name.mx is optional.
- zones.name.records is optional and contains a list of records.
- zones.name.records.name is manadory when adding a host.
- zones.name.records.name.type is optional, defaults to "A", other values may be: TXT or CNAME.

if you set "dns_caching_dns" (to any value) your dns server will act as a caching nameserver.

Dependencies
------------

You can use this role to ensure your system is prepared.

- [robertdebock.bootstrap](https://travis-ci.org/robertdebock/ansible-role-bootstrap)

Compatibility
-------------

This role has been tested against the following distributions and Ansible version:

|distribution|ansible 2.4|ansible 2.5|ansible 2.6|
|------------|-----------|-----------|-----------|
|alpine-edge|yes|yes|yes|
|alpine-latest|yes|yes|yes|
|archlinux|yes|yes|yes|
|centos-6|yes|yes|yes|
|centos-latest|yes|yes|yes|
|debian-latest|yes|yes|yes|
|debian-stable|yes|yes|yes|
|fedora-latest|yes|yes|yes|
|fedora-rawhide|yes|yes|yes|
|opensuse-leap|yes|yes|yes|
|opensuse-tumbleweed|yes|yes|yes|
|ubuntu-artful|yes|yes|yes|
|ubuntu-latest|yes|yes|yes|

Example Playbook
----------------

```
---
- hosts: servers

  roles:
    - role: robertdebock.bootstrap
    - role: robertdebock.dns
      dns_zones:
        - name: example.com
        ns:
          - name: ns1.example.com.
        mx:
          - name: mail1.example.com.
        priority: 10
          - name: mail2.example.com.
        priority: 20
        records:
          - name: www
        value: 192.168.1.1
          - name: ns1
        value: 192.167.1.1
          - name: mail1
        value: 192.168.1.1
          - name: mail2
        value: 192.168.1.2
```
Install this role using `galaxy install robertdebock.dns`.

License
-------

Apache License, Version 2.0

Author Information
------------------

[Robert de Bock](https://robertdebock.nl/) <robert@meinit.nl>
