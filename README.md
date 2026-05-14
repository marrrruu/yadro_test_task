# Автоматизация развертывания скрипта с использованием Python, Docker и Ansible

## Структура проекта

- **`setup_playbook.yml`** — Ansible-плейбук.
- **`http_script.py`** — Python-скрипт.
- **`Dockerfile`** — Докерфайл.
- **`requirements.txt`** — Внешние зависимости.

---

## Требования к окружению

1. **На управляющей машине:**
   - Установлен Ansible
2. **На целевом хосте:**
   - Операционная система семейства **Debian**  или **RedHat**.
---

## Инструкция по запуску

1. Запуск на локальном хосте

ansible-playbook -i "localhost," -c local setup_playbook.yml -K

2. Запуск на удаленном

ansible-playbook -i hosts.ini setup_playbook.yml -K

