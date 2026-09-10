"""Warmup 4 - Virtual Environment Setup.

Confirms that requests is installed and importable inside the project's virtual
environment.

Set up with:
    python3 -m venv .venv
    source .venv/bin/activate
    pip install requests
    pip freeze > requirements.txt

# requirements.txt contents:
# certifi==2026.7.22
# charset-normalizer==3.5.1
# idna==3.19
# requests==2.34.2
# urllib3==2.7.0

Only `requests` was installed by hand - the other four are its dependencies,
pulled in automatically. That's the reason to commit requirements.txt rather
than a note saying "needs requests": it records the whole tree, at the versions
that actually worked.

Run this with the venv active, or it will raise ModuleNotFoundError from the
system Python, which has no requests installed.
"""

import requests

# Most packages expose __version__. Printing it proves the import came from the
# venv and not from nowhere.
print(f"requests version: {requests.__version__}")
