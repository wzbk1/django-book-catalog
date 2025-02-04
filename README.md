# Lab 7
## Instrukcje Uruchomienia Aplikacji

1. **Pobierz repozytorium z GitHub**:
```
git clone https://github.com/wzbk1/django-book-catalog
```

2. **Wchodzimy do folderu aplikacji**:
```
cd django-book-catalog\book_catalog
```

3. **Instalujemy zależności**:
```
pip install django
```

4. **Uruchamiamy serwer Django**:
```
python manage.py runserver
```
---
# Lab 8
## Uruchimianie testów

1. **Instalujemy zależności**:
```
pip install selenium
pip install webdriver-manager
```
2. **Komenda dla uruchamienie wszystkich testów odrazu**:
```
python manage.py test books
```
 3. **Testy oddzielnie**:
```
1. python manage.py test books.tests.test_views
2. python manage.py test books.tests.test_models
3. python manage.py test books.tests.test_acceptance (robić przy uruchomionej aplikacji)
4. python manage.py test books.tests.test_integration
```
