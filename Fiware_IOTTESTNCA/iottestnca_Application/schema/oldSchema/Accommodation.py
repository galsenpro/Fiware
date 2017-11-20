"""
	On propose un nouveau datamodel ("Hotels and Motels" ou "Accommodation" qui sera référencé dans POI)
"""
{
	"id" : "Accomadation-NCA-2017", #ID hebergement
	"type" : "Hotels and Motels OR Accommadation",
	"name" : "Name of the Accommadation",
	"address" : {
		"zip": "06100",
		"city": "NICE"
	},
	"phone": "+33(0)6 63 52 19 70",
	"fax": null,
	"email": "gregoops@hotmail.com",
	"website": null,
	"contacts": null,
	"payments": [ "Espèces","Virements"], #Mode de paiement
	"languages":  ["English", "French", "Espanish"], #Langues parlées à l'accueil
	"amenities": ["Ascenseur", "Wifi gratuit", "Double vitrage", ],#Equipements
 	"locations": [ "Bord de mer", "Gambetta", "Centre Ville"], #Diffent de location (lat,lg)
    "categories": ["Hotels de tourisme","Hotels pour conférence", "Offre  Séminaires"],
    "stations": ["Grosso CUM - Promenade","Grosso CUM", "Grosso CUM"],
    "standings_levels": {
                "standings_level": "4 étoiles"
            },
    "chains": {
             "chain": "Marriott International"
           },
    "options": {
                "option": "Privatisable"
            },
    "publications": null,
    "common_tags": null,
    "group_options": null,
    "family_options": {
        "family_option": "matériel adapté aux enfants"
        },
    "disabled_options": {
            "disabled_option": "Accessible personnes handicapées"
        },
    "sectors": null,
    "living": {
            "room_count": "143",
          	"room_bath_count": "0",
            "room_shower_count": "143",
            "suite_count": "22",
        },
    "tariffs": null,
    "capacity": {
     		"indoor": "0",
            "outdoor": "0",
            "room_count": "4",
            "seated": "100",
            "cocktail": "150"
        },
    "closures": null,
    "spaces": null,
    "opening": null,
    "closing": null
}