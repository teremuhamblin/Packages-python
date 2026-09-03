###### README.md >> markdown 
# GitHub
- Packages
   - Package Python minimal pour démontrer la publication automatique via GitHub Actions.
 
### 🗂️ Structure de base du projet
```text
Packages-python/
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
