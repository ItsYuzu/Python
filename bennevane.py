# szoveg = "ezegyszöveg"
# if "v" in szoveg:
#     print("benne van")
# else: print("nincs benne")

# szoveg ="ezegyszöveg"
# beker= input("Kérem a betűt")
# if beker in szoveg:
#     print(f"{beker}betű benne van a szövegbe")
# else: print ("nincs benne")

hetnapjai = ["Hétfő","Kedd","Szerda","Csütörtök","Péntek","Szombat","Vasárnap"]

hetnapjai_kisbetu = [item.lower() for item in hetnapjai]

beker= input ("Kérem a napot! ").upper()

if beker in hetnapjai_kisbetu:
    print(f"{beker}nap benne van a listában")
else:
    print(f"{beker}nap nincs benne a listában")
    

    



