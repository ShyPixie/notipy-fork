#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name="notipy-fork",
    version="0.4.0",
    description="A minimalistic gtk3 notification daemon written in python.",
    author="Lara Maia",
    author_email="angel@mail.com",
    url="https://github.com/laracraft93/notipy/",
    scripts=["notipy"]
    license="GPLv3",
    data_files=[("/etc", ["notipy.conf"])]
    )
