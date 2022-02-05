IntelMQ Ansible Role
=========

An Ansible Role to install and configure [IntelMQ](https://github.com/certtools/intelmq/), including:
- the [IntelMQ Core](https://github.com/certtools/intelmq),
- the [IntelMQ Manager](https://github.com/certtools/intelmq-manager) (graphical user interface),
- the [IntelMQ API](https://github.com/certtools/intelmq-api) (required for the Manager).

Galaxy Website: https://galaxy.ansible.com/sebix/intelmq

Install this role with:
```bash
ansible-galaxy install sebix.intelmq
```

Requirements
------------

none

Role Variables
--------------

```
intelmq_api_username
intelmq_api_password
```

Dependencies
------------

none

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
      - intelmq

License
-------

CC-BY-NC-SA-4.0

Author Information
------------------

- Sebastian Wagner
- [mailto:sebix@sebix.at](sebix@sebix.at)
- [GitHub: @sebix](https://github.com/sebix)
