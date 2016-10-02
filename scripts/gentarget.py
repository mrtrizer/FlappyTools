#!/usr/bin/python
import os
import sys
import json
import re
import md5
import tools


def parseTemplateFolder(sourceTemplateDir, targetDir, config, functions):

    # methods loading
    # all loaded methods can be called from templates

    curPath = sourceTemplateDir

    # load common methods for target template and parent dirs
    for i in range(3):
        commonMethods = tools.loadScripts(curPath, "methods", config)
        if commonMethods is not None:
            functions.update(commonMethods.__dict__)
        curPath = os.path.join(curPath, "..")

    tools.replaceAll(sourceTemplateDir, targetDir, config, functions)


def run(argv, projectDir, engineDir, config):
    tools.assertMsg(projectDir, "Wrong project dir. Can't find project configuration.")
    tools.assertMsg(len(argv) > 1, "Target not defined")
    tools.assertMsg(config is not None, "It is not a flappy project subdir.")

    targetName = argv[1]
    templateDir = os.path.join(projectDir, config["engine"], "templates")
    moduleTemplateDir = os.path.join(templateDir, "modules", targetName)
    targetTemplateDir = os.path.join(templateDir, "targets", targetName)

    print("Template: " + templateDir)

    tools.assertMsg(os.path.isdir(targetTemplateDir), "Target is not supported: " + targetName)

    targetDir = os.path.join(projectDir, "targets", targetName)

    print("Target: " + targetDir)

    # module configs loading first
    modules = []
    if "modules" in config:
        for modulePath in config["modules"]:
            configPath = os.path.join(projectDir, modulePath, "config.json")
            jsonFile = open(configPath, 'r')
            moduleConfig = tools.parseConfig(json.load(jsonFile))
            moduleConfig["path"] = modulePath
            moduleConfig["project"] = config
            modules.append(moduleConfig)

    # we need moduleNames for using in printList()
    moduleNames = []
    for module in modules:
        moduleNames.append(module["name"])

    functions = {"projectDir": projectDir,
                 "engineDir": engineDir,
                 "modules": modules,
                 "moduleNames": moduleNames}

    # process all modules
    for module in modules:
        parseTemplateFolder(moduleTemplateDir, targetDir, module, functions)

    # script for special actions after module generation
    targetSpec = tools.loadScripts(targetTemplateDir, "genmodules", config)
    if targetSpec is not None:
        targetSpec.genModules(argv, projectDir, engineDir, config, modules)

    # loading of project itself
    parseTemplateFolder(targetTemplateDir, targetDir, config, functions)
