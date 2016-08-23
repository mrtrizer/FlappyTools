#!/usr/bin/python
import os
import sys

import tools


def run(argv, projectDir, engineDir, config):
    engineResDir = os.path.join(projectDir, config["engine"], "res")
    projectResDir = os.path.join(projectDir, "res")
    templateConfigDir = os.path.join(projectDir,
                                     config["engine"],
                                     "templates/")
    outResDir = os.path.join(projectDir, "build/res/")
    outSrcDir = os.path.join(projectDir, "build/src/")

    if not os.path.exists(outResDir):
        os.makedirs(outResDir)

    if not os.path.exists(outSrcDir):
        os.makedirs(outSrcDir)

    resDirs = [engineResDir, projectResDir]

    print "Resource processing..."
    for resDir in resDirs:
        tools.copyAll(resDir, outResDir)

    print "Config generation..."
    revision = os.popen("git describe --always").read().strip()
    print len(revision.strip())
    if (len(revision.strip()) == 0):
        revision = "0"
    config = {"revision": revision}
    tools.replaceAll(templateConfigDir, outSrcDir, config)
