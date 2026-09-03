"""
core.py — Module principal du package Packages-python
Version : 0.1.0
Description : Fonctions simples pour démonstration GitHub Packages.
"""

def add(a: int, b: int) -> int:
    """
    Additionne deux entiers.
    """
    return a + b


def multiply(a: int, b: int) -> int:
    """
    Multiplie deux entiers.
    """
    return a * b


def status() -> str:
    """
    Retourne un statut simple pour vérifier le bon fonctionnement du package.
    """
    return "Packages-python operational"
