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

    projectName = argv[1]
    enginePath = None
    if len(argv) > 2:
        enginePath = argv[2]
    engineRepo = "https://github.com/mrtrizer/FlappyEngine.git"

    tools.assertMsg(not os.path.exists(projectName),
                    "Dir with name \"" + projectName + "\" already exists.")

    os.makedirs(projectName)
    os.chdir(projectName)
    projectDir = "."

    # Add a submodule only if engine path was not defined
    if not enginePath:
        enginePath = "engine"
        print os.popen("git init").read().strip()
        print os.popen("git submodule add " + engineRepo + " " + enginePath).read().strip()
        print os.popen("git submodule update --init").read().strip()

    templateDir = os.path.join(engineDir, "templates/project")
    tools.infoMessage("info", "Project template: " + templateDir)
    config = {"name": projectName, "engine": enginePath}

    tools.replaceAll(templateDir, projectDir, config)
