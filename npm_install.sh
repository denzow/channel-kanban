#!/bin/sh

args=$#

if [ ${args} -eq 0 ] ; then
    npm --prefix ./docker/task_runner/ install ./docker/task_runner/;
else
    npm --prefix ./docker/task_runner/ install $*;
fi