import re
import os
import json
import shutil


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


def replace(data, config):
    curData = data

    def replaceLink(str):
        repl = str.group(1)
        value = findValue(config, repl)
        return value

    def evalCode(str):
        repl = str.group(1)
        return eval(repl, config)
    curData = re.sub("{!(.*?)!}", replaceLink, curData)
    curData = re.sub("{\?(.*?)\?}", evalCode, curData)
    return curData


def replaceAll(templateDir, targetDir, config):
    print "Parameters:"
    print json.dumps(config, sort_keys=True, indent=4, separators=(',', ': '))
    print "Processing..."
    for path, dirs, files in os.walk(templateDir):
        for fileName in files:
            print bcolors.OKGREEN + " [PROC] " + bcolors.ENDC + fileName
            relPath = os.path.relpath(path, templateDir)
            relPath = replace(relPath, config)
            inPath = os.path.join(path, fileName)
            outPath = os.path.join(targetDir, relPath, fileName)
            outDir = os.path.dirname(outPath)
            with open(inPath, 'r') as f:
                inData = f.read()
                outData = replace(inData, config)
                if not os.path.exists(outDir):
                    os.makedirs(outDir)
                out = open(outPath, 'w')
                out.write(outData)


def copyAll(sourceDir, targetDir):
    for path, dirs, files in os.walk(sourceDir):
        print "Path: " + os.path.relpath(path)
        for fileName in files:
            print (bcolors.OKGREEN + " [COPY] " +
                   bcolors.ENDC + fileName)
            shutil.copy(os.path.join(path, fileName), targetDir)


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
