Python CI/CD Demo - opis projektu

To prosty projekt demonstracyjny w Pythonie, pokazujący pełny CI/CD pipeline z GitHub Actions.

Pipeline obejmuje:

Testy jednostkowe w Pythonie (pytest) przy każdym pushu do main.
Budowanie obrazu Docker po udanych testach.
Push obrazu Docker do GitHub Container Registry (GHCR).
Obsługę tagowania obrazów:
latest → zawsze najnowszy build

Struktura projektu

python-ci-cd-demo/
│── app.py             # prosta aplikacja Python
│── test_app.py        # testy jednostkowe
│── requirements.txt   # zależności
│── Dockerfile         # Dockerfile do budowy obrazu
│── .github/
│    └── workflows/
│         └── ci.yml   # workflow CI/CD


Wymagania:

Python 3.10+
Docker
GitHub repo z włączonym GitHub Actions i GitHub Container Registry, token
