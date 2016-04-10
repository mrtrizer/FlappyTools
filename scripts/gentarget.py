#!/usr/bin/python
import os
import sys
import json
import re

import tools


def fileList(sourceDir, template, targetExt=None):
    str = ""
    for path, dirs, files in os.walk(sourceDir):
        for fileName in files:
            ext = os.path.splitext(fileName)[1]
            line = re.sub("\*", fileName, template)
            if ((ext == targetExt) or (targetExt is None)):
                str += line
    return str


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
                 "engineDir": engineDir,
                 "fileList": fileList}

    targetSpec = tools.loadTargetSpec(engineDir, argv[1], "methods")

    if targetSpec is not None:
        functions.update(targetSpec.__dict__)

    tools.replaceAll(templateDir, targetDir, config, functions)
