# Monthly Meal Schedule Generator

## Opis
To narzędzie generuje harmonogram posiłków dla wybranego miesiąca i grup osób, a następnie zapisuje go jako plik PDF w formacie A4 (orientacja pozioma). Każda grupa otrzymuje osobną stronę.

## Wymagania
Program działa jako samodzielny plik wykonywalny, ale jeśli chcesz uruchomić go ze źródła, wymagane są:
- Python 3
- `pip install -r requirements.txt`
- `wkhtmltopdf` (zainstalowany i dostępny w PATH)

## Instalacja `wkhtmltopdf`
- **Windows**: Pobierz i zainstaluj z [wkhtmltopdf.org](https://wkhtmltopdf.org/downloads.html), dodaj do PATH.
- **Linux (Ubuntu/Debian)**: `sudo apt install wkhtmltopdf`
- **macOS (Homebrew)**: `brew install wkhtmltopdf`

## Uruchamianie programu
Jeśli masz plik wykonywalny (`schedule.exe`):
```sh
schedule.exe
```

Jeśli uruchamiasz skrypt Python:
```sh
python schedule.py
```

## Tworzenie pliku wykonywalnego (Windows/Linux/macOS)
Aby utworzyć plik `.exe` lub samodzielny plik binarny:
```sh
pyinstaller --onefile --add-data "template.html;." --add-data "groups.json;." --hidden-import jinja2 schedule.py
```
Po zakończeniu plik znajdziesz w katalogu `dist/`.

## Pliki projektu
- `schedule.py` – główny skrypt
- `groups.json` – lista grup i osób
- `template.html` – szablon tabeli HTML
- `requirements.txt` – wymagane pakiety

## Konfiguracja `groups.json`
Plik JSON powinien mieć następujący format:
```json
{
  "groups": {
    "Grupa A": ["Jan", "Anna", "Piotr"],
    "Grupa B": ["Kasia", "Tomek", "Maria"]
  }
}
```

## Wynik
Program generuje plik `schedule.pdf` zawierający harmonogram dla każdej grupy.

## Autor
Rafał Miczek

