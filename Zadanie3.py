import re  
 
wejscie = "Łącze.txt"  
wyjscie = "Wynik.txt"  
 
wzorzec = r"\b([Żż]abk[aeę]|[Kk]awk[aeę])\b"  
  
uczestnicy = {}  

with open(wejscie, "r", encoding="utf-8") as plik:  
    zawartosc = plik.read()  

znalezione = re.findall(wzorzec, zawartosc)  
 
for wystapienie in znalezione:   
    klucz = wystapienie.lower()  
    if klucz.endswith("ę"):  
        klucz = klucz[:-1] + "a"  

    if klucz not in uczestnicy:  
        uczestnicy[klucz] = {"liczba": 0, "wystapienia": []}  

    uczestnicy[klucz]["liczba"] += 1  
    uczestnicy[klucz]["wystapienia"].append(wystapienie)  

with open(wyjscie, "w", encoding="utf-8") as plik_wy:  
    # Dla każdego uczestnika zapisujemy linię zgodnie z wymaganym formatem  
    for nazwa, dane in uczestnicy.items():  
        linia = f"{nazwa} ({dane['liczba']}) - {', '.join(dane['wystapienia'])}\n"  
        plik_wy.write(linia)  

print("Przetwarzanie zakończone. Wynik zapisano w pliku:", wyjscie)
