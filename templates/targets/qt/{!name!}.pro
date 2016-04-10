QT += core

TARGET = test
CONFIG += console
CONFIG -= app_bundle

TEMPLATE = app
INCLUDEPATH += ../../src
INCLUDEPATH += ../../build/src/

include("../../engine/src/FlappyEngine.pri")

QMAKE_CXXFLAGS += -std=c++1y

DEFINES += VIEW_TYPE=GL

SOURCES += main.cpp
HEADERS += ../../build/src/config.h

{?sourceList(projectDir + "/src/","SOURCES += ../../src/*\n",".cpp")?}
{?sourceList(projectDir + "/src/","HEADERS += ../../src/*\n",".h")?}

prebuildTarget.target = prebuild
prebuildTarget.depends = FORCE
prebuildTarget.commands = flappy prebuild qt
QMAKE_EXTRA_TARGETS += prebuildTarget
PRE_TARGETDEPS += prebuild

RESOURCES += res.qrc
