#!/usr/bin/python
import os
import sys
import json
import imp

import tools


def run(argv, projectDir, engineDir):
    tools.assertMsg(len(argv) > 1, "Target not defined")
    templateDir = os.path.join(engineDir, "templates/targets", argv[1])
    tools.assertMsg(os.path.isdir(templateDir),
                    "Target is not supported: " + argv[1])
    configPath = os.path.join(projectDir, "config.json")

    jsonFile = open(configPath, 'r')
    config = json.load(jsonFile)
    targetDir = os.path.join(projectDir, "targets", argv[1])

    print("Template: " + templateDir)
    print("Target: " + targetDir)
    print("Config: " + configPath)

    functions = {"projectDir": projectDir,
                 "engineDir": engineDir}

    scriptPath = os.path.join(engineDir,
                              "scripts/targets/",
                              argv[1],
                              "gentarget.py")
    if (os.path.exists(scriptPath)):
        functions.update(imp.load_source('copyres', scriptPath).__dict__)

    tools.replaceAll(templateDir, targetDir, config, functions)
