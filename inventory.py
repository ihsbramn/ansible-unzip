#!/usr/bin/env python

import os
import json

target_host = os.getenv('TARGET_HOST')
ssh_user = os.getenv('SSH_USER')
ssh_pass = os.getenv('SSH_PASS')
ssh_port = os.getenv('SSH_PORT')

inventory = {
    'web_servers': {
        'hosts': [target_host],
        'vars': {
            'ansible_python_interpreter': '/usr/bin/python3',
            'ansible_ssh_user': ssh_user,
            'ansible_ssh_pass': ssh_pass,
            'ansible_ssh_port': ssh_port,
        }
    }
}

print(json.dumps(inventory))
