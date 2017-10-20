#POI qui fait référence à un SHOP
#
#
{
    "id": "PointOfInterest-SHOP_1328", #BOUTIQUE_ID
    "type": "PointOfInterest",
    "name": "A L'OLIVIER", #name_fr
    "description": "Descriptions de la boutique", #descriptions
    "address": {
      "addressCountry": "ES", #Split sur le télephone ou name
      "addressLocality": "7 Rue Saint-Fraçois de Paule" #adress_line1 + adress_line2 + adress_line3
      #Add 'zip' = '06300',
      #dd 'city' = 'NICE'
    },
    "category": ["169"], #Boutique - Centre commercial
    "location": {
      "type": "Point",
      "coordinates": [
        -8.768460000000001, #latitude
        42.60214472222222 #longitude
      ]
    },
    "source": "http://www.tourspain.es", #
    "refSeeAlso": ["Beach-A-Concha-123456"],
    #Attributs supplémentaires (SI NON NULL)
    "phone": "+33(0)4 93 13 44 97",
    "fax": null,
    "email": "nice@alolivier.com",
    "website": null,
    "contacts": null,
    #Fin attributs supplémentaires
}