# Import the dependencies.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Import the time library and the datetime module from the datetime library 
import time
from datetime import datetime as dt
from citipy import citipy
import requests
# Import the API key.
from config import weather_api_key
# Create a set of random latitude and longitude combinations.
lats = np.random.uniform(low = -90.00, high = 90.00, size = 1500)
lngs = np.random.uniform(low = -180.00, high = 180.00, size = 1500)
lat_lngs = zip(lats,lngs)
# Add the latitudes and longitudes to a list.
coordinates = list(lat_lngs)
# Create a list for holding the cities.

cities =[]

#Identify the nearest city for each lattitude and longitude combination
for coordinate in coordinates:
    city = citipy.nearest_city(coordinate[0],coordinate[1]).city_name
    
    # check for the city if already exists
    if city not in cities:
        cities.append(city)
# Create an empty list to hold the weather data.
# Starting URL for Weather Map API Call.
url = "http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=" + weather_api_key
city_data = []
# Print the beginning of the logging.
print("Beginning Data Retrieval     ")
print("-----------------------------")

# Create counters.
record_count = 1
set_count = 1
Beginning Data Retrieval     
-----------------------------
# Loop through all the cities in the list.
for i, city in enumerate(cities):
    
    # Group cities in sets of 50 for logging purposes.
    if (i%50 == 0 and i >= 50):
        set_count += 1
        record_count = 1
        time.sleep(60)
    
    # Create endpoint URL with each city.
    city_url = url + "&q=" + city.replace(" ","+")
    print(f"Processing Record {record_count} of Set {set_count} | {city}")
    record_count += 1
    try:
        # Parse the JSON and retrieve data.
        city_weather = requests.get(city_url).json()
        # Parse out the needed data.
        city_lat = city_weather["coord"]["lat"]
        city_lng = city_weather["coord"]["lon"]
        city_max_temp = city_weather["main"]["temp_max"]
        city_humidity = city_weather["main"]["humidity"]
        city_clouds = city_weather["clouds"]["all"]
        city_wind = city_weather["wind"]["speed"]
        city_country = city_weather["sys"]["country"]
        # Convert the date to ISO standard.
        city_date = dt.utcfromtimestamp(city_weather["dt"]).strftime('%Y-%m-%d %H:%M:%S')
        # Append the city information into city_data list.
        city_data.append({"City": city.title(),
                          "Lat": city_lat,
                          "Lng": city_lng,
                          "Max Temp": city_max_temp,
                          "Humidity": city_humidity,
                          "Cloudiness": city_clouds,
                          "Wind Speed": city_wind,
                          "Country": city_country,
                          "Date": city_date})

# If an error is experienced, skip the city.
    except:
        print(f"City {city} not found. Skipping...")
        pass

