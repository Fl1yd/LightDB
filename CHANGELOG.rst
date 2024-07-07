Changelog
=========

2.0
---

Added
^^^^^
- Created `models.py` for model implementation
- Created `fields.py` for field implementation and validation
- Created `query.py` for executing queries on model data
- Created `exceptions.py` to define custom exceptions related to models
- Added tests for LightDB and models
- Updated `README.md` with documentation on using models
- Added an example of using models in `examples/models_usage.py`


1.4.0
-----

- Rename `LightDB.py` -> `core.py`
- Update license


1.3.3
-----

Added
^^^^^
- Rewrite code and docstrings
- Rewrite README
- Added tests


1.3.2
-----

Fixed
^^^^^
- Fixed error while getting non string key


1.3.1
-----

Fixed
^^^^^
- Fixed encoding error


1.3
---

Added
^^^^^
- Added methods: `set_key()`, `get_key()`, `pop_key()`


1.2
---
- Some code refactor


1.1
---

Added
^^^^^
- Added subclass `dict`

Fixed
^^^^^
- Fixed fatal error: recursive function call


1.0
---

Added
^^^^^
- Added class `LightDB`
