#!/usr/bin/python
import re
import os
import sys
import json

import tools


def run(argv, projectDir, engineDir):
    tools.assertMsg(len(argv) > 1, "Specify a project name.")
    tools.assertMsg(projectDir is None, "Project was initialized earlier.\n" +
                                        "Remove config.json to reinitialize.")
    projectDir = "."

    templateDir = os.path.join(engineDir, "templates/project")
    projectName = argv[1]
    config = {"name": projectName}

    tools.replaceAll(templateDir, projectDir, config)
