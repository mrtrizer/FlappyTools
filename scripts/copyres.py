#!/usr/bin/python
import os
import sys
import json
import imp

import tools


def defaultCopyRes(filePath, targetPath):
    return os.path.join(targetPath, "res")


def run(argv, projectDir, engineDir):
    tools.assertMsg(len(argv) > 1, "Target not defined")
    targetDir = os.path.join(projectDir, "targets/", argv[1], "res/")
    resDir = os.path.join(projectDir, "build/res/")
    targetResDir = os.path.join(projectDir, "targets/", argv[1], "res/")

    scriptPath = os.path.join(engineDir,
                              "scripts/targets/",
                              argv[1],
                              "copyres.py")
    copyResFunc = defaultCopyRes
    if (os.path.exists(targetResDir)):
        copyResFunc = imp.load_source('copyres', scriptPath).copyRes

    print "Resource copy to target..."
    tools.copyAll(resDir, targetResDir, copyResFunc)
