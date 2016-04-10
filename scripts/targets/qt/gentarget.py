import os


def sourceList(projectDir, targetExt, name):
    str = ""
    srcDir = os.path.join(projectDir, "src")
    for path, dirs, files in os.walk(srcDir):
        for fileName in files:
            ext = os.path.splitext(fileName)[1]
            print ext
            if (ext == targetExt):
                str += name + " += ../../" + fileName + "\n"
    print str
    return str
