<!--
SPDX-FileCopyrightText: 2026 Institute for Common Good Technology

SPDX-License-Identifier: CC-BY-NC-SA-4.0
-->

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

Enable piplining, e.g. in you `ansible.cfg`:
```
[connection]
# Required for become_user to work without ACL support on the remote host
pipelining = True
```

The playbook is best tested on Ubuntu 24.04.

To process the RIPE database, about 8 GB of RAM are required.
All other set-up processes require only minimal memory.

Role Variables
--------------

```
intelmq_api_username
intelmq_api_password
    On Debian: Only used if package is to be installed
redirect_mail:
    default: root. Set to `false` to disable
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
checkmk:
    default: false. Set to true to install checkmk monitoring system
autostart:
    default: true. Install `intelmq-autostart` package
catch_emails:
    default: true. Don't send email's out, but use dsmtpd to catch them locally. Keep at true for test systems, disable for production systems
intelmq_optional_dependencies:
    default: true
intelmq_api_username
intelmq_api_password
db_password_intelmq: ""  # best set in secrets
db_password_fody: ""     # best set in secrets
db_password_mailgen: ""  # best set in secrets
ripe_import_countries:
    list of countries to import RIPE data for
    see https://github.com/Intevation/intelmq-certbund-contact/blob/master/README-ripe-import.md
mailgen_formats_dir:
    local path to sync to /etc/intelmq/mailgen/formats/
mailgen_templates_dir:
    local path to sync to /etc/intelmq/mailgen/templates/
certbund_notification_rules_dir:
    local path to sync to /var/lib/intelmq/bots/notification_rules/

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
      vars:
        intelmq_api_username: intelmq
        intelmq_api_password:
        db_password_intelmq:
        db_password_fody:
        db_password_mailgen:
        ripe_import_countries: AT

License
-------

CC-BY-NC-SA-4.0

Author Information
------------------

Institute for Common Good Technology

Funded and supported by [FIRST](https://www.first.org/), the global Forum of Incident Response and Security Teams

Thanks also to Kamil Mankowski, CERT.at, for providing input and help.
