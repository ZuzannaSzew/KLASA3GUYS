import sqlite3



conn = sqlite3.connect("cmentarz.db")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# Tworzymy tabelę, jeśli jeszcze nie istnieje
cursor.execute("""
CREATE TABLE IF NOT EXISTS groby (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    imie TEXT,
    wiek INTEGER
)
""")



def dodaj(imie: str, wiek: int):
    cursor.execute("INSERT INTO groby (imie, wiek) VALUES (?, ?)", (imie, wiek))
    conn.commit()



def wyswietl_dane():
    cursor.execute("SELECT * FROM groby")
    rekordy = cursor.fetchall()
    if rekordy:
        for r in rekordy:
            print(f"ID: {r['id']} | Imię: {r['imie']} | Wiek: {r['wiek']}")
    else:
        print("⚠️ Brak wpisów w bazie.")



while True:
    print("\nWybierz opcję:")
    print("  dodaj  - Dodaj zmarłego użytkownika")
    print("  pokaz  - Wyświetl dane z cmentarza")
    print("  wyjdz  - Zakończ program")

    inp = input("> ").strip().lower()

    if inp == "dodaj":
        imie = input("Imię: ")
        try:
            wiek = int(input("Wiek: "))
            dodaj(imie, wiek)
            print("✅ Dodano do bazy.")
        except ValueError:
            print("❌ Błąd: wiek musi być liczbą.")
    elif inp == "pokaz":
        wyswietl_dane()
    elif inp == "wyjdz":
        break
    else:
        print("❓ Nieznana komenda.")

conn.close()
print("👋 Program zakończony.")
