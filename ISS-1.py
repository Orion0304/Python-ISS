# Créé par Ulysse, le 21/02/2021 en Python 3.7
import json
import time
import urllib.request
import cartopy.crs as ccrs
import matplotlib.pyplot as plt


url='http://api.open-notify.org/astros.json'
reponse=urllib.request.urlopen(url)
resultat=json.loads(reponse.read())

print("Personnes dans l'espace: ", resultat['number'])

Personne = resultat['people']
Vaisseau = resultat['message']

for p in Personne:
  print(p["name"], ("dans "), p["craft"])

url = 'http://api.open-notify.org/iss-now.json'
reponse = urllib.request.urlopen(url)
resultat = json.loads(reponse.read())

emplacement = resultat['iss_position']
lat = float(emplacement['latitude'])
lon = float(emplacement['longitude'])
print('Latitude:', lat)
print('Longitude:', lon)

#Centre spatial de Houston
latH = 29.5502
lonH = -95.097

#Coordonnées de Rennes
latR=48.11198000
lonR=-1.67429000

ax = plt.axes(projection=ccrs.PlateCarree())
ax.stock_img()

plt.plot([lonH,lonR], [latH,latR],
         color='blue', ls='None', marker='o',
         transform=ccrs.Geodetic(),
         )
plt.plot(lon,lat, color='red', ls='None', marker='o',
         transform=ccrs.Geodetic(),
         )
plt.text(lonH + 1, latH +2, 'Houston',
         horizontalalignment='right',
         transform=ccrs.Geodetic())

plt.text(lonR + 1, latR +2, 'Rennes',
         horizontalalignment='right',
         transform=ccrs.Geodetic())

plt.text(lon + 1, lat +2, 'ISS',
         horizontalalignment='left',
         transform=ccrs.Geodetic())


#Ce qui suit récupérait la prochaine date à laquelle l'ISS passe au-dessus d'un point donné, mais l'API n'existe plus aujourd'hui.
'''url = 'http://api.open-notify.org/iss-pass.json'
url = url + '?lat=' + str(lat) + '&lon=' + str(lon)
print(url)
response = urllib.request.urlopen(url)
resultat = json.loads(response.read())

audessus = resultat['response'][1]['risetime']
print(audessus)


#Chez nous
latC = 47.801233
lonC = -2.325638

plt.plot(lonC, latC,
         color='blue', ls='None', marker='o',
         transform=ccrs.Geodetic(),
         )

plt.text(lonC + 1, latC +2, 'Houston',
         horizontalalignment='right',
         transform=ccrs.Geodetic())


url = 'http://api.open-notify.org/iss-pass.json'
url = url + '?lat=' + str(lat) + '&lon=' + str(lon)
response = urllib.request.urlopen(url)
resultat = json.loads(response.read())

audessus = resultat['response'][1]['risetime']
print(audessus)'''

plt.show()
