#  This file is part of Python Builder
#
#  Copyright 2011-2013 PyBuilder Team
#
#  Licensed under the Apache License, Version 2.0(the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

"""
    Python module providing easy to use text styling for terminals
    being able to understand standard escape sequences.

    Sample usages:

        print styled_text("spam", fg(RED))
        print styled_text("spam", fg(BLACK), bg(GREY))

        print bold("eggs")
        print underline(bold("eggs"))
"""

import sys

_ESCAPE_SEQUENCE_PATTERN = "\033[%sm"
_ESCAPE_SEQUENCE_SEPARATOR = ";"

_BACKGROUND_COLOR = "4"
_FOREGROUND_COLOR = "3"

BLACK = "0"
RED = "1"
GREEN = "2"
BROWN = "3"
BLUE = "4"
MAGENTA = "5"
CYAN = "6"
GREY = "7"
COLOR_DEFAULT = "9"

RESET_TEXT_ATTRIBUTES = "0"
BOLD = "1"
ITALIC = "2"
UNDERLINE = "4"


def bg(color):
    """ Returns the color code to use the given color as a background color. """
    return _BACKGROUND_COLOR + str(int(color))


def fg(color):
    """ Returns the color code to use the given color as a foreground color. """
    return _FOREGROUND_COLOR + str(int(color))


def styled_text(text, *style_attributes):
    """
        Applies all the given style attributes to the given text and returns
        as string which contains
        - the application of the style attributes
        - the text itself
        - a reset of all style attributes
    """
    return "%s%s%s" % (
        _ESCAPE_SEQUENCE_PATTERN % (_ESCAPE_SEQUENCE_SEPARATOR.join(style_attributes)),
        text,
        _ESCAPE_SEQUENCE_PATTERN % "0;0")


def bold(text):
    """
        Convenience function to format the given text in bold font face.
        Equivalent to
            styled_text(text, BOLD)
    """
    return styled_text(text, BOLD)


def italic(text):
    """
        Convenience function to format the given text in italic font face.
        Equivalent to
            styled_text(text, ITALIC)
    """
    return styled_text(text, ITALIC)


def underline(text):
    """
        Convenience function to format the given text with an underline.
        Equivalent to
            styled_text(text, UNDERLINE)
    """
    return styled_text(text, UNDERLINE)


def write(text):
    sys.stdout.write(text)


def write_line(text=""):
    write(text)
    write("\n")


def draw_line():
    return write("-" * 60 + "\n")


def write_error(text):
    sys.stderr.write(text)


def write_error_line(text=""):
    write_error(text)
    write_error("\n")
