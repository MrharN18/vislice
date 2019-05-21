import bottle, model

vislice = model.Vislice()

#ta igra je namenjena testiranju
id_testne_igre = vislice.nova_igra()
(testna_igra, poskus) = vislice.igre[id_testne_igre]


@bottle.get('/')
def prva_stran():
    return bottle.template('vislice/views/index.tpl')


@bottle.get('/igra')
def prikaz_testne_igre():
    return bottle.template('vislice/views/igra.tpl', igra=testna_igra)

bottle.run(debug=True, reloader=True)

