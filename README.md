## 🔁 CI/CD пайплайн

Цей репозиторій має автоматизований CI/CD, що працює через **GitHub Actions**.

### 🚀 Коли запускається:
- При створенні Pull Request у гілку `develop`.

### 🧪 Що перевіряється:
1. **Наявність схваленого код-рев’ю** (APPROVED)
2. **Лінтинг через Flake8**
3. **Форматування через Black**
4. **Юніт-тести з покриттям (`pytest + coverage`)**
5. **Метрики коду через Cloc**
6. **Статичний аналіз через SonarCloud**

### ⚙️ Інструменти:
- `flake8` + `reviewdog` (лінтинг з коментарями)
- `black` + `reviewdog` (перевірка форматування)
- `pytest` + `pytest-cov`
- `cloc` (підрахунок рядків коду)
- `SonarCloud`

### ✅ Статус:
![CI](https://github.com/D4bleGunInVador/zonk_project/actions/workflows/ci.yml/badge.svg)
