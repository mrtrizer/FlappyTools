#!/usr/bin/python
import os
import sys
import json

import tools


def run(argv, projectDir, engineDir, config):
    tools.assertMsg(projectDir,
                    "Wrong project dir. Can't find project configuration.")
    tools.assertMsg(len(argv) > 1, "Target is not defined")
    targetDir = os.path.join(projectDir, "targets/", argv[1], "res/")
    resDir = os.path.join(projectDir, "build/res/")
    targetResDir = os.path.join(projectDir, "targets/", argv[1], "res/")

    targetSpec = tools.loadScripts(targetResDir,
                                      "copyres",
                                      config)
    if targetSpec is not None:
        tools.copyAll(resDir, targetResDir, targetSpec.copyRes)
    else:
        tools.copyAll(resDir, targetResDir)

    print "Resource copy to target..."
