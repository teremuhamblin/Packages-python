###### README.md >> markdown 

[![CI](https://github.com/teremuhamblin/Packages-python/actions/workflows/ci.yml/badge.svg)](https://github.com/teremuhamblin/Packages-python/actions/workflows/ci.yml)

**Packages Python**
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