# Indicate that Data Loading is complete.
print("-----------------------------")
print("Data Retrieval Complete      ")
print("-----------------------------")
Processing Record 1 of Set 1 | jamestown
Processing Record 2 of Set 1 | cherskiy
Processing Record 3 of Set 1 | kaitangata
Processing Record 4 of Set 1 | pankrushikha
Processing Record 5 of Set 1 | fortuna
Processing Record 6 of Set 1 | nome
Processing Record 7 of Set 1 | avanigadda
Processing Record 8 of Set 1 | kapaa
Processing Record 9 of Set 1 | punta arenas
Processing Record 10 of Set 1 | castro
Processing Record 11 of Set 1 | mount gambier
Processing Record 12 of Set 1 | laguna
Processing Record 13 of Set 1 | kalmunai
Processing Record 14 of Set 1 | severo-kurilsk
Processing Record 15 of Set 1 | umzimvubu
City umzimvubu not found. Skipping...
Processing Record 16 of Set 1 | hailar
Processing Record 17 of Set 1 | redlands
Processing Record 18 of Set 1 | luderitz
Processing Record 19 of Set 1 | rawson
Processing Record 20 of Set 1 | mataura
Processing Record 21 of Set 1 | east london
Processing Record 22 of Set 1 | vao
Processing Record 23 of Set 1 | port elizabeth
Processing Record 24 of Set 1 | kamenka
Processing Record 25 of Set 1 | nizhneyansk
City nizhneyansk not found. Skipping...
Processing Record 26 of Set 1 | hindupur
Processing Record 27 of Set 1 | mar del plata
Processing Record 28 of Set 1 | la rioja
Processing Record 29 of Set 1 | porto santo
Processing Record 30 of Set 1 | altay
Processing Record 31 of Set 1 | avarua
Processing Record 32 of Set 1 | esna
Processing Record 33 of Set 1 | avera
Processing Record 34 of Set 1 | fare
Processing Record 35 of Set 1 | albany
Processing Record 36 of Set 1 | hilo
Processing Record 37 of Set 1 | ushuaia
Processing Record 38 of Set 1 | puerto ayora
Processing Record 39 of Set 1 | qaanaaq
Processing Record 40 of Set 1 | nikolskoye
Processing Record 41 of Set 1 | grand centre
City grand centre not found. Skipping...
Processing Record 42 of Set 1 | rikitea
Processing Record 43 of Set 1 | santa cruz
Processing Record 44 of Set 1 | bur gabo
City bur gabo not found. Skipping...
Processing Record 45 of Set 1 | hobart
Processing Record 46 of Set 1 | ilhabela
Processing Record 47 of Set 1 | constitucion
Processing Record 48 of Set 1 | cape town
Processing Record 49 of Set 1 | bengkulu
Processing Record 50 of Set 1 | busselton
Processing Record 1 of Set 2 | bhola
Processing Record 2 of Set 2 | bambous virieux
Processing Record 3 of Set 2 | sao joao da barra
Processing Record 4 of Set 2 | flinders
Processing Record 5 of Set 2 | husavik
Processing Record 6 of Set 2 | rocha
Processing Record 7 of Set 2 | ardistan
City ardistan not found. Skipping...
Processing Record 8 of Set 2 | hofn
Processing Record 9 of Set 2 | arraial do cabo
Processing Record 10 of Set 2 | beachwood
Processing Record 11 of Set 2 | iqaluit
Processing Record 12 of Set 2 | san pedro
Processing Record 13 of Set 2 | akyab
Processing Record 14 of Set 2 | mahebourg
Processing Record 15 of Set 2 | ribeira grande
Processing Record 16 of Set 2 | monze
Processing Record 17 of Set 2 | beloha
Processing Record 18 of Set 2 | itanagar
Processing Record 19 of Set 2 | atuona
Processing Record 20 of Set 2 | rungata
City rungata not found. Skipping...
Processing Record 21 of Set 2 | hirara
Processing Record 22 of Set 2 | attawapiskat
City attawapiskat not found. Skipping...
Processing Record 23 of Set 2 | georgetown
Processing Record 24 of Set 2 | fairbanks
Processing Record 25 of Set 2 | dikson
Processing Record 26 of Set 2 | tukrah
Processing Record 27 of Set 2 | kahului
Processing Record 28 of Set 2 | cabo san lucas
Processing Record 29 of Set 2 | vaini
Processing Record 30 of Set 2 | kushima
Processing Record 31 of Set 2 | provideniya
Processing Record 32 of Set 2 | hamilton
Processing Record 33 of Set 2 | krasnoselkup
Processing Record 34 of Set 2 | pak phanang
Processing Record 35 of Set 2 | mastung
Processing Record 36 of Set 2 | akdepe
Processing Record 37 of Set 2 | bredasdorp
Processing Record 38 of Set 2 | hermanus
Processing Record 39 of Set 2 | zabol
Processing Record 40 of Set 2 | bluff
Processing Record 41 of Set 2 | guerrero negro
Processing Record 42 of Set 2 | opunake
Processing Record 43 of Set 2 | butaritari
Processing Record 44 of Set 2 | san cristobal
Processing Record 45 of Set 2 | ngaoundere
Processing Record 46 of Set 2 | khatanga
Processing Record 47 of Set 2 | amderma
City amderma not found. Skipping...
Processing Record 48 of Set 2 | lokosovo
Processing Record 49 of Set 2 | fort nelson
Processing Record 50 of Set 2 | barrow
Processing Record 1 of Set 3 | itarema
Processing Record 2 of Set 3 | faanui
Processing Record 3 of Set 3 | svetlogorsk
Processing Record 4 of Set 3 | thompson
Processing Record 5 of Set 3 | yellowknife
Processing Record 6 of Set 3 | tazovskiy
Processing Record 7 of Set 3 | saldanha
Processing Record 8 of Set 3 | kinablangan
Processing Record 9 of Set 3 | taoudenni
Processing Record 10 of Set 3 | kibala
Processing Record 11 of Set 3 | medvode
Processing Record 12 of Set 3 | nouadhibou
Processing Record 13 of Set 3 | college
Processing Record 14 of Set 3 | maumere
Processing Record 15 of Set 3 | ayna
Processing Record 16 of Set 3 | tura
Processing Record 17 of Set 3 | rundu
Processing Record 18 of Set 3 | verkhoyansk
Processing Record 19 of Set 3 | littleton
Processing Record 20 of Set 3 | kuytun
Processing Record 21 of Set 3 | villamontes
Processing Record 22 of Set 3 | krapivinskiy
Processing Record 23 of Set 3 | sorong
Processing Record 24 of Set 3 | scottsburgh
City scottsburgh not found. Skipping...
Processing Record 25 of Set 3 | illoqqortoormiut
City illoqqortoormiut not found. Skipping...
Processing Record 26 of Set 3 | amuntai
Processing Record 27 of Set 3 | alcudia
Processing Record 28 of Set 3 | mys shmidta
City mys shmidta not found. Skipping...
Processing Record 29 of Set 3 | lebu
Processing Record 30 of Set 3 | barentsburg
City barentsburg not found. Skipping...
Processing Record 31 of Set 3 | george
Processing Record 32 of Set 3 | cockburn town
Processing Record 33 of Set 3 | sechura
Processing Record 34 of Set 3 | lakes entrance
Processing Record 35 of Set 3 | aden
Processing Record 36 of Set 3 | son la
Processing Record 37 of Set 3 | baixa grande
Processing Record 38 of Set 3 | koungou
Processing Record 39 of Set 3 | pevek
Processing Record 40 of Set 3 | tinaquillo
Processing Record 41 of Set 3 | furano
Processing Record 42 of Set 3 | lembang
Processing Record 43 of Set 3 | eenhana
Processing Record 44 of Set 3 | bereda
Processing Record 45 of Set 3 | marawi
Processing Record 46 of Set 3 | moerai
Processing Record 47 of Set 3 | tasiilaq
Processing Record 48 of Set 3 | dalby
Processing Record 49 of Set 3 | broome
Processing Record 50 of Set 3 | vaitupu
City vaitupu not found. Skipping...
Processing Record 1 of Set 4 | semenivka
Processing Record 2 of Set 4 | vondrozo
Processing Record 3 of Set 4 | hernani
Processing Record 4 of Set 4 | mpika
Processing Record 5 of Set 4 | phan thiet
Processing Record 6 of Set 4 | cabedelo
Processing Record 7 of Set 4 | amapa
Processing Record 8 of Set 4 | saint anthony
Processing Record 9 of Set 4 | belushya guba
City belushya guba not found. Skipping...
Processing Record 10 of Set 4 | kavieng
Processing Record 11 of Set 4 | tomatlan
Processing Record 12 of Set 4 | sitka
Processing Record 13 of Set 4 | yelizovo
Processing Record 14 of Set 4 | upernavik
Processing Record 15 of Set 4 | chuy
Processing Record 16 of Set 4 | vila velha
Processing Record 17 of Set 4 | salalah
Processing Record 18 of Set 4 | palabuhanratu
City palabuhanratu not found. Skipping...
Processing Record 19 of Set 4 | baykalsk
Processing Record 20 of Set 4 | nkan
Processing Record 21 of Set 4 | tsihombe
City tsihombe not found. Skipping...
Processing Record 22 of Set 4 | victoria
Processing Record 23 of Set 4 | bilibino
Processing Record 24 of Set 4 | malazgirt
Processing Record 25 of Set 4 | homer
Processing Record 26 of Set 4 | beringovskiy
Processing Record 27 of Set 4 | general higinio morinigo
Processing Record 28 of Set 4 | hovd
Processing Record 29 of Set 4 | geraldton
Processing Record 30 of Set 4 | aflu
City aflu not found. Skipping...
Processing Record 31 of Set 4 | sakakah
Processing Record 32 of Set 4 | bolungarvik
City bolungarvik not found. Skipping...
Processing Record 33 of Set 4 | kiama
Processing Record 34 of Set 4 | azimur
City azimur not found. Skipping...
Processing Record 35 of Set 4 | parana
Processing Record 36 of Set 4 | san patricio
Processing Record 37 of Set 4 | sumenep
Processing Record 38 of Set 4 | progreso
Processing Record 39 of Set 4 | mount isa
Processing Record 40 of Set 4 | chum phae
Processing Record 41 of Set 4 | baykit
Processing Record 42 of Set 4 | haines junction
Processing Record 43 of Set 4 | port alfred
Processing Record 44 of Set 4 | nizwa
Processing Record 45 of Set 4 | stamsund
City stamsund not found. Skipping...
Processing Record 46 of Set 4 | gambela
Processing Record 47 of Set 4 | aqtobe
Processing Record 48 of Set 4 | nizhniy tsasuchey
Processing Record 49 of Set 4 | san jose
Processing Record 50 of Set 4 | saint-augustin
Processing Record 1 of Set 5 | sweetwater
Processing Record 2 of Set 5 | lake cowichan
Processing Record 3 of Set 5 | carnarvon
Processing Record 4 of Set 5 | micomeseng
Processing Record 5 of Set 5 | hambantota
Processing Record 6 of Set 5 | yueyang
Processing Record 7 of Set 5 | taolanaro
City taolanaro not found. Skipping...
Processing Record 8 of Set 5 | muros
Processing Record 9 of Set 5 | skelleftea
Processing Record 10 of Set 5 | saint-francois
Processing Record 11 of Set 5 | henties bay
Processing Record 12 of Set 5 | vihti
Processing Record 13 of Set 5 | codrington
Processing Record 14 of Set 5 | pundaguitan
Processing Record 15 of Set 5 | atasu
Processing Record 16 of Set 5 | conde
Processing Record 17 of Set 5 | saint-philippe
Processing Record 18 of Set 5 | airai
Processing Record 19 of Set 5 | caravelas
Processing Record 20 of Set 5 | lata
Processing Record 21 of Set 5 | sao filipe
Processing Record 22 of Set 5 | chokurdakh
Processing Record 23 of Set 5 | ribas do rio pardo
Processing Record 24 of Set 5 | ponta do sol
Processing Record 25 of Set 5 | koumac
Processing Record 26 of Set 5 | chernyshevskiy
Processing Record 27 of Set 5 | torbay
Processing Record 28 of Set 5 | eureka
Processing Record 29 of Set 5 | salvador
Processing Record 30 of Set 5 | dalbandin
Processing Record 31 of Set 5 | bulungu
Processing Record 32 of Set 5 | praia
Processing Record 33 of Set 5 | eyl
Processing Record 34 of Set 5 | ketchikan
Processing Record 35 of Set 5 | katsuura
Processing Record 36 of Set 5 | nokaneng
Processing Record 37 of Set 5 | new norfolk
Processing Record 38 of Set 5 | talnakh
Processing Record 39 of Set 5 | namatanai
Processing Record 40 of Set 5 | grindavik
Processing Record 41 of Set 5 | peterhead
Processing Record 42 of Set 5 | sao jose da coroa grande
Processing Record 43 of Set 5 | nanortalik
Processing Record 44 of Set 5 | ilulissat
Processing Record 45 of Set 5 | kruisfontein
Processing Record 46 of Set 5 | half moon bay
Processing Record 47 of Set 5 | margate
Processing Record 48 of Set 5 | auki
Processing Record 49 of Set 5 | luanda
Processing Record 50 of Set 5 | champerico
Processing Record 1 of Set 6 | mullaitivu
City mullaitivu not found. Skipping...
Processing Record 2 of Set 6 | gat
Processing Record 3 of Set 6 | parscoveni
City parscoveni not found. Skipping...
Processing Record 4 of Set 6 | walvis bay
Processing Record 5 of Set 6 | bundaberg
Processing Record 6 of Set 6 | chumikan
Processing Record 7 of Set 6 | komsomolskiy
Processing Record 8 of Set 6 | hithadhoo
Processing Record 9 of Set 6 | lorengau
Processing Record 10 of Set 6 | pavlodar
Processing Record 11 of Set 6 | souillac
Processing Record 12 of Set 6 | samarai
Processing Record 13 of Set 6 | sorvag
City sorvag not found. Skipping...
Processing Record 14 of Set 6 | stolbishche
Processing Record 15 of Set 6 | mayahi
Processing Record 16 of Set 6 | khandyga
Processing Record 17 of Set 6 | dianopolis
City dianopolis not found. Skipping...
Processing Record 18 of Set 6 | ust-omchug
Processing Record 19 of Set 6 | mucuri
Processing Record 20 of Set 6 | marathon
Processing Record 21 of Set 6 | ambilobe
Processing Record 22 of Set 6 | saleaula
City saleaula not found. Skipping...
Processing Record 23 of Set 6 | marcona
City marcona not found. Skipping...
Processing Record 24 of Set 6 | licheng
Processing Record 25 of Set 6 | isla mujeres
Processing Record 26 of Set 6 | nicoya
Processing Record 27 of Set 6 | ust-karsk
Processing Record 28 of Set 6 | griffith
Processing Record 29 of Set 6 | puerto escondido
Processing Record 30 of Set 6 | ciudad guayana
Processing Record 31 of Set 6 | atkinson
Processing Record 32 of Set 6 | ahipara
Processing Record 33 of Set 6 | cairns
Processing Record 34 of Set 6 | portland
Processing Record 35 of Set 6 | manado
Processing Record 36 of Set 6 | porto-vecchio
Processing Record 37 of Set 6 | opuwo
Processing Record 38 of Set 6 | sudak
Processing Record 39 of Set 6 | tezu
Processing Record 40 of Set 6 | saskylakh
Processing Record 41 of Set 6 | dunedin
Processing Record 42 of Set 6 | port macquarie
Processing Record 43 of Set 6 | nautla
Processing Record 44 of Set 6 | atambua
Processing Record 45 of Set 6 | oussouye
Processing Record 46 of Set 6 | kaka
Processing Record 47 of Set 6 | higuey
City higuey not found. Skipping...
Processing Record 48 of Set 6 | warqla
City warqla not found. Skipping...
Processing Record 49 of Set 6 | lincoln
Processing Record 50 of Set 6 | salta
Processing Record 1 of Set 7 | potosi
Processing Record 2 of Set 7 | olyka
Processing Record 3 of Set 7 | konstantinovka
Processing Record 4 of Set 7 | tumannyy
City tumannyy not found. Skipping...
Processing Record 5 of Set 7 | astana
Processing Record 6 of Set 7 | bhag
Processing Record 7 of Set 7 | kayankulam
Processing Record 8 of Set 7 | leningradskiy
Processing Record 9 of Set 7 | plouzane
Processing Record 10 of Set 7 | izumo
Processing Record 11 of Set 7 | matagami
Processing Record 12 of Set 7 | taonan
Processing Record 13 of Set 7 | kenai
Processing Record 14 of Set 7 | samusu
City samusu not found. Skipping...
Processing Record 15 of Set 7 | narsaq
Processing Record 16 of Set 7 | grand river south east
City grand river south east not found. Skipping...
Processing Record 17 of Set 7 | karauzyak
City karauzyak not found. Skipping...
Processing Record 18 of Set 7 | boyolangu
Processing Record 19 of Set 7 | zambezi
Processing Record 20 of Set 7 | taphan hin
Processing Record 21 of Set 7 | dillon
Processing Record 22 of Set 7 | longyearbyen
Processing Record 23 of Set 7 | goderich
Processing Record 24 of Set 7 | dauphin
Processing Record 25 of Set 7 | salinas
Processing Record 26 of Set 7 | turbat
Processing Record 27 of Set 7 | namibe
Processing Record 28 of Set 7 | tiksi
Processing Record 29 of Set 7 | asau
Processing Record 30 of Set 7 | vardo
Processing Record 31 of Set 7 | sambava
Processing Record 32 of Set 7 | tuktoyaktuk
Processing Record 33 of Set 7 | goragorskiy
Processing Record 34 of Set 7 | noumea
Processing Record 35 of Set 7 | callaway
Processing Record 36 of Set 7 | chute-aux-outardes
Processing Record 37 of Set 7 | jackson
Processing Record 38 of Set 7 | centerville
Processing Record 39 of Set 7 | le mars
Processing Record 40 of Set 7 | cidreira
Processing Record 41 of Set 7 | norman wells
Processing Record 42 of Set 7 | nelson bay
Processing Record 43 of Set 7 | teya
Processing Record 44 of Set 7 | ambulu
Processing Record 45 of Set 7 | masterton
Processing Record 46 of Set 7 | tuatapere
Processing Record 47 of Set 7 | anadyr
Processing Record 48 of Set 7 | vostok
Processing Record 49 of Set 7 | ambon
Processing Record 50 of Set 7 | chiredzi
Processing Record 1 of Set 8 | montbrison
Processing Record 2 of Set 8 | atar
Processing Record 3 of Set 8 | lusambo
Processing Record 4 of Set 8 | morsbach
Processing Record 5 of Set 8 | bethel
Processing Record 6 of Set 8 | naze
Processing Record 7 of Set 8 | ballina
Processing Record 8 of Set 8 | olenegorsk
Processing Record 9 of Set 8 | hasaki
Processing Record 10 of Set 8 | port lincoln
Processing Record 11 of Set 8 | esperance
Processing Record 12 of Set 8 | dangara
Processing Record 13 of Set 8 | pedregal
Processing Record 14 of Set 8 | dryden
Processing Record 15 of Set 8 | yulara
Processing Record 16 of Set 8 | alofi
Processing Record 17 of Set 8 | clyde river
Processing Record 18 of Set 8 | shirakawa
Processing Record 19 of Set 8 | jian
Processing Record 20 of Set 8 | nizhnyaya tura
Processing Record 21 of Set 8 | lerwick
Processing Record 22 of Set 8 | innisfail
Processing Record 23 of Set 8 | san quintin
Processing Record 24 of Set 8 | toliary
City toliary not found. Skipping...
Processing Record 25 of Set 8 | poum
Processing Record 26 of Set 8 | grimari
City grimari not found. Skipping...
Processing Record 27 of Set 8 | praya
Processing Record 28 of Set 8 | kurtalan
Processing Record 29 of Set 8 | saint-louis
Processing Record 30 of Set 8 | nemuro
Processing Record 31 of Set 8 | shache
Processing Record 32 of Set 8 | acapulco
Processing Record 33 of Set 8 | deputatskiy
Processing Record 34 of Set 8 | monrovia
Processing Record 35 of Set 8 | sentyabrskiy
City sentyabrskiy not found. Skipping...
Processing Record 36 of Set 8 | mana
Processing Record 37 of Set 8 | omboue
Processing Record 38 of Set 8 | kudahuvadhoo
Processing Record 39 of Set 8 | udarnyy
Processing Record 40 of Set 8 | biak
Processing Record 41 of Set 8 | bathsheba
Processing Record 42 of Set 8 | wanning
Processing Record 43 of Set 8 | belyy yar
Processing Record 44 of Set 8 | lompoc
Processing Record 45 of Set 8 | katobu
Processing Record 46 of Set 8 | fuzhou
Processing Record 47 of Set 8 | rio grande
Processing Record 48 of Set 8 | sorochinsk
Processing Record 49 of Set 8 | balykshi
Processing Record 50 of Set 8 | louisbourg
City louisbourg not found. Skipping...
Processing Record 1 of Set 9 | marzuq
Processing Record 2 of Set 9 | ropcha
Processing Record 3 of Set 9 | sorland
Processing Record 4 of Set 9 | khonuu
City khonuu not found. Skipping...
Processing Record 5 of Set 9 | sistranda
Processing Record 6 of Set 9 | qasigiannguit
Processing Record 7 of Set 9 | grande-riviere
City grande-riviere not found. Skipping...
Processing Record 8 of Set 9 | maunabo
Processing Record 9 of Set 9 | sinnamary
Processing Record 10 of Set 9 | mogadishu
Processing Record 11 of Set 9 | vagay
Processing Record 12 of Set 9 | rumonge
Processing Record 13 of Set 9 | zedelgem
Processing Record 14 of Set 9 | mathathane
Processing Record 15 of Set 9 | rosetta
Processing Record 16 of Set 9 | maragheh
Processing Record 17 of Set 9 | kamenskoye
City kamenskoye not found. Skipping...
Processing Record 18 of Set 9 | vostochnyy
Processing Record 19 of Set 9 | megion
Processing Record 20 of Set 9 | scarborough
Processing Record 21 of Set 9 | riyadh
Processing Record 22 of Set 9 | tooele
Processing Record 23 of Set 9 | worland
Processing Record 24 of Set 9 | pangnirtung
Processing Record 25 of Set 9 | norwich
Processing Record 26 of Set 9 | sola
Processing Record 27 of Set 9 | dongsheng
Processing Record 28 of Set 9 | kisangani
Processing Record 29 of Set 9 | colombo
Processing Record 30 of Set 9 | darhan
Processing Record 31 of Set 9 | ponta delgada
Processing Record 32 of Set 9 | mbanza-ngungu
Processing Record 33 of Set 9 | ous
Processing Record 34 of Set 9 | bar harbor
Processing Record 35 of Set 9 | baghmara
Processing Record 36 of Set 9 | yangjiang
Processing Record 37 of Set 9 | akureyri
Processing Record 38 of Set 9 | havoysund
Processing Record 39 of Set 9 | mehamn
Processing Record 40 of Set 9 | krasnopavlivka
Processing Record 41 of Set 9 | myitkyina
Processing Record 42 of Set 9 | bawku
Processing Record 43 of Set 9 | christchurch
Processing Record 44 of Set 9 | chapleau
Processing Record 45 of Set 9 | port-gentil
Processing Record 46 of Set 9 | antalaha
Processing Record 47 of Set 9 | taungdwingyi
Processing Record 48 of Set 9 | klaksvik
Processing Record 49 of Set 9 | san carlos de bariloche
Processing Record 50 of Set 9 | dothan
Processing Record 1 of Set 10 | paamiut
Processing Record 2 of Set 10 | tema
Processing Record 3 of Set 10 | isangel
Processing Record 4 of Set 10 | saint george
Processing Record 5 of Set 10 | chadan
Processing Record 6 of Set 10 | nizhneangarsk
Processing Record 7 of Set 10 | molchanovo
Processing Record 8 of Set 10 | chapais
Processing Record 9 of Set 10 | thisted
Processing Record 10 of Set 10 | rock sound
Processing Record 11 of Set 10 | hammerfest
Processing Record 12 of Set 10 | dzhusaly
City dzhusaly not found. Skipping...
Processing Record 13 of Set 10 | neuquen
Processing Record 14 of Set 10 | zolotinka
City zolotinka not found. Skipping...
Processing Record 15 of Set 10 | clonakilty
Processing Record 16 of Set 10 | saint-georges
Processing Record 17 of Set 10 | kodiak
Processing Record 18 of Set 10 | ewo
Processing Record 19 of Set 10 | pontarlier
Processing Record 20 of Set 10 | derbent
Processing Record 21 of Set 10 | kodinsk
Processing Record 22 of Set 10 | petropavlovsk-kamchatskiy
Processing Record 23 of Set 10 | bima
Processing Record 24 of Set 10 | bud
Processing Record 25 of Set 10 | hami
Processing Record 26 of Set 10 | tremedal
Processing Record 27 of Set 10 | gumdag
Processing Record 28 of Set 10 | marondera
Processing Record 29 of Set 10 | gualaco
Processing Record 30 of Set 10 | balgazyn
Processing Record 31 of Set 10 | labytnangi
Processing Record 32 of Set 10 | vestmanna
Processing Record 33 of Set 10 | omsukchan
Processing Record 34 of Set 10 | talcahuano
Processing Record 35 of Set 10 | jiuquan
Processing Record 36 of Set 10 | monte cristi
City monte cristi not found. Skipping...
Processing Record 37 of Set 10 | cochrane
Processing Record 38 of Set 10 | manchester
Processing Record 39 of Set 10 | simao
Processing Record 40 of Set 10 | wasilla
Processing Record 41 of Set 10 | pemangkat
Processing Record 42 of Set 10 | pontianak
Processing Record 43 of Set 10 | sao gabriel da cachoeira
Processing Record 44 of Set 10 | leh
Processing Record 45 of Set 10 | prince rupert
Processing Record 46 of Set 10 | kontagora
Processing Record 47 of Set 10 | padang
Processing Record 48 of Set 10 | raudeberg
Processing Record 49 of Set 10 | rafai
Processing Record 50 of Set 10 | tommot
Processing Record 1 of Set 11 | jumla
Processing Record 2 of Set 11 | shenjiamen
Processing Record 3 of Set 11 | mildura
Processing Record 4 of Set 11 | cheyur
City cheyur not found. Skipping...
Processing Record 5 of Set 11 | gimli
Processing Record 6 of Set 11 | berlevag
Processing Record 7 of Set 11 | palmer
Processing Record 8 of Set 11 | yerbogachen
Processing Record 9 of Set 11 | tombouctou
Processing Record 10 of Set 11 | vermillion
Processing Record 11 of Set 11 | pedernales
Processing Record 12 of Set 11 | chifeng
Processing Record 13 of Set 11 | ixtapa
Processing Record 14 of Set 11 | dhidhdhoo
Processing Record 15 of Set 11 | tabiauea
City tabiauea not found. Skipping...
Processing Record 16 of Set 11 | gazli
Processing Record 17 of Set 11 | messina
Processing Record 18 of Set 11 | southbridge
Processing Record 19 of Set 11 | carutapera
Processing Record 20 of Set 11 | alice springs
Processing Record 21 of Set 11 | port blair
Processing Record 22 of Set 11 | villazon
Processing Record 23 of Set 11 | sal rei
Processing Record 24 of Set 11 | maceio
Processing Record 25 of Set 11 | vestmannaeyjar
Processing Record 26 of Set 11 | daru
Processing Record 27 of Set 11 | shitanjing
Processing Record 28 of Set 11 | karla
Processing Record 29 of Set 11 | aranos
Processing Record 30 of Set 11 | coihaique
Processing Record 31 of Set 11 | dongobesh
Processing Record 32 of Set 11 | tabulbah
City tabulbah not found. Skipping...
Processing Record 33 of Set 11 | erenhot
Processing Record 34 of Set 11 | moranbah
Processing Record 35 of Set 11 | verkhnebakanskiy
Processing Record 36 of Set 11 | jalu
Processing Record 37 of Set 11 | les cayes
Processing Record 38 of Set 11 | corinto
Processing Record 39 of Set 11 | dwarka
Processing Record 40 of Set 11 | pueblo
Processing Record 41 of Set 11 | tamazunchale
Processing Record 42 of Set 11 | snezhnogorsk
Processing Record 43 of Set 11 | grande prairie
Processing Record 44 of Set 11 | korla
Processing Record 45 of Set 11 | inderborskiy
City inderborskiy not found. Skipping...
Processing Record 46 of Set 11 | markova
Processing Record 47 of Set 11 | smithers
Processing Record 48 of Set 11 | kochki
Processing Record 49 of Set 11 | ocean city
Processing Record 50 of Set 11 | thinadhoo
Processing Record 1 of Set 12 | nouakchott
Processing Record 2 of Set 12 | joensuu
Processing Record 3 of Set 12 | santa helena
Processing Record 4 of Set 12 | ushibuka
Processing Record 5 of Set 12 | linda
Processing Record 6 of Set 12 | apango
Processing Record 7 of Set 12 | kralendijk
Processing Record 8 of Set 12 | yuza
Processing Record 9 of Set 12 | kadykchan
City kadykchan not found. Skipping...
Processing Record 10 of Set 12 | thunder bay
Processing Record 11 of Set 12 | kwinana
Processing Record 12 of Set 12 | yeppoon
Processing Record 13 of Set 12 | sciacca
Processing Record 14 of Set 12 | casma
Processing Record 15 of Set 12 | santa isabel
Processing Record 16 of Set 12 | pa sang
Processing Record 17 of Set 12 | benghazi
Processing Record 18 of Set 12 | turukhansk
Processing Record 19 of Set 12 | dali
Processing Record 20 of Set 12 | zhigansk
Processing Record 21 of Set 12 | borba
Processing Record 22 of Set 12 | upata
Processing Record 23 of Set 12 | tashla
Processing Record 24 of Set 12 | petropavlovskoye
Processing Record 25 of Set 12 | itacoatiara
Processing Record 26 of Set 12 | indian head
Processing Record 27 of Set 12 | north platte
Processing Record 28 of Set 12 | baker city
Processing Record 29 of Set 12 | yatou
Processing Record 30 of Set 12 | peniche
Processing Record 31 of Set 12 | rajula
Processing Record 32 of Set 12 | xapuri
Processing Record 33 of Set 12 | catuday
Processing Record 34 of Set 12 | senno
Processing Record 35 of Set 12 | mayumba
Processing Record 36 of Set 12 | rexburg
Processing Record 37 of Set 12 | meulaboh
Processing Record 38 of Set 12 | mahadday weyne
City mahadday weyne not found. Skipping...
Processing Record 39 of Set 12 | bababe
City bababe not found. Skipping...
Processing Record 40 of Set 12 | najran
Processing Record 41 of Set 12 | ginda
Processing Record 42 of Set 12 | barillas
Processing Record 43 of Set 12 | barawe
City barawe not found. Skipping...
-----------------------------
Data Retrieval Complete      
-----------------------------
# Convert the array of dictionaries to a Pandas DataFrame.
city_data_df = pd.DataFrame(city_data)
city_data_df.head(10)
City	Lat	Lng	Max Temp	Humidity	Cloudiness	Wind Speed	Country	Date
0	Jamestown	42.0970	-79.2353	45.01	25	100	17.27	US	2022-03-23 13:38:42
1	Cherskiy	68.7500	161.3000	1.31	100	63	1.07	RU	2022-03-23 13:38:42
2	Kaitangata	-46.2817	169.8464	57.09	96	5	3.53	NZ	2022-03-23 13:38:43
3	Pankrushikha	53.8319	80.3406	23.65	94	100	18.21	RU	2022-03-23 13:38:43
4	Fortuna	40.5982	-124.1573	49.93	96	100	0.00	US	2022-03-23 13:38:43
5	Nome	64.5011	-165.4064	12.27	44	0	4.61	US	2022-03-23 13:38:44
6	Avanigadda	16.0215	80.9181	83.05	74	88	5.59	IN	2022-03-23 13:38:44
7	Kapaa	22.0752	-159.3190	72.19	86	75	17.27	US	2022-03-23 13:38:44
8	Punta Arenas	-53.1500	-70.9167	42.91	52	0	11.50	CL	2022-03-23 13:38:44
9	Castro	-24.7911	-50.0119	73.35	62	100	9.06	BR	2022-03-23 13:38:45
new_column_order = ["City","Country","Date","Lat","Lng","Max Temp","Humidity","Cloudiness","Wind Speed"]
city_data_df =city_data_df[new_column_order]
city_data_df
City	Country	Date	Lat	Lng	Max Temp	Humidity	Cloudiness	Wind Speed
0	Provideniya	RU	2022-03-19 19:44:17	64.3833	-173.3000	2.28	71	1	2.98
1	Hithadhoo	MV	2022-03-19 19:51:40	-0.6000	73.0833	83.52	71	8	17.00
2	Kruisfontein	ZA	2022-03-19 19:51:40	-34.0033	24.7314	68.88	95	0	4.45
3	Energetik	RU	2022-03-19 19:51:41	51.7445	58.7934	4.77	99	83	5.48
4	Constitucion	CL	2022-03-19 19:51:41	-35.3333	-72.4167	67.48	48	100	14.47
...	...	...	...	...	...	...	...	...	...
522	Odweyne	SO	2022-03-19 20:05:30	9.4092	45.0640	74.52	41	6	4.45
523	Kuching	MY	2022-03-19 20:00:33	1.5500	110.3333	75.42	94	40	0.00
524	San Roque	ES	2022-03-19 20:05:30	36.2107	-5.3842	57.38	84	46	20.11
525	Sao Paulo De Olivenca	BR	2022-03-19 20:05:31	-3.3783	-68.8725	76.68	93	97	4.21
526	Qaqortoq	GL	2022-03-19 20:05:31	60.7167	-46.0333	13.68	90	59	3.44
527 rows ?? 9 columns

