#!/usr/bin/env python


import re
import sys
import logging
from subprocess import check_output

logger = logging.getLogger(__name__)

hooks = {}



def prepare_commit_message():
    # Collect the parameters
    commit_msg_filepath = sys.argv[1]
    commit_hash = ''
    if len(sys.argv) > 2:
        commit_type = sys.argv[2]
    else:
        commit_type = ''
        if len(sys.argv) > 3:
            commit_hash = sys.argv[3]
        else:
            commit_hash = ''
    # Figure out which branch we're on
    branch = check_output(['git', 'symbolic-ref', '--short', 'HEAD']).strip().decode('utf-8')
    # Populate the commit message with the issue #, if there is one
    result = re.match('.*OFS[-_](\d+)', branch, re.IGNORECASE)
    if result:
        issue_number = result.group(1)
        with open(commit_msg_filepath, 'r+') as f:
            content = f.read()
            f.seek(0, 0)
            f.write("OFS-%s %s" % (issue_number, content))


def run_hook(hook_name):
    function = hooks.get(hook_name, None)
    sys.argv = sys.argv[1:]
    if function:
        function()

        
hooks = {'prepare-commit-msg' : prepare_commit_message}


run_hook(sys.argv[1].lower())





