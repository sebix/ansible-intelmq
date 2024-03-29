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
    On Debian: Only used if package is to be installed
redirect_mail:
    default: root. Set to `no` to disable
intelmq_runtime:
    the new configuration
intelmq_runtime_clean:
    if the previous configuration should be removed
skip_intelmqctl_check:
    If `intelmqctl check` should be skipped at the end, default: no
skip_intelmqctl_upgrade_config:
    If `intelmqctl upgrade-config` should be skipped at the end, default: no
intelmq_unstable_repository:
    default: false. Set to `true` to use the "unstable" repository
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
- [sebix@sebix.at](mailto:sebix@sebix.at)
- [GitHub: @sebix](https://github.com/sebix)
