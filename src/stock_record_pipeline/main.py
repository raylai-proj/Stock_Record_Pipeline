"""
Summary: main.py launch the main() process stock record pipeline.

Author: Chun-Juei Lai 04/08/2026
"""

import tkinter as tk

from stock_record_pipeline import utility


def main():
    """Entry point of the program."""
    window = tk.Tk()
    utility.Components(window)
    window.mainloop()


if __name__ == "__main__":
    main()
