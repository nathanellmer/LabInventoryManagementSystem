import sys
import os


def resource_path(relative_path):
    """Get absolute path to resource (works in dev and PyInstaller)"""
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS  # PyInstaller temp folder
    else:
        base_path = os.path.abspath(".")  # dev environment

    return os.path.join(base_path, relative_path)