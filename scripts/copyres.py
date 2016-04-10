#!/usr/bin/python
import os
import sys
import json
import imp

import tools


def run(argv, projectDir, engineDir):
    tools.assertMsg(len(argv) > 1, "Target is not defined")
    targetDir = os.path.join(projectDir, "targets/", argv[1], "res/")
    resDir = os.path.join(projectDir, "build/res/")
    targetResDir = os.path.join(projectDir, "targets/", argv[1], "res/")

    scriptPath = os.path.join(engineDir,
                              "scripts/targets/",
                              argv[1],
                              "copyres.py")
    if (os.path.exists(scriptPath)):
        copyResFunc = imp.load_source('copyres', scriptPath).copyRes
        tools.copyAll(resDir, targetResDir, copyResFunc)
    else:
        tools.copyAll(resDir, targetResDir)

    print "Resource copy to target..."
