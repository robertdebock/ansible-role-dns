ansible-role-dns
=========

Ability to configure DNS and records.

Requirements
------------

Bootstrap a system (many flavors) to use Ansible, likely the first role to depend on.
Access to internet to download ftp://ftp.internic.net/domain/named.root.

Role Variables
--------------

Have a look at defaults/main.yml:
```
zones:
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

if you set "caching_dns" (to any value) your dns server will act as a caching nameserver.

Dependencies
------------

- robertdebock.ansible-role-bootstrap

Example Playbook
----------------

```
---
- hosts: servers

  roles:
    - role: robertdebock.ansible-role-dns
      zones:
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

License
-------

Apache License, Version 2.0

Author Information
------------------

Robert de Bock <robert@meinit.nl>
