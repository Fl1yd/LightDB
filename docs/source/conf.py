import os
import sys
import datetime

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, root_path)

import lightdb

# Project information
project = "LightDB"
author = "Fl1yd"
copyright = f"2021-{datetime.date.today().year}, {author}"
release = lightdb.__version__

# Templates
html_theme = "furo"
html_favicon = "_static/favicon.ico"

html_static_path = ["_static"]
templates_path = ["_templates"]

html_theme_options = {
    "light_logo": "logo_light.png",
    "dark_logo": "logo_dark.png",
}

# Extensions
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.todo"
]

# Parameters
todo_include_todos = True
