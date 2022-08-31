from __future__ import annotations

import json.encoder as json_encoder
import os
import os.path
from base64 import b16decode
from base64 import b32decode as b32
from base64 import b64encode
from os import chdir as annotations  # type: ignore
from os import path

import black
import tomli

from . import something  # type: ignore

os.listdir(".")
os.path.dirname(".")


with open("pyproject.toml", "rb") as f:
    tomli.load(f)
path.dirname(".")
something()
annotations(".")  # type: ignore
b64encode(b"")
b16decode(b"")
b32(b"")
json_encoder.JSONEncoder()

black.nullcontext()