# Create the output file (CSV).
output_data_file = "weather_data/cities.csv"
# Export the City_Data into a CSV.
city_data_df.to_csv(output_data_file, index_label="City_ID")
# Extract relevant fields from the DataFrame for plotting.
lats = city_data_df["Lat"]
max_temps = city_data_df["Max Temp"]
humidity = city_data_df["Humidity"]
cloudiness = city_data_df["Cloudiness"]
wind_speed = city_data_df["Wind Speed"]
# Build the scatter plot for latitude vs. max temperature.
plt.scatter(lats,
            max_temps,
            edgecolor="black", linewidths=1, marker="o",
            alpha=0.8, label="Cities")
# Incorporate the other graph properties.
plt.title(f"City Latitude vs. Max Temperature "+ time.strftime("%x"))
plt.ylabel("Max Temperature (F)")
plt.xlabel("Latitude")
plt.grid(True)
# Save the figure.
plt.savefig("weather_data/Fig1.png")

# Show plot.
plt.show()

# Build the scatter plots for latitude vs. humidity.
plt.scatter(lats,
            humidity,
            edgecolor="black", linewidths=1, marker="o",
            alpha=0.8, label="Cities")

# Incorporate the other graph properties.
plt.title(f"City Latitude vs. Humidity "+ time.strftime("%x"))
plt.ylabel("Humidity (%)")
plt.xlabel("Latitude")
plt.grid(True)
# Save the figure.
plt.savefig("weather_data/Fig2.png")
# Show plot.
plt.show()

