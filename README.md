dns
=========

Ability to configure DNS and records.

Requirements
------------

Access to a repository that provides the package for bind.
Access to internet to download ftp://ftp.internic.net/domain/named.root.

Role Variables
--------------

Have a look at defaults/main.yml:
```
zone: example.com
records:
  - www:
    type: A
    value: 127.0.0.1
```

- type can be: A or CNAME

Dependencies
------------

- robertdebock.bootstrap

Example Playbook
----------------

```
- hosts: servers
  roles:
    - robertdebock.dns
```

License
-------

Apache License, Version 2.0

Author Information
------------------

Robert de Bock <robert@meinit.nl>
