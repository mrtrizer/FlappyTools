#!/usr/bin/python
import os
import sys
import json
import re
import md5
import tools


def run(argv, projectDir, engineDir, config):
    tools.assertMsg(len(argv) > 1, "Target not defined")
    templateDir = os.path.join(projectDir,
                               config["engine"],
                               "targets",
                               argv[1],
                               "template")

    print("Template: " + templateDir)

    tools.assertMsg(os.path.isdir(templateDir),
                    "Target is not supported: " + argv[1])
    tools.assertMsg(config is not None, "It is not a flappy project subdir.")
    targetDir = os.path.join(projectDir, "targets", argv[1])

    print("Target: " + targetDir)

    functions = {"projectDir": projectDir,
                 "engineDir": engineDir}

    commonMethods = tools.loadTargetAll(projectDir,
                                        engineDir,
                                        "methods",
                                        config)

    functions.update(commonMethods.__dict__)

    targetSpec = tools.loadTargetSpec(projectDir,
                                      engineDir,
                                      argv[1],
                                      "methods",
                                      config)

    if targetSpec is not None:
        functions.update(targetSpec.__dict__)

    tools.replaceAll(templateDir, targetDir, config, functions)
