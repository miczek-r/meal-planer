# Monthly Meal Schedule Generator

## Opis
To narzędzie generuje harmonogram posiłków dla wybranego miesiąca i grup osób, a następnie zapisuje go jako plik PDF w formacie A4 (orientacja pozioma). Każda grupa otrzymuje osobną stronę.

## Wymagania
Program działa jako samodzielny plik wykonywalny, ale jeśli chcesz uruchomić go ze źródła, wymagane są:
- Python 3
- `pip install -r requirements.txt`

## Uruchamianie programu
Do uruchomienia potrzebny jest plik `groups.json` w folderze z plikiem `schedule.exe`.
Jeśli masz plik wykonywalny (`schedule.exe`):
```sh
schedule.exe
```

Jeśli uruchamiasz skrypt Python:
```sh
python src/schedule.py
```

## Tworzenie pliku wykonywalnego (Windows/Linux/macOS)
Aby utworzyć plik `.exe` lub samodzielny plik binarny:
```sh
pyinstaller schedule.spec
```
Po zakończeniu plik znajdziesz w katalogu `dist/`.

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

