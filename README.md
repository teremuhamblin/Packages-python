###### README.md >> markdown 
# GitHub

Python version 3.10 alpha 0
=====================================

.. image:: https://github.com/python/cpython/actions/workflows/build.yml/badge.svg?branch=main&event=push
   :alt: CPython build status on GitHub Actions
   :target: https://github.com/python/cpython/actions

.. image:: https://dev.azure.com/python/cpython/_apis/build/status/Azure%20Pipelines%20CI?branchName=main
   :alt: CPython build status on Azure DevOps
   :target: https://dev.azure.com/python/cpython/_build/latest?definitionId=4&branchName=main

.. image:: https://img.shields.io/badge/discourse-join_chat-brightgreen.svg
   :alt: Python Discourse chat
   :target: https://discuss.python.org/


Copyright © 2001 Python Software Foundation.  All rights reserved.

See the end of this file for further copyright and license information.

- Packages
   - Package Python minimal pour démontrer la publication automatique via GitHub Actions.
 
### 🗂️ Structure de base du projet
```text
Packages-python/
├── .github/
│   ├── FUNDING.yml
│   ├── CODEOWNERS
│   ├── CODE_OF_CONDUCT.yml
│   ├── CONTRIBUTING.yml
│   ├── SECURITY.yml
│   ├── ISSUE_TEMPLATE.yml
│   ├── PULL_REQUEST_TEMPLATE.yml
│   └── workflows/
│       ├── publish.yml
│       ├── ci.yml
│
├── src/
│   ├── README.md 
│   └── packages_python/
│       ├── init.py
│       ├── package-python.py
│       └── core.py
│
├── tests/
│   ├── README.md 
│   └── test_core.py
│
├── .gitignore
├── LICENSE
├── pyproject.toml
└── README.md
```

### 🚀 Installation
```bash
pip install packages-python
```

### 🧩 Utilisation
```python
from packages_python import add

print(add(2, 3))  # 5
```

### 🛠️ Publication
Créer un tag :
```bash
git tag v0.1.0
git push origin v0.1.0
```

>GitHub Actions publiera automatiquement le package
