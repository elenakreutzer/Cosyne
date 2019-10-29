#!/usr/bin/env python2
# encoding: utf-8

import glob
import os
import os.path as osp
import sys #setting search paths

#insert directory name of absolute path of current file at front of search path
sys.path.insert(0, osp.dirname(osp.abspath(__file__)))

import core
from core import log
reload(core)

#looks for files called fig*.py
def plot_all():
    plotscripts = glob.glob(osp.join(osp.dirname(osp.abspath(__file__)),
        "fig*.py"))
    #split base names of the fig files in root and extension, then discard extension
    plotscripts = map(lambda x: osp.splitext(osp.basename(x))[0], plotscripts)
    print(plotscripts)
    #make all the figures with core method
    for name in plotscripts:
        core.make_figure(name)
    


if __name__ == "__main__":# only executed when main is run directly
    import sys
    from inspect import isfunction, getargspec
    local_globals = globals().keys()
    

    def is_noarg_function(f):
        "Test if f is valid function and has no arguments"
        func = globals()[f]
        if isfunction(func):
            argspec = getargspec(func)
            if len(argspec.args) == 0\
                        and argspec.varargs is None\
                        and argspec.keywords is None:
                return True
        return False

    def show_functions():
        functions.sort()
        for f in functions:
            print f
    functions = [f for f in local_globals if is_noarg_function(f)]
    if len(sys.argv) <= 1 or sys.argv[1] == "-h":#no command line arguments
        show_functions()# print global functions with no arguments
    else:#if other functions are passed as command line arguments, run these functions
        for launch in sys.argv[1:]:
            if launch in functions:
                run = globals()[launch]
                run()
            else:
                print launch, "not part of functions:"
                show_functions()

