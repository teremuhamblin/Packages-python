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
│       ├── pyproject.toml
│       ├── init.py
│       ├── package-python.py
│       └── core.py
│
├── tests/
│   ├── README.md 
│   └── test_core.py
│
├── .gitignore
├── MANIFEST.in
├── LICENSE
├── setup.py
├── setup.cfg
├── CHANGELOG.md
└── README.md
```

### 🚀 Installation
```bash
pip install packages-python
```

>Calibrer pour ton projet Packages Delivery / Packages-python, layout :
```md
setup.cfg
setup.py
MANIFEST.in
CHANGELOG.md
.gitignore
src/packages_python/
```

---

### 🛡️ Sections pour documenter
![Version](https://img.shields.io/badge/version-0.1.0-blue)
#### 📦 MANIFEST.in
Le fichier MANIFEST.in contrôle les fichiers inclus dans la distribution Python.  
Dans ce projet, il permet :
   - d’inclure la documentation (README.md, CHANGELOG.md, LICENSE)
   - d’inclure tous les fichiers utiles du package packages_python
   - d’exclure les fichiers inutiles (pycache, .pyc)

>Cela garantit que le package publié sur GitHub Packages contient tout ce qui est nécessaire.

### 📝 CHANGELOG.md
- Le fichier CHANGELOG.md documente l’évolution du projet.  
- Il suit une structure simple :
   - Ajouté : nouvelles fonctionnalités  
   - Fixé : corrections  
   - Notes : informations diverses  

- La version actuelle : ***0.1.0 — Initial Release***

---

### 🔒 .gitignore
- Le .gitignore est optimisé pour :
   - Python  
   - Build (dist/, build/)  
   - Environnements virtuels  
   - IDE (VSCode, PyCharm)  
   - GitHub Actions  
   - Fichiers système  

>Il protège ton dépôt contre les fichiers inutiles ou sensibles.

---

### ⚙️ Packaging
![Python](https://img.shields.io/badge/python-3.10_|_3.11_|_3.12-blue.svg)
- (setup.cfg + setup.py)
Le projet utilise :
   - setup.cfg pour la configuration du package  
   - setup.py minimal pour permettre le build  
   - MANIFEST.in pour contrôler les fichiers inclus  

Le layout est :
```text
src/packages_python/
```

Ce modèle est compatible :
- python -m build
- pip install .
- GitHub Actions CI
- Publication GitHub Packages

---

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
