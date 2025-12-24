# Лабораторна робота №2  
## Створення простого HTTP-клієнта (Python)

### Опис
Проєкт демонструє реалізацію простого HTTP-клієнта мовою Python для роботи з REST API **MeowFacts**.
Клієнт виконує GET-запити, обробляє JSON-відповіді та зберігає отримані дані у CSV-файл.

---

### Використане API
- **MeowFacts API**
- Документація: https://github.com/wh-iterabb-it/meowfacts
- Endpoint: `https://meowfacts.herokuapp.com/?count=N`

---

### Структура проєкту

- [`client.py`](./client.py) — HTTP-клієнт для роботи з API  
- [`main.py`](./main.py) — демонстрація використання клієнта  
- [`meow_facts.csv`](./meow_facts.csv) — збережені результати роботи клієнта  
---

### Запуск

```bash
python main.py
