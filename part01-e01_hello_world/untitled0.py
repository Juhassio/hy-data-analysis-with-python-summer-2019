import sqlite3
import random
import string
import time
from time import perf_counter
from sqlite3 import Error

def toiminto1():
    try:
        db = sqlite3.connect("HT-tietokanta.db")
        db.isolation_level = None

        c = db.cursor()

        c.execute("CREATE TABLE Paikat (paikkaid INTEGER PRIMARY KEY, paikannimi TEXT)")
        c.execute("CREATE TABLE Asiakkaat (asiakasid INTEGER PRIMARY KEY, asiakas TEXT)")
        c.execute("CREATE TABLE Paketit (pakettiid INTEGER PRIMARY KEY, seurantakoodi TEXT, asiakasid INT)")
        c.execute("CREATE TABLE Tapahtumat (tapahtumaid INTEGER PRIMARY KEY, pakettiid TEXT, paikkaid INT, kuvaus TEXT, \
         tapahtumaaika TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL)")

        print("Tietokanta luotu")
    
def toiminto2():
        
    try:
        db = sqlite3.connect("HT-tietokanta.db")
        db.isolation_level = None

        c = db.cursor()

        print("Anna paikan nimi:")
        paikannimi = input().lower()
        if len(paikannimi) < 1:
            print("Paikannimessä täytyy olla ainakin yksi merkki. Yritä uudelleen.")
        else:
            c.execute("SELECT paikannimi FROM Paikat WHERE paikannimi=?", [paikannimi])
            tiedot = c.fetchone()
            if tiedot == None:
                c.execute("INSERT INTO Paikat(paikannimi) VALUES (?)", [paikannimi])
                print("Paikka lisätty")
            else:
                print("Paikka on jo tietokannassa.")
    except Error:
        print("Tietokantaa ei ole vielä luotu. Käytä ensin toimintoa 1.")
def toiminto3():
    try:
        db = sqlite3.connect("HT-tietokanta.db")
        db.isolation_level = None

        c = db.cursor()

        print("Anna asiakkaan nimi:")
        asiakas = input().lower()
        if len(asiakas) < 1:
            print("Asiakkaan nimessä täytyy olla ainakin yksi merkki. Yritä uudelleen.")
        else:
            c.execute("SELECT asiakas FROM Asiakkaat WHERE asiakas=?", [asiakas])
            tiedot = c.fetchone()
            if tiedot == None:
                c.execute("INSERT INTO Asiakkaat(asiakas) VALUES (?)", [asiakas])
                print("Asiakas lisätty")
            else:
                print("Asiakas on jo tietokannassa.")
    except Error:
        print("Tietokantaa ei ole vielä luotu. Käytä ensin toimintoa 1.")

def toiminto4():
    try:
        db = sqlite3.connect("HT-tietokanta.db")
        db.isolation_level = None

        c = db.cursor()

        print("Anna asiakkaan nimi:")
        asiakas = input().lower()

        c.execute("SELECT asiakas FROM Asiakkaat WHERE asiakas=?", [asiakas])
        tiedot = c.fetchone()
        if tiedot != None:
            print("Asiakas", tiedot[0], "löytyi")
            print("Anna paketin seurantakoodi:")
            seurantakoodi = input().lower()
            c.execute("SELECT seurantakoodi FROM Paketit WHERE seurantakoodi = ?", [seurantakoodi])
            tiedot = c.fetchone()
            if tiedot != None:
                    print("Seurantakoodi on jo käytetty. Pakettia ei lisätty. Yritä uudelleen toisella seurantakoodilla.")

            else:
                c.execute("INSERT INTO Paketit(seurantakoodi,asiakasid) VALUES (?,(SELECT asiakasid FROM Asiakkaat WHERE asiakas =?))", [seurantakoodi,asiakas])
                print("Paketti lisätty.")

        else:
            print("Asiakasta ei löytynyt")
    except Error:
        print("Tietokantaa ei ole vielä luotu. Käytä ensin toimintoa 1.")

