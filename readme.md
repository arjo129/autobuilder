# Autobuild.py

>All code must be compiled, from the first day of development, with all compiler warnings enabled at the most
>pedantic setting available. All code must compile without warnings. All code must also be
>checked daily with at least one,
>but preferably more than one, strong static source code analyzer and should pass all analyses with zero warnings-- _JPL Coding standard_

Autobuild.py is a build system that aims to make unit testing easy for C/C++ so that you're
code can be compiled on Day 1. It is inspired by go's simple but elegant unit testing framework.

## Usage

To start a new project use the command line tool
``````````````
 autobuilder.py init
``````````````
This will create the following directory tree:
``````````````
+---configure.ab
|
+---include/
|
+---tests/
|
+---src/
|
+---libs/
``````````````
In your tests folder you can include your unit tests and runtime tests.
