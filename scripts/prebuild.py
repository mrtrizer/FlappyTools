#!/usr/bin/python
import re
import os
import sys
import json

import tools
import buildres
import copyres
import gentarget


def run(argv, projectDir, engineDir, config):
    buildres.run(argv, projectDir, engineDir, config)
    gentarget.run(argv, projectDir, engineDir, config)
    copyres.run(argv, projectDir, engineDir, config)
