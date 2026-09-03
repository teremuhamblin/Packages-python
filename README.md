###### README.md >> markdown 
# GitHub
- Packages
   - Package Python minimal pour démontrer la publication automatique via GitHub Actions.

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
