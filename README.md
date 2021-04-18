# ZIwG
Zastosowania Informatyki w Gospodarce


## Backend:

### Uruchamianie:
1. Utwórz wirtualne środowisko pythona `virtualenv venv`.
2. Uruchom wirtualne środowisko (na linux `source venv/bin/activate`).
3. Zainstaluj wymagane biblioteki (`pip install -r requirements.txt`).
4. Przejdź do folderu backend.
5. Uruchom migracje `python manage.py makemigrations`, a następnie `python manage.py migrate`.
6. Stwórz superużytkownika `python manage.py createsuperuser`.
7. Uruchom backend `python manage.py runserver`

## Frontend:

### Uruchamianie:
1. Przejdź do folderu frontend
2. Pobierz zależności 
```
npm install
```
3. Uruchom
    * Serwer developerski
    ```
    npm run serve
    ```
    * Serwer produkcyjny
    ```
    npm run build
    ```
    * Panel vue
    ```
    vue ui
    ```
