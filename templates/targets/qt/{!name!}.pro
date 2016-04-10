QT += core

TARGET = test
CONFIG += console
CONFIG -= app_bundle

TEMPLATE = app
INCLUDEPATH += ../../src

include("../../engine/src/FlappyEngine.pri")

QMAKE_CXXFLAGS += -std=c++1y

DEFINES += VIEW_TYPE=GL

SOURCES += main.cpp

{?sourceList(projectDir,".cpp","SOURCES")?}
{?sourceList(projectDir,".h","HEADERS")?}
