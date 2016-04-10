import os
import re


def sourceList(sourceDir, template, targetExt=None):
    str = ""
    for path, dirs, files in os.walk(sourceDir):
        for fileName in files:
            ext = os.path.splitext(fileName)[1]
            line = re.sub("\*", fileName, template)
            print fileName
            if ((ext == targetExt) or (targetExt is None)):
                str += line
    return str
