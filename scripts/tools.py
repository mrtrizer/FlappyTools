import re
import os
import json
import shutil
import imp


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def findValue(config, keyStr):
    keyList = keyStr.split(".")
    curConfig = config
    for key in keyList:
        if (isinstance(curConfig, dict)):
            if (key in curConfig):
                curConfig = curConfig[key]
            else:
                return 0
        else:
            return 1
    return curConfig


def replace(data, config, functions):
    curData = data

    def replaceLink(str):
        repl = str.group(1)
        value = findValue(config, repl)
        return value

    def evalCode(str):
        repl = str.group(1)
        return eval(repl, config, functions)
    curData = re.sub("{!(.*?)!}", replaceLink, curData)
    curData = re.sub("{\?(.*?)\?}", evalCode, curData)
    return curData


def replaceAll(templateDir, targetDir, config, functions={}):
    print "Parameters:"
    print json.dumps(config, sort_keys=True, indent=4, separators=(',', ': '))
    print "Processing..."
    for path, dirs, files in os.walk(templateDir):
        for fileName in files:
            print bcolors.OKGREEN + " [PROC] " + bcolors.ENDC + fileName
            relPath = os.path.relpath(path, templateDir)
            inPath = os.path.join(path, fileName)
            outPath = os.path.join(targetDir, relPath, fileName)
            outPath = replace(outPath, config, functions)
            outDir = os.path.dirname(outPath)
            with open(inPath, 'r') as f:
                inData = f.read()
                outData = replace(inData, config, functions)
                if not os.path.exists(outDir):
                    os.makedirs(outDir)
                if os.path.exists(outPath):
                    check = open(outPath, 'r')
                    if (check.read() == outData):
                        print (bcolors.OKGREEN + " [PASS] " + bcolors.ENDC +
                               fileName)
                        continue
                out = open(outPath, 'w')
                out.write(outData)


def copyAll(sourceDir, targetDir, copyCallback=None):
    for path, dirs, files in os.walk(sourceDir):
        print "Path: " + os.path.relpath(path)
        for fileName in files:
            outDir = targetDir
            if copyCallback is not None:
                outDir = copyCallback(fileName, targetDir)
            if not os.path.exists(outDir):
                os.makedirs(outDir)
                print (bcolors.OKGREEN +
                       " [NEW DIR] " +
                       bcolors.ENDC +
                       outDir)
            print (bcolors.OKGREEN +
                   " [COPY] " +
                   bcolors.ENDC +
                   fileName + " > " + outDir)
            shutil.copy(os.path.join(path, fileName), outDir)


def findProRoot(path):
    """Searches a project root with config.json. Returns None if can't find."""
    proRootPath = os.path.realpath(path)
    while (proRootPath != "/"):
        if (os.path.exists(os.path.join(proRootPath, "config.json"))):
            return proRootPath
        proRootPath = os.path.realpath(os.path.join(proRootPath, ".."))
    return None


def getToolPath(path):
    """Returns path to FlappyTools"""
    return os.path.join(os.path.dirname(os.path.realpath(path)), "..")


def assertMsg(condition, msg):
    if (condition):
        return
    print (bcolors.FAIL + " [ERROR] " + bcolors.ENDC + msg)
    exit(1)


def loadTargetAll(projectDir, engineDir, name):
    """Loads common targets script and returns it as a module"""
    scriptPath = os.path.join(projectDir,
                              "engine/scripts/targets/",
                              name + ".py")
    if (os.path.exists(scriptPath)):
        return imp.load_source(name, scriptPath)
    else:
        return None


def loadTargetSpec(projectDir, engineDir, target, name):
    """Loads target specific script and returns it as a module"""
    scriptPath = os.path.join(projectDir,
                              "engine/scripts/targets/",
                              target,
                              name + ".py")
    if (os.path.exists(scriptPath)):
        return imp.load_source(name, scriptPath)
    else:
        return None
