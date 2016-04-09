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

SOURCES += ../../src/ctrl.cpp ../../src/world.cpp
HEADERS += ../../src/ctrl.h ../../src/world.h