def toiminto5():
    try:
        db = sqlite3.connect("HT-tietokanta.db")
        db.isolation_level = None

        c = db.cursor()

        print("Anna tapahtuman paikka:")
        paikannimi = input().lower()
        c.execute("SELECT paikannimi FROM Paikat WHERE paikannimi=?", [paikannimi])
        tiedot = c.fetchone()
        if tiedot != None:
            print("Anna paketin seurantakoodi:")
            seurantakoodi = input().lower()
            c.execute("SELECT seurantakoodi FROM Paketit WHERE seurantakoodi=?", [seurantakoodi])
            tiedot = c.fetchone()
            if tiedot != None:
                print("Anna tapahtuman kuvaus:")
                kuvaus = input().lower()
                c.execute("INSERT INTO Tapahtumat(pakettiid,paikkaid,kuvaus) VALUES ((SELECT pakettiid \
                 FROM Paketit WHERE seurantakoodi=?),(SELECT paikkaid FROM Paikat WHERE paikannimi =?),?)",[seurantakoodi,paikannimi,kuvaus])
                print("Tapahtuma tallennettu.")
            else:
                print("Seurantakoodia ei ole olemassa.")
        else:
            print("Paikkaa ei ole olemassa.")
    except Error:
        print("Tietokantaa ei ole vielä luotu. Käytä ensin toimintoa 1.")
def toiminto6():
    try:
        db = sqlite3.connect("HT-tietokanta.db")
        db.isolation_level = None

        c = db.cursor()

        print("Anna paketin seurantakoodi:")
        seurantakoodi = input().lower()
        c.execute("SELECT seurantakoodi FROM Paketit WHERE seurantakoodi=?", [seurantakoodi])
        tiedot = c.fetchone()
        if tiedot != None:

            c.execute("SELECT COUNT(kuvaus) FROM Tapahtumat WHERE pakettiid=(SELECT pakettiid FROM Paketit WHERE seurantakoodi = ?)", [seurantakoodi])
            apumuuttuja = c.fetchone()
            tapahtumienmaara = int(apumuuttuja[0])

            c.execute("SELECT tapahtumaaika FROM Tapahtumat WHERE pakettiid=(SELECT pakettiid FROM Paketit WHERE seurantakoodi =?)", [seurantakoodi])
            tapahtumaajat = c.fetchall()

            c.execute("SELECT kuvaus FROM Tapahtumat WHERE pakettiid=(SELECT pakettiid FROM Paketit WHERE seurantakoodi =?)",
                [seurantakoodi])
            kuvaukset = c.fetchall()


            i = 0
            while i < tapahtumienmaara:
                print("Aikaleima:", str(tapahtumaajat[i])[2:-3])
                tapahtumaaikaapu = str(tapahtumaajat[i])[2:-3]
                c.execute("SELECT paikannimi FROM Paikat WHERE paikkaid = (SELECT paikkaid FROM Tapahtumat WHERE tapahtumaaika =?)", [tapahtumaaikaapu])
                paikka = c.fetchall()
                print("Tapahtuman paikka", str(paikka)[3:-4])
                print("Tapahtuman kuvaus:", str(kuvaukset[i])[2:-3])
                print("")
                i = i+1
    except Error:
        print("Tietokantaa ei ole vielä luotu. Käytä ensin toimintoa 1.")
