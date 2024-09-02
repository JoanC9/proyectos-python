from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import pandas as pd


app = Flask(__name__)

def buscar_pagina(dirrecion:str):
    
    url = dirrecion
    pagina = requests.get(url)
    s = BeautifulSoup(pagina.text,"lxml")
    return s 

def buscar_texto(elemento, tag_padre:str, nombre_clase_padre:str, tag_hijo:str, muchos_tag_texto=False):
    resultados = []
    padres = elemento.find_all(tag_padre, class_=nombre_clase_padre)
    for padre in padres:
        if muchos_tag_texto:
            hijos = padre.find_all(tag_hijo)
            
            resultados.extend([hijo.text.strip() for hijo in hijos])
        else:
            hijo = padre.find(tag_hijo)
            if hijo:
                resultados.append(hijo.text.strip())
    return resultados

 
pag_listas1 = buscar_pagina("https://www.ecologiaverde.com/region-andina-caracteristicas-flora-y-fauna-2527.html")
text_listas1 = buscar_texto(pag_listas1,"div","apartado","li",muchos_tag_texto=True)


tli1=""
tli9=""
tli19=""
tli20=""


for btl1 in text_listas1:
    
    if "Cuenta con tres cordilleras: dentro de ellas encontramos" in btl1:
        tli1 = btl1
    elif "Vegetación destinada al cultivo: ya que la región cuenta con" in btl1:
        tli9 = btl1
    elif "Cóndor (Vultur gryphus): es un ave con unas alas de gran" in btl1:
        tli19 = btl1
    elif "Colibrí (Trochilidae): es un ave de pequeño tamaño" in btl1:
        tli20 = btl1


pag_tex_chingaza = buscar_pagina("https://www.parquesnacionales.gov.co/nuestros-parques/pnn-chingaza/")
tex_chingaza = buscar_texto(pag_tex_chingaza,"div","wpb_wrapper","p",muchos_tag_texto=True)


tpc1 = ""
tpc2 = ""
tpc3 = ""



for btexchin in tex_chingaza:
    if "El Parque Nacional Natural Chingaza es un tesoro" in btexchin:
        tpc1 = btexchin
    elif "El PNN está ubicado en la cordillera oriental de los Andes" in btexchin:
        tpc2 = btexchin
    elif "Sus ecosistemas predominantes son los bosques alto" in btexchin:
        tpc3 = btexchin
        
pag_tex_sumapaz = buscar_pagina("https://old.parquesnacionales.gov.co/portal/es/parques-nacionales/parque-nacional-natural-sumapaz/")
text_sumapaz = buscar_texto(pag_tex_sumapaz,"div","entry-content","p",muchos_tag_texto=True)

tps1 = ""
tps2 = ""

for btextsuma in text_sumapaz:
    if "En el Parque Nacional Natural Sumapaz se encuentran representados dos" in btextsuma:
        tps1 = btextsuma
    elif "Esta área protegida del Sumapaz se caracteriza por sus altos" in btextsuma:
        tps2 = btextsuma

pag_text_zoque = buscar_pagina("https://www.reservaelzoque.co/la-regin")
text_zoque = buscar_texto(pag_text_zoque,"div","sqs-html-content","p",muchos_tag_texto=False)

trz = ""

for btextzoque in text_zoque:
    if "Este extraordinario ecosistema es el encargado de la producción" in btextzoque:
        trz = btextzoque
        
pag_texto_pisba = buscar_pagina("https://old.parquesnacionales.gov.co/portal/es/parques-nacionales/parque-nacional-natural-pisba/")
text_pisba = buscar_texto(pag_texto_pisba,"div","entry-content","p",muchos_tag_texto=True)

tpp1 = "" 
tpp2 = ""

for btextpisba in text_pisba:
    if "El Parque Nacional Natural Pisba tiene una localización estratégica" in btextpisba:
        tpp1 = btextpisba
    elif "Posee elementos únicos y de gran relevancia que realzan su importancia" in btextpisba:
        tpp2 = btextpisba
        
pag_texto_oceta = buscar_pagina("https://situr.boyaca.gov.co/atractivo-turistico/paramo-de-oceta-2/")
tex_oceta = buscar_texto(pag_texto_oceta,"div","wpb_wrapper","p",muchos_tag_texto=False)    

tpo1 = ""

for btextoceta in tex_oceta:
    if "Es considerado, por algunos, como el más hermoso del mundo" in btextoceta:
        tpo1 = btextoceta
        
pag_texto_iguaque = buscar_pagina("https://situr.boyaca.gov.co/atractivo-turistico/santuario-de-flora-y-fauna-iguaque/")
text_iguaque = buscar_texto(pag_texto_iguaque,"div","wpb_wrapper","p",muchos_tag_texto=False)

tri1 = "" 

for btextiguaque in text_iguaque:
    if "La reserva de Iguaque está conformada por 6.750 hectáreas, de páramo" in btextiguaque:
        tri1 = btextiguaque
        
# pag_texto_rabanal = buscar_pagina("https://www.corpoboyaca.gov.co/noticias/parque-natural-regional-rabanal-mucho-mas-que-una-de-paramo/")
# text_rabanal = buscar_texto(pag_texto_rabanal,"div","px-sm-3 content","p",muchos_tag_texto=True)

text_rabanal = ''
prr1 = ""
tprr2 = "" 

for btextrabanal in text_rabanal:
    if "Para el director de la Corporación, Herman Amaya es" in btextrabanal:
        prr1 = btextrabanal
    elif "“El área del Páramo de Rabanal reporta un total de 44 especies" in btextrabanal:
        tprr2 = btextrabanal
    else:
        prr1 = 'Para el director de la Corporación, Herman Amaya es importante resaltar que el PNR Rabanal, es fuente abastecedora de agua para las cuencas del embalse La Esmeralda de la Central Hidroeléctrica de Chivor (una de las primeras productoras de energía eléctrica del país), de igual manera este sistema irriga más de 1.000.000 de hectáreas de esta región del país y aporta aguas a una población estimada de 300.000 habitantes.'
        tprr2 = 'El área del Páramo de Rabanal reporta un total de 44 especies de aves, lo que corresponde aproximadamente al 4,91 porciento de las especies que Avibase.'


@app.route('/')
def pagina():
    
    li1 = tli1[0:-139]
    
    li9 = tli9[0:-63]
   
    li19 = tli19[0:-63]
    
    li20 = tli20[0:-120]
    
    tc1 = tpc1
    tc2 = tpc2
    tc3 = tpc3
    
    tprr1 = prr1[50:-1]
    
    #leer el archivo csv
    df = pd.read_csv('cocreacion3/biodiversidad.csv')
    
    # Convertir el DataFrame a un diccionario para pasarlo a la plantilla
    data = df.to_dict(orient='records')

        
    return(render_template("index.html", htli1 = li1, htli9 = li9, htli19 = li19, htli20 = li20,
                           htc1 = tc1, htc2 = tc2, htc3 = tc3, hts1 = tps1, hts2 = tps2, htrz = trz,
                           htpp1 = tpp1, htpp2 =tpp2,htpo1 = tpo1, htri1 = tri1, htprr1 = tprr1, htprr2 = tprr2, biodiversidad=data))

if __name__ == '__main__':
    app.run(debug=True)