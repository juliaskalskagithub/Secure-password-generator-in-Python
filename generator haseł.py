import random
import string

def generowanie_bezpiecznego_hasla(dlugosc_hasla, duze_litery, male_litery, cyfry, specjalne_znaki):
    duze_litery_znaki = string.ascii_uppercase if duze_litery else ''
    male_litery_znaki = string.ascii_lowercase if male_litery else ''
    cyfry_znaki = string.digits if cyfry else ''
    specjalne_znaki = '!@#$%^&*' if specjalne_znaki else ''

    wszystkie_znaki = duze_litery_znaki + male_litery_znaki + cyfry_znaki + specjalne_znaki

    haslo = ''.join(random.choice(wszystkie_znaki) for _ in range(dlugosc_hasla))

    return haslo

def main():
    print("Generator bezpiecznych haseł")

    hasla = []  

    while True:
        try:
            dlugosc_hasla = int(input("Podaj długość hasła (co najmniej 8 znaków): "))

            if dlugosc_hasla >= 8:
                break
            else:
                print("Długość hasła musi mieć co najmniej 8 znaków. Spróbuj ponownie.")
        except ValueError:
            print("Podaj liczbę całkowitą.")

    while True:
        duze_litery = input("Czy hasło powinno zawierać duże litery? (Tak/Nie): ").strip().lower()
        if duze_litery in ["tak", "nie"]:
            break
        else:
            print("Odpowiedz 'tak' lub 'nie'. Spróbuj ponownie.")

    while True:
        male_litery = input("Czy hasło powinno zawierać małe litery? (Tak/Nie): ").strip().lower()
        if male_litery in ["tak", "nie"]:
            break
        else:
            print("Odpowiedz 'tak' lub 'nie'. Spróbuj ponownie.")

    while True:
        cyfry = input("Czy hasło powinno zawierać cyfry? (Tak/Nie): ").strip().lower()
        if cyfry in ["tak", "nie"]:
            break
        else:
            print("Odpowiedz 'tak' lub 'nie'. Spróbuj ponownie.")

    while True:
        specjalne_znaki = input("Czy hasło powinno zawierać znaki specjalne? (Tak/Nie): ").strip().lower()
        if specjalne_znaki in ["tak", "nie"]:
            break
        else:
            print("Odpowiedz 'tak' lub 'nie'. Spróbuj ponownie.")

    while True:
        try:
            ilosc_hasel = int(input("Ile haseł chcesz wygenerować? "))
            break
        except ValueError:
            print("Podaj liczbę całkowitą.")

    for _ in range(ilosc_hasel):
        haslo = generowanie_bezpiecznego_hasla(dlugosc_hasla, duze_litery == 'tak', male_litery == 'tak', cyfry == 'tak', specjalne_znaki == 'tak')
        hasla.append(haslo)  
        print("Oto wygenerowane hasło:")
        print(haslo)

    zapisz_do_pliku = input("Czy chcesz zapisać wygenerowane hasła do pliku? (Tak/Nie): ").strip().lower()
    if zapisz_do_pliku == 'tak':
        nazwa_pliku = input("Podaj nazwę pliku: ")
        sciezka = r"C:\Users\Asus\Documents\studia\3 rok\1 semestr\python\\" + nazwa_pliku
        with open(sciezka, 'w') as plik:
            plik.write("Wygenerowane hasła:\n")
            for haslo in hasla:
                plik.write(haslo + '\n')

if __name__ == "__main__":
    main()