# Build the scatter plots for latitude vs. cloudiness.
plt.scatter(lats,
            cloudiness,
            edgecolor="black", linewidths=1, marker="o",
            alpha=0.8, label="Cities")

# Incorporate the other graph properties.
plt.title(f"City Latitude vs. Cloudiness (%) "+ time.strftime("%x"))
plt.ylabel("Cloudiness (%)")
plt.xlabel("Latitude")
plt.grid(True)
# Save the figure.
plt.savefig("weather_data/Fig3.png")
# Show plot.
plt.show()

# Build the scatter plots for latitude vs. wind speed.
plt.scatter(lats,
            wind_speed,
            edgecolor="black", linewidths=1, marker="o",
            alpha=0.8, label="Cities")

# Incorporate the other graph properties.
plt.title(f"City Latitude vs. Wind Speed "+ time.strftime("%x"))
plt.ylabel("Wind Speed (mph)")
plt.xlabel("Latitude")
plt.grid(True)
# Save the figure.
plt.savefig("weather_data/Fig4.png")
# Show plot.
plt.show()

# Import linregress
from scipy.stats import linregress

# Create a function to create perform linear regression on the weather data
# and plot a regression line and the equation with the data.
def plot_linear_regression(x_values, y_values, title, y_label, text_coordinates):

    # Run regression on hemisphere weather data.
    (slope, intercept, r_value, p_value, std_err) = linregress(x_values, y_values)

    # Calculate the regression line "y values" from the slope and intercept.
    regress_values = x_values * slope + intercept
    # Get the equation of the line.
    line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))
    # Create a scatter plot and plot the regression line.
    plt.scatter(x_values,y_values)
    plt.plot(x_values,regress_values,"r")
    # Annotate the text for the line equation.
    plt.annotate(line_eq, text_coordinates, fontsize=15, color="red")
    plt.title(title)
    plt.xlabel('Latitude')
    plt.ylabel(y_label)
    plt.show()
    return r_value
index13 = city_data_df.loc[13]
index13 
City               Severo-Kurilsk
Country                        RU
Date          2022-03-23 13:38:46
Lat                       50.6789
Lng                       156.125
Max Temp                    27.72
Humidity                       69
Cloudiness                     26
Wind Speed                  12.75
Name: 13, dtype: object
city_data_df["Lat"] >= 0
0       True
1       True
2      False
3       True
4       True
       ...  
537     True
538     True
539     True
540     True
541     True
Name: Lat, Length: 542, dtype: bool
city_data_df.loc[(city_data_df["Lat"] >= 0)]
City	Country	Date	Lat	Lng	Max Temp	Humidity	Cloudiness	Wind Speed
0	Jamestown	US	2022-03-23 13:38:42	42.0970	-79.2353	45.01	25	100	17.27
1	Cherskiy	RU	2022-03-23 13:38:42	68.7500	161.3000	1.31	100	63	1.07
3	Pankrushikha	RU	2022-03-23 13:38:43	53.8319	80.3406	23.65	94	100	18.21
4	Fortuna	US	2022-03-23 13:38:43	40.5982	-124.1573	49.93	96	100	0.00
5	Nome	US	2022-03-23 13:38:44	64.5011	-165.4064	12.27	44	0	4.61
...	...	...	...	...	...	...	...	...	...
537	Rexburg	US	2022-03-23 13:49:55	43.8260	-111.7897	29.71	74	0	3.44
538	Meulaboh	ID	2022-03-23 13:52:41	4.1363	96.1285	79.77	83	62	4.61
539	Najran	SA	2022-03-23 13:48:21	17.4924	44.1277	93.85	16	46	19.91
540	Ginda	IN	2022-03-23 13:52:42	30.6945	78.4932	58.82	26	4	5.03
541	Barillas	GT	2022-03-23 13:52:42	15.8036	-91.3158	70.84	56	0	2.48
379 rows ?? 9 columns

city_data_df.loc[(city_data_df["Lat"] >= 0)].head()
City	Country	Date	Lat	Lng	Max Temp	Humidity	Cloudiness	Wind Speed
0	Jamestown	US	2022-03-23 13:38:42	42.0970	-79.2353	45.01	25	100	17.27
1	Cherskiy	RU	2022-03-23 13:38:42	68.7500	161.3000	1.31	100	63	1.07
3	Pankrushikha	RU	2022-03-23 13:38:43	53.8319	80.3406	23.65	94	100	18.21
4	Fortuna	US	2022-03-23 13:38:43	40.5982	-124.1573	49.93	96	100	0.00
5	Nome	US	2022-03-23 13:38:44	64.5011	-165.4064	12.27	44	0	4.61
# Create Northern and Southern Hemisphere DataFrames.
northern_hemi_df = city_data_df.loc[(city_data_df["Lat"] >= 0)]
southern_hemi_df = city_data_df.loc[(city_data_df["Lat"] < 0)]
northern_hemi_df.head()
City	Country	Date	Lat	Lng	Max Temp	Humidity	Cloudiness	Wind Speed
0	Jamestown	US	2022-03-23 13:38:42	42.0970	-79.2353	45.01	25	100	17.27
1	Cherskiy	RU	2022-03-23 13:38:42	68.7500	161.3000	1.31	100	63	1.07
3	Pankrushikha	RU	2022-03-23 13:38:43	53.8319	80.3406	23.65	94	100	18.21
4	Fortuna	US	2022-03-23 13:38:43	40.5982	-124.1573	49.93	96	100	0.00
5	Nome	US	2022-03-23 13:38:44	64.5011	-165.4064	12.27	44	0	4.61
# Linear regression on the Northern Hemisphere
x_values = northern_hemi_df["Lat"]
y_values = northern_hemi_df["Max Temp"]
# Call the function.
r_value = plot_linear_regression(x_values, y_values,
                       'Linear Regression on the Northern Hemisphere \
                        for Maximum Temperature', 'Max Temp',(10,40))
print(f"r_value is {r_value}")

r_value is -0.8640767468506919
# Linear regression on the Northern Hemisphere
x_values = southern_hemi_df["Lat"]
y_values = southern_hemi_df["Max Temp"]
# Call the function.
r_value = plot_linear_regression(x_values, y_values,
                       'Linear Regression on the Southern Hemisphere \
                        for Maximum Temperature', 'Max Temp',(-50,90))
print(f"r_value is {r_value}")

r_value is 0.6762953421444049
# Linear regression on the Northern Hemisphere
x_values = northern_hemi_df["Lat"]
y_values = northern_hemi_df["Humidity"]
# Call the function.
r_value = plot_linear_regression(x_values, y_values,
                       'Linear Regression on the Northern Hemisphere \
                        for % Humidity', '% Humidity',(40,10))
print(f"r_value is {r_value}")

r_value is 0.34046369235861146
# Linear regression on the Southern Hemisphere
x_values = southern_hemi_df["Lat"]
y_values = southern_hemi_df["Humidity"]
# Call the function.
r_value = plot_linear_regression(x_values, y_values,
                       'Linear Regression on the Southern Hemisphere \
                        for % Humidity', '% Humidity',(-50,25))
print(f"r_value is {r_value}")

r_value is 0.043082229179424385
# Linear regression on the Northern Hemisphere for Cloudiness
x_values = northern_hemi_df["Lat"]
y_values = northern_hemi_df["Cloudiness"]
# Call the function.
r_value = plot_linear_regression(x_values, y_values,
                       'Linear Regression on the Northern Hemisphere \
                        for % Cloudiness', '% Cloudiness',(10,40))
