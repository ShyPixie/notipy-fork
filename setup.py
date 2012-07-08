#!/usr/bin/env python
# -*- coding: utf-8 -*-

import distutils.core

distutils.core.setup(
    name="notipy-fork",
    version="0.3.0",
    description="A minimalistic gtk3 notification daemon written in python.",
    author="Lara Maia",
    author_email="angel@mail.com",
    url="https://github.com/laracraft93/notipy/",
    scripts=["notipy"]
    )
