# Addpost

Prosty skrypt w Pythonie do masowego dodawania wpisów na stronę WordPress przez REST API (`/wp-json/wp/v2/posts`). Każdy wpis dostaje tytuł, treść, datę publikacji, slug zrobiony z tytułu i kategorię.

## Wymagania

- Python 3
- biblioteka `requests`
- strona na WordPressie 5.6 lub nowszym z włączonym REST API
- konto z uprawnieniami do publikowania i **hasło aplikacji** (Application Password)

```bash
pip install requests
```

> Skrypt importuje też `facepy` i `json`, ale z nich nie korzysta. Możesz usunąć te importy albo doinstalować `facepy` (`pip install facepy`), żeby skrypt w ogóle się uruchomił. Chciałem ich użyć potem do scrapowania strony facebooka do integracji wordpress i facebook(skończyło się niepowodzeniem).

## Konfiguracja

### 1. Hasło aplikacji

W panelu WordPressa wejdź w **Użytkownicy → Profil → Hasła aplikacji**, wpisz nazwę (np. `addpost`) i wygeneruj hasło.

### 2. Dane logowania

W `ko.py` uzupełnij:

```python
wordpress_user = "twoj_login"
wordpress_password = "abcd EFGH 1234 ijkl MNOP 5678"
```

Wpisz hasło aplikacji, a nie zwykłe hasło do konta.

### 3. Adres API

W funkcji `nowy_post` ustaw adres swojej strony:

```python
api_url = 'https://twojastrona.pl/wp-json/wp/v2/posts'
```

### 4. Kategoria

Wszystkie wpisy trafiają domyślnie do kategorii o ID `2`:

```python
'categories': '2'
```

ID kategorii sprawdzisz w panelu (**Wpisy → Kategorie**, najedź na nazwę i zobacz `tag_ID=` w adresie)

## Użycie

Wpisy dodajesz w trzech listach. Ten sam indeks w każdej liście oznacza ten sam wpis:

```python
title = ["Pierwszy wpis", "Drugi wpis"]
content = ["<p>Treść pierwszego wpisu</p>", "<p>Treść drugiego wpisu</p>"]
daty = ["2024-01-16T08:00:00", "2024-01-17T08:00:00"]
```

- `title` to tytuły wpisów. Slug powstaje z tytułu przez zamianę spacji na myślniki.
- `content` to treść. Może być zwykły tekst albo HTML.
- `daty` to data publikacji w formacie `RRRR-MM-DDTGG:MM:SS`, w strefie czasowej ustawionej na stronie.

Wszystkie trzy listy muszą mieć tyle samo elementów.

Potem uruchom:

```bash
python ko.py
```

Dla każdego wpisu skrypt wypisze odpowiedź serwera:

| Odpowiedź | Znaczenie |
|---|---|
| `<Response [201]>` | wpis dodany |
| `<Response [401]>` | zły login albo hasło aplikacji |
| `<Response [403]>` | konto nie ma uprawnień do publikowania |
| `<Response [400]>` | błędne dane, np. zły format daty albo nieistniejąca kategoria |
| `<Response [404]>` | zły adres API albo wyłączone REST API |

Wpisy dostają status `publish`, więc pojawiają się na stronie od razu. Jeśli data jest w przyszłości, WordPress ustawi je jako zaplanowane.

## Uwagi

- Skrypt nie sprawdza, czy wpis o takim tytule już istnieje. Każde uruchomienie doda wszystko jeszcze raz.
- Strona musi działać po HTTPS, bo hasło aplikacji leci w nagłówku Basic Auth.
