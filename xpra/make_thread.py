# This file is part of Xpra.
# Copyright (C) 2012-2013 Antoine Martin <antoine@xpra.org>
# Xpra is released under the terms of the GNU GPL v2, or, at your option, any
# later version. See the file COPYING for details.

"""
Intercepting thread creation

These wrapper functions are here so that we can more easily intercept
the creation of all daemon threads and inject some code.

This is used by the `pycallgraph` test wrapper.
(this is cleaner than overriding the threading module directly
 as only our code will be affected)
"""

from threading import Thread
from collections.abc import Callable

def make_thread(target : Callable, name : str, daemon : bool=False, args=()) -> Thread:
    t = Thread(target=target, name=name, args=args)
    t.daemon = daemon
    return t

def start_thread(target : Callable, name : str, daemon : bool=False, args=()) -> Thread:
    t = make_thread(target, name, daemon, args=args)
    t.start()
    return t
