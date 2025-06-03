import json

# 1. Učitaj prvi JSON fajl i uzmi njegove top-level ključeve
with open("test.json", "r", encoding="utf-8") as f1:
    data1 = json.load(f1)

valid_keys = set(data1.keys())

# 2. Učitaj drugi JSON fajl
with open("falcons-vs-gamerlegion-m3-inferno.json", "r", encoding="utf-8") as f2:
    data2 = json.load(f2)

# 3. Obrisi sve ključeve iz drugog fajla koji se ne nalaze u prvom
filtered_data2 = {key: value for key, value in data2.items() if key in valid_keys}

# 4. (Opcionalno) Sačuvaj filtrirani JSON ako želiš
with open("treci-fajl-filtriran.json", "w", encoding="utf-8") as fout:
    json.dump(filtered_data2, fout, indent=4)

print("Završeno. Sačuvani su samo ključevi koji postoje u prvom JSON fajlu.")

print("Top-level ključevi u JSON fajlu:")
for key in data1.keys():
    print("-", key)

print("Top-level ključevi u JSON fajlu:")
for key in data2.keys():
    print("-", key)    