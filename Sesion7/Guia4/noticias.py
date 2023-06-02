lista_noticias = [{'id': 1, 
                   'titulo':'Ant-Man y la Avispa: Quantumania rompe un récord negativo de Marvel y siembra dudas sobre el futuro de la Fase 5', 
                   'link': 'https://www.espinof.com/estrenos/ant-man-avispa-quantumania-rompe-record-negativo-marvel-siembra-dudas-futuro-fase-5'}, 
                  {'id': 2, 
                   'titulo':'Última hora y noticias en vivo del tiroteo en Louisville, Kentucky', 
                   'link': 'https://cnnespanol.cnn.com/2023/04/10/ultima-hora-noticias-vivo-tiroteo-louisville-kentucky-orix/'},
                  {'id': 3, 
                   'titulo':'Volcán Nevado del Ruiz: se mantienen el movimiento de fluidos y la emisión de ceniza', 
                   'link': 'https://www.lapatria.com/caldas/volcan-nevado-del-ruiz-se-mantienen-el-movimiento-de-fluidos-y-la-emision-de-ceniza'},
                  {'id': 4, 
                   'titulo': 'En Desarrollo: Incendio en una productora de huevos', 
                   'link': 'https://www.tcsahora.com/en-desarrollo-incendio-en-una-productora-de-huevos/'},
                  {'id': 5, 
                   'titulo': 'La película, "Super Mario Bros", bate récord de taquilla tras su estreno', 
                   'link': 'https://www.tcsahora.com/la-pelicula-super-mario-bros-bate-record-de-taquilla-tras-su-estreno/'},
                  {'id': 6, 
                   'titulo': 'Autoridades brindan balance de Plan Verano 2023', 
                   'link': 'https://www.tcsahora.com/autoridades-brindan-balance-de-plan-verano-2023/'},
                  {'id': 7, 
                   'titulo': '¿Sube o baja? Analistas de Bitcoin determinan si el precio de BTC superará los USD 30,000', 
                   'link': 'https://es.cointelegraph.com/news/pop-or-drop-bitcoin-analysts-decide-if-btc-price-will-beat-30k'},
                  {'id': 8, 
                   'titulo': 'Pronto podrás compartir tus estados de WhatsApp en Facebook con un solo paso', 
                   'link': 'https://www.enter.co/chips-bits/apps-software/pronto-podras-compartir-tus-estados-de-whatsapp-en-facebook-con-un-solo-paso/'},
                  {'id': 9, 
                   'titulo': 'Tormenta en Canadá deja dos muertos y miles sin energía', 
                   'link': 'https://www.dw.com/es/tormenta-en-canad%C3%A1-deja-dos-muertos-y-miles-sin-energ%C3%ADa/a-65255590'},
                  {'id': 10, 
                   'titulo': 'Sigue, Manchester City vs. Bayern en vivo: fecha, horarios y cómo ver la Champions League', 
                   'link': 'https://elcomercio.pe/deporte-total/champions-league/manchester-city-vs-bayern-en-vivo-hoy-por-champions-league-a-que-hora-juegan-canal-de-transmision-y-como-seguir-partido-de-ida-cuartos-de-final-via-espn-fox-sports-hbo-max-movistar-liga-de-campeones-y-tnt-sports-lbposting-video-noticia/'},
                  {'id': 11, 
                   'titulo': 'Recopilación de accidentes sucedidos durante Semana Santa', 
                   'link': 'https://www.tcsahora.com/recopilacion-de-accidentes-sucedidos-durante-semana-santa/'},
                  {'id': 12, 
                   'titulo': 'Puerto Rico prohibirá TikTok en dispositivos de gobierno', 
                   'link': 'https://aristeguinoticias.com/1004/mundo/puerto-rico-prohibira-tiktok-en-dispositivos-de-gobierno/'},
                  {'id': 13, 
                   'titulo': 'Mejores apps libres, abiertas y gratuitas para Linux en el 2023', 
                   'link': 'https://blog.desdelinux.net/mejores-apps-linux-2023/'},
                  {'id': 14, 
                   'titulo': 'Crunchyroll suma nuevos animes para este año', 
                   'link': 'https://ramenparados.com/crunchyroll-suma-nuevos-animes-para-este-2023/'},
                  {'id': 15, 
                   'titulo': 'Los mejores podcast de Spotify Estados Unidos para escuchar este día', 
                   'link': 'https://www.infobae.com/noticias/2023/04/10/los-mejores-podcast-de-spotify-estados-unidos-para-escuchar-este-dia/'},
                  {'id': 16, 
                   'titulo': 'Microsoft cambia la forma de toda la vida de capturar pantalla en Windows 11, y no va a gustarte', 
                   'link': 'https://computerhoy.com/windows/microsoft-cambia-forma-toda-vida-capturar-pantalla-windows-11-no-va-gustarte-1227498'},
                  {'id': 17, 
                   'titulo': 'Iglesia El Calvario: así lucen edificios en la zona', 
                   'link': 'https://www.laprensagrafica.com/cultura/Iglesia-El-Calvario-asi-lucen-edificios-en-la-zona-20230408-0057.html'},
                  {'id': 18, 
                   'titulo': 'Muere Julián Figueroa, hijo de Joan Sebastian y Maribel Guardia, a los 28 años', 
                   'link': 'https://www.dallasnews.com/espanol/al-dia/2023/04/10/muere-julian-figueroa-hijo-joan-sebastian-maribel-guardia/'},
                  {'id': 19, 
                   'titulo': 'NETFLIX: esta es la nueva PELÍCULA MÁS VISTA a nivel mundial HOY', 
                   'link': 'https://spoiler.bolavip.com/cine/NETFLIX-esta-es-la-nueva-PELICULA-MAS-VISTA-a-nivel-mundial-HOY-20230410-0009.html'},
                  {'id': 20, 
                   'titulo': 'La filtración de documentos secretos del Pentágono en Internet vuelve a enfrentar a Estados Unidos e Israel', 
                   'link': 'https://elpais.com/internacional/2023-04-09/la-filtracion-de-documentos-secretos-del-pentagono-en-internet-vuelve-a-enfrentar-a-estados-unidos-e-israel.html'}]

# for k, v in lista_noticias[9].items():
#     print(k,":", v)

# print(lista_noticias[18]['titulo']) 
search = "o"

# list_filter = search in lista_noticias[18]['titulo']
# print(list_filter)

for i in range(len(lista_noticias)):
    list_filter = search in lista_noticias[i]['titulo']
    if list_filter == True:
        new_list = lista_noticias[i]
        print(new_list)
    # print(list_filter)
    # if search == true:
    #     list_filter = 