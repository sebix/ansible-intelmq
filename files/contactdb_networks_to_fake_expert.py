#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2025-2026 Institute for Common Good Technology
#
# SPDX-License-Identifier: CC-BY-NC-SA-4.0

"""
Export all addresses from network_automatic table as fake expert configuration
"""

import json
import sys

import psycopg2


CONFIG_FILE = "/etc/intelmq/contactdb-serve.conf"


def load_config(path):
    try:
        with open(path) as f:
            config = json.load(f)
    except FileNotFoundError:
        print(f"Error: config file not found: {path}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: failed to parse config file: {e}", file=sys.stderr)
        sys.exit(1)

    if "libpg conninfo" not in config:
        print("Error: 'libpg conninfo' key missing from config", file=sys.stderr)
        sys.exit(1)

    return config["libpg conninfo"]


def main():
    conninfo = load_config(CONFIG_FILE)

    try:
        conn = psycopg2.connect(conninfo)
    except psycopg2.OperationalError as e:
        print(f"Error: could not connect to database: {e}", file=sys.stderr)
        sys.exit(1)

    try:
        with conn.cursor() as cur:
            cur.execute("SELECT address FROM network_automatic;")
            rows = cur.fetchall()
    except psycopg2.Error as e:
        print(f"Error: database query failed: {e}", file=sys.stderr)
        sys.exit(1)
    finally:
        conn.close()

    addresses = [row[0] for row in rows]
    print(json.dumps({"ip_network": addresses}, indent=4))


if __name__ == "__main__":
    main()
