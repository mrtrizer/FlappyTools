import os


def copyRes(filePath, targetPath):
    (_, ext) = os.path.splitext(filePath)
    if (ext == ".png"):
        return os.path.join(targetPath, "drawable")
    return targetPath