def toiminto7():
    try:
        db = sqlite3.connect("HT-tietokanta.db")
        db.isolation_level = None

        c = db.cursor()

        print("Anna asiakkaan nimi:")
        asiakas = input().lower()

        c.execute("SELECT asiakas FROM Asiakkaat WHERE asiakas=?", [asiakas])
        tiedot = c.fetchone()
        if tiedot != None:
            print("Asiakas", tiedot[0], "löytyi.")
            c.execute("SELECT COUNT(pakettiid) FROM Paketit  WHERE asiakasid IN (SELECT asiakasid FROM Asiakkaat WHERE asiakas = ? )", [asiakas])
            apumuuttuja = c.fetchone()
            montakopakettia = int(apumuuttuja[0])
            if montakopakettia == 0:
                print("Asiakkaalla ei kuitenkaan ole paketteja.")
            else:
                i = 0
                print("Asiakkaan paketit ovat:")
                while i < montakopakettia:
                    c.execute("SELECT seurantakoodi FROM Paketit WHERE asiakasid IN (SELECT asiakasid FROM Asiakkaat WHERE asiakas = ?)", [asiakas])
                    seurantakoodit = c.fetchall()
                    yksiseurantakoodi = str(seurantakoodit[i])[2:-3]
                    print("Paketti", str(seurantakoodit[i])[2:-3])

                    c.execute("SELECT COUNT(kuvaus) FROM Tapahtumat WHERE pakettiid=(SELECT pakettiid FROM Paketit WHERE seurantakoodi = ?)",[yksiseurantakoodi])
                    tapahtumienmaarapaketille = c.fetchone()
                    print("Tapahtumien määrä paketille:", str(tapahtumienmaarapaketille)[1:-2])
                    i = i+1

        else:
            print("Asiakasta ei löytynyt")
    except Error:
        print("Tietokantaa ei ole vielä luotu. Käytä ensin toimintoa 1.")
def toiminto8():
    try:
        db = sqlite3.connect("HT-tietokanta.db")
        db.isolation_level = None

        c = db.cursor()

        print("Syötä paikan nimi:")
        paikannimi = input().lower()
        c.execute("SELECT paikannimi FROM Paikat WHERE paikannimi=?", [paikannimi])
        tiedot = c.fetchone()
        if tiedot != None:
            print("Paikka löytyi. Syötä päivämäärä muodossa YYYY-MM-DD:")
            paivamaara = input().lower()
            c.execute("SELECT count(kuvaus) FROM Tapahtumat WHERE date(?) AND paikkaid = (SELECT paikkaid FROM Paikat WHERE paikannimi=?) ", [paivamaara, paikannimi])
            tapahtumienmaarapaketille = c.fetchone()
            print("Tapahtumien määrä paketeille syötettynä päivänä:", str(tapahtumienmaarapaketille)[1:-2])

        else:
            print("Paikkaa ei löytynyt. Yritä uudelleen.")
    except Error:
        print("Paikkaa ei voitu tallentaa, sillä tietokantaa ei ole vielä luotu. Käytä ensin toimintoa 1.")

def toiminto9():
    try:
        db = sqlite3.connect("HT-tietokanta.db")
        db.isolation_level = None

        c = db.cursor()
        print("Tämä funktio testaa tietokannan suorituskykyä. Testi alkaa.")
        i = 1
        suorituskykymittaus_alku = perf_counter()
        c.execute("BEGIN TRANSACTION;")
        while i < 1001:
            testipaikka = "p" + str(i)
            c.execute("INSERT INTO Paikat(paikannimi) VALUES (?)", [testipaikka])
            testiasiakas = "a" + str(i)
            c.execute("INSERT INTO Asiakkaat(asiakas) VALUES (?)", [testiasiakas])
            seurantakoodi = "c" + str(i)
            testiasiakas2 = str(random.randint(1, 1001))
            c.execute("INSERT INTO Paketit(seurantakoodi, asiakasid) VALUES (?,?)", [seurantakoodi,testiasiakas2])
            i = i+1
        o = 1
        while o < 1000001:
            c.execute("INSERT INTO Tapahtumat(pakettiid, kuvaus) VALUES (?,?)", [testiasiakas2, "kuvaus"])
            o = o+1

        c.execute("COMMIT;")
        suorituskykymittaus_loppu = perf_counter()
        print("Kirjoitusaika:",
              suorituskykymittaus_loppu - suorituskykymittaus_alku)
        suorituskykymittaus_alku = perf_counter()
        z = 1

        while z < 1001:
            testiasiakas = "a" + str(random.randint(1,1001))
            c.execute("SELECT count(seurantakoodi) FROM Paketit JOIN Asiakkaat ON \
            Paketit.asiakasid = Asiakkaat.asiakasid WHERE Paketit.asiakasid = ?", [testiasiakas])
            testipaketti = "c" + str(random.randint(1,1001))
            c.execute("SELECT count(tapahtumaid) FROM Tapahtumat JOIN Paketit ON \
            Tapahtumat.pakettiid = Tapahtumat.pakettiid WHERE Paketit.asiakasid = ?",[testipaketti])
            z = z+1




        suorituskykymittaus_loppu = perf_counter()
        print("Lukuaika:",
              suorituskykymittaus_loppu - suorituskykymittaus_alku)

    except Error:
        print("Paikkaa ei voitu tallentaa, sillä tietokantaa ei ole vielä luotu. Käytä ensin toimintoa 1.")


