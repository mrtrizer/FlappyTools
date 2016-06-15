#!/usr/bin/python
import os
import sys
import json
import re

import tools


def fileList(sourceDir, targetExt=None):
    fileList = []
    for path, dirs, files in os.walk(sourceDir):
        for fileName in files:
            ext = os.path.splitext(fileName)[1]
            filePath = os.path.join(os.path.relpath(path, sourceDir), fileName)
            if ((ext == targetExt) or (targetExt is None)):
                fileList.append(filePath)
    return fileList


def printList(list, template, exclude=None):
    text = ""
    for item in list:
        line = re.sub("\*", item, template)
        passLine = False
        if exclude is not None:
            for pattern in exclude:
                pattern = re.sub("\*\*", ".*", pattern)
                if (len(re.findall(pattern, line)) > 0):
                    passLine = True
        if not passLine:
            text += line
    return text


def run(argv, projectDir, engineDir, config):
    tools.assertMsg(len(argv) > 1, "Target not defined")
    templateDir = os.path.join(projectDir, "engine/templates/targets", argv[1])
    tools.assertMsg(os.path.isdir(templateDir),
                    "Target is not supported: " + argv[1])
    tools.assertMsg(config is not None, "It is not a flappy project subdir.")
    targetDir = os.path.join(projectDir, "targets", argv[1])

    print("Template: " + templateDir)
    print("Target: " + targetDir)

    functions = {"projectDir": projectDir,
                 "engineDir": engineDir,
                 "fileList": fileList,
                 "printList": printList}

    targetSpec = tools.loadTargetSpec(engineDir, argv[1], "methods")

    if targetSpec is not None:
        functions.update(targetSpec.__dict__)

    tools.replaceAll(templateDir, targetDir, config, functions)