print(f"r_value is {r_value}")

r_value is 0.23221600927610156
# Linear regression on the Southern Hemisphere
x_values = southern_hemi_df["Lat"]
y_values = southern_hemi_df["Cloudiness"]
# Call the function.
r_value = plot_linear_regression(x_values, y_values,
                       'Linear Regression on the Southern Hemisphere \
                        for % Cloudiness', '% Cloudiness',(-50,60))
print(f"r_value is {r_value}")

r_value is 0.20241518901229974
# Linear regression on the Northern Hemisphere
x_values = northern_hemi_df["Lat"]
y_values = northern_hemi_df["Wind Speed"]
# Call the function.
r_value = plot_linear_regression(x_values, y_values,
                       'Linear Regression on the Northern Hemisphere \
                        for Wind Speed', 'Wind Speed',(30,25))
print(f"r_value is {r_value}")

r_value is -0.03185305617896415
# Linear regression on the Southern Hemisphere
x_values = southern_hemi_df["Lat"]
y_values = southern_hemi_df["Wind Speed"]
# Call the function.
r_value = plot_linear_regression(x_values, y_values,
                       'Linear Regression on the Southern Hemisphere \
                        for Wind Speed', 'Wind Speed',(-50,20))
print(f"r_value is {r_value}")

r_value is -0.24872506676163253