# Description

A stupid simple script for watching for changes on a file (linux-only at the moment) and firing a command. In this case we fire off [landslide](https://github.com/adamzap/landslide).

# Requirements:

`Python` and the following module:
 - `landslide`

# Installation

Just use `pip` for the dependency:

    $ pip install landslide

Then put this script somewhere useful, like:

    $ chmod +x landslide_watch.py
    $ mv landslide_watch.py ~/bin/landslide_watch

# Usage

    $ landslide_watch file