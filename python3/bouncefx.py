#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ============================================================================
# BounceFX - Line bouncing effect text printer
# Copyright (C) 2021 by Ralf Kilian
# Distributed under the MIT License (https://opensource.org/licenses/MIT)
#
# GitHub: https://github.com/urbanware-org/bouncefx
# GitLab: https://gitlab.com/urbanware-org/bouncefx
# ============================================================================

__version__ = "1.0.0"

import subprocess
import time


def bounce_line(string, line_length=80, delay=0.1, bounces=3):
    """
        Print the given string using a side bouncing effect.
    """
    if line_length == 0:
        # Determine the width (columns) of a line inside the console the
        # script is being run
        line_length = \
            int(subprocess.check_output(['stty', 'size']).split()[1])

    if not string:
        return

    if line_length < 0:
        raise Exception("The line length must at least be zero.")

    if len(string) >= line_length:
        raise Exception("The string must be shorter than the line length.")

    if delay <= 0:
        raise Exception("The delay must be greater than zero.")

    if bounces < 0:
        raise Exception("The number of bounces must at least be zero.")

    left = 0
    left_max = line_length - len(string) + 1
    go_left = True
    bounces_count = 0

    while True:
        string = (" " * left) + string.ljust(line_length, " ").strip() + " "
        print(string, end="\r")
        time.sleep(delay)

        if left == left_max:
            go_left = False
        elif left == 0:
            if bounces > 0 and bounces_count == bounces:
                print()
                break
            bounces_count += 1
            go_left = True

        if go_left:
            left += 1
        else:
            left -= 1

# EOF
