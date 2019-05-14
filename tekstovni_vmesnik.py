import model

# Funkcije, ki geneirajo izpis

def izpis_poraza(igra):
    return 'Porabili ste preveč poskusov. Pravilno geslo je {}.'.format(igra.geslo)

def izpis_zmage(igra):
    return 'Uspešno ste uganili geslo {}.!'.format(igra.geslo)

def izpis_igre(igra):
    tekst = (
        '==============================\n\n'
        '    {trenutno_stanje}\n'
        'Neuspesni poskusi: {poskusi}\n\n'
        '=============================='


    ).format(trenutno_stanje = igra.pravilni_del_gesla(), poskusi = igra.nepravilni_ugibi())

    return tekst

def zahtevaj_vnos():
    vnos = input('Poskusi uganiti črko: ')
    return vnos

def preveri_vnos(vnos):
    if len(vnos) != 1:
        print('Neveljaven vnos! Vnesi zgolj eno črko.')
        return False
    else:
        return True


# Izvajanje vmesnika

def pozeni_vmesnik():
    igra = model.nova_igra()

    while True:
        # izpisemo stanje
        print(izpis_igre(igra))
        # igralec ugiba
        poskus = zahtevaj_vnos() # se ni napisano !!!
        if not preveri_vnos(poskus):
            continue
        igra.ugibaj(poskus)
        # preverimo, ce je igre konec
        if igra.poraz(): # if rezultat == model.poraz()
            print(izpis_poraza(igra))
        elif igra.zmaga():
            print(izpis_zmage(igra))
        return
    return

# zares pozeni igro
pozeni_vmesnik()

