# 🐍 Django Girls — Blog

Blog criado seguindo o tutorial [**Django Girls**](https://tutorial.djangogirls.org/pt/): aplicação com posts (autor, título, texto, datas de criação e publicação), área administrativa e formulários para criar/editar posts.

## Tecnologias

Python · Django

## Como rodar

```bash
cd smoke
python -m venv venv && source venv/bin/activate
pip install django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver     # http://localhost:8000  (admin em /admin)
```

## Autor

Feito por [Amós Magalhães](https://github.com/amslimaa).
