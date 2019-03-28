def provincias(doc):
    return doc.xpath('//PROVINCIA/NOMBRE/text()')
def contaradar(doc):
    return doc.xpath('count(//CARRETERA/RADAR)')
def carretera(doc,prov):
    return doc.xpath('//CARRETERA/DENOMINACION/../../NOMBRE=%s'%prov)
def contarcarretera(carretera,doc):
    return doc.xpath('count(//CARRETERA[DENOMINACION="%s"]/RADAR)'%carretera)
def latitud(carretera,doc):
    return doc.xpath('//CARRETERA[DENOMINACION="%s"]/RADAR/PUNTO_INICIAL/LATITUD/text()'%carretera)
def longitud(carretera,doc):
    return doc.xpath('//CARRETERA[DENOMINACION="%s"]/RADAR/PUNTO_INICIAL/LONGITUD/text()'%carretera)
