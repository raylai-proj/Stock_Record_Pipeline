"""
Summary: window_helper.py creates a GUI for selecting and executing analysis actions.

This module defines a Components class that builds a basic tkinter-based interface
with a dropdown to choose miscellaneous options analyze data.

Chun-Juei Lai 04/09/2026
"""

from tkinter import ttk


def demo():
    """Demo function for ACTDICT."""
    print("demo")


ACTDICT = {"test": demo}
FONT = ("Arial", 12)
PAD = 10


class Components(object):
    """Components class initial a window to provide actions in data analysis task."""

    def __init__(self, window):
        """Initialize Components object and create a window for data analysis task."""
        self.window = window
        self.label = ttk.Label(self.window, FONT, text="Select the Action:")
        self.label.grid(column=0, row=0, padx=PAD, pady=PAD, sticky="e")
