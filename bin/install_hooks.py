#!/usr/bin/env python

import subprocess
import os

ALL_HOOKS = ['applypatch-msg', 'pre-applypatch', 'post-applypatch', 'pre-commit', 'prepare-commit-msg', 'commit-msg', 'post-commit', 'pre-rebase', 'post-checkout', 'post-merge', 'pre-receive', 'update', 'post-receive', 'post-update', 'pre-auto-gc', 'post-rewrite', 'pre-push']


git_root = subprocess.check_output( ['git', 'rev-parse', '--show-toplevel'], shell=False).strip().decode('utf-8')

git_hook_dir =  git_root + '/.git/hooks/'

for hook_name in ALL_HOOKS:
    file_name = git_hook_dir + hook_name
    with open(file_name, 'w') as file:
        file.write('#!/bin/sh\npython ./bin/run_hook.py %s $@\n' % hook_name)
    os.chmod(file_name, 0o755)

