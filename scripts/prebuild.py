#!/usr/bin/python
import re
import os
import sys
import json

import tools
import buildres
import copyres
import gentarget


def run(argv, projectDir, engineDir):
    buildres.run(argv, projectDir, engineDir)
    gentarget.run(argv, projectDir, engineDir)
    copyres.run(argv, projectDir, engineDir)
