#!/usr/bin/python
import os
import sys
import json
import re

import tools


def run(argv, projectDir, engineDir, config):
    """Prints help doc from doc/commands"""
    if (len(argv) < 2):
        commandName = "help"
    else:
        commandName = argv[1]
    pagePath = os.path.join(engineDir, "doc/commands", commandName + ".md")
    tools.assertMsg(os.path.exists(pagePath), "Unknown command " + commandName)
    text = open(pagePath, 'r').read()
    text = re.sub("^.*\n\=*", "", text)
    print text