def suorituskyky2():
    try:
        db = sqlite3.connect("HT-tietokanta.db")
        db.isolation_level = None

        c = db.cursor()
        c.execute("CREATE INDEX idx_paketti ON Paketit (seurantakoodi)")
        c.execute("CREATE INDEX idx_paketti2 ON Paketit (pakettiid)")
        c.execute("CREATE INDEX idx_paketti3 ON Paketit (asiakasid)")
        c.execute("CREATE INDEX idx_asiakas ON Asiakkaat (asiakas)")
        c.execute("CREATE INDEX idx_paikka ON Paikat (paikannimi)")
        c.execute("CREATE INDEX idx_paketit_tapahtumissa ON Tapahtumat (pakettiid)")
        c.execute("CREATE INDEX paketidx ON Paketit (pakettiid)")
        print("Tämä funktio testaa tietokannan suorituskykyä indeksien kanssa. Testi alkaa.")
        i = 1
        suorituskykymittaus_alku = perf_counter()
        c.execute("BEGIN TRANSACTION;")
        while i < 1001:
            testipaikka = "p" + str(i)
            c.execute("INSERT INTO Paikat(paikannimi) VALUES (?)", [testipaikka])
            testiasiakas = "a" + str(i)
            c.execute("INSERT INTO Asiakkaat(asiakas) VALUES (?)", [testiasiakas])
            seurantakoodi = "c" + str(i)
            testiasiakas2 = str(random.randint(1, 1001))
            c.execute("INSERT INTO Paketit(seurantakoodi, asiakasid) VALUES (?,?)", [seurantakoodi, testiasiakas2])
            i = i + 1
        o = 1
        while o < 1000001:
            c.execute("INSERT INTO Tapahtumat(pakettiid, kuvaus) VALUES (?,?)", [testiasiakas2, "kuvaus"])
            o = o + 1

        c.execute("COMMIT;")
        suorituskykymittaus_loppu = perf_counter()
        print("Kirjoitusaika:",
              suorituskykymittaus_loppu - suorituskykymittaus_alku)
        suorituskykymittaus_alku = perf_counter()
        z = 1

        while z < 1001:
            testiasiakas = "a" + str(random.randint(1, 1001))

            c.execute(
                "SELECT count(seurantakoodi) FROM Paketit JOIN Asiakkaat ON \
            Paketit.asiakasid = Asiakkaat.asiakasid WHERE Paketit.asiakasid = ?",[testiasiakas])
            testipaketti = "c" + str(random.randint(1, 1001))
            c.execute("SELECT count(tapahtumaid) FROM Tapahtumat JOIN Paketit ON \
            Tapahtumat.pakettiid = Tapahtumat.pakettiid WHERE Paketit.asiakasid = ?",[testipaketti])
            z = z + 1



        suorituskykymittaus_loppu = perf_counter()
        print("Lukuaika:",
              suorituskykymittaus_loppu - suorituskykymittaus_alku)
    except Error:
        print("Tietokantaa ei ole vielä luotu. Käytä ensin toimintoa 1.")

def main():

    print("Tervetuloa!")
    while True:
        valinta = input("Valitse toiminto (1-9) tai lopeta ohjelma valitsemalla q: ")
        if valinta == "1":
            toiminto1()
        elif valinta == "2":
            toiminto2()
        elif valinta == "3":
            toiminto3()
        elif valinta == "4":
            toiminto4()
        elif valinta == "5":
            toiminto5()
        elif valinta == "6":
            toiminto6()
        elif valinta == "7":
            toiminto7()
        elif valinta == "8":
            toiminto8()
        elif valinta == "9":
            toiminto9()
            suorituskyky2()
        elif valinta == "q":
            quit()
        else:
            pass

main()