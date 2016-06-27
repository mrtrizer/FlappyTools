#!/usr/bin/python
import re
import os
import sys
import json

import tools


def run(argv, projectDir, engineDir, config):
    tools.assertMsg(len(argv) > 1, "Specify a project name.")
    tools.assertMsg(projectDir is None, "Project was initialized earlier.\n" +
                                        "Remove config.json to reinitialize.")
    projectDir = "."

    print os.popen("git init").read().strip()
    print os.popen("git submodule add https://github.com/mrtrizer/FlappyEngine.git engine").read().strip()
    print os.popen("git submodule update --init").read().strip()

    templateDir = os.path.join(projectDir, "engine/templates/project")
    projectName = argv[1]
    config = {"name": projectName}

    tools.replaceAll(templateDir, projectDir, config)
