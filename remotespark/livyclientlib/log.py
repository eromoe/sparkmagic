﻿# Copyright (c) 2015  aggftw@gmail.com
# Distributed under the terms of the Modified BSD License.

from __future__ import print_function


class Log(object):
    """Logger."""

    _mode = "normal"
                
    @property
    def mode(self):
        """One of: 'debug', 'normal'"""
        return self._mode

    @mode.setter
    def mode(self, value):
        self.debug("Logger mode set to: {}".format(value))

        val = value.lower()

        if val == "debug":
            self.mode = "debug"
        elif val == "error":
            self.mode = "error"
        else:
            self.mode = "normal"

    def debug(self, message):
        """Prints if in debug mode."""
        if self._mode == "debug":
            print("DEBUG\t" + message)

    def error(self, message):
        """Prints if in debug mode."""
        if self.mode == "debug" or self.mode == "error":
            print("ERROR\t" + message)
