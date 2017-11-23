{
	"datamodels" : {
		"entities" : [
			{
			"context" : "TRANSPORTS",
			"datamodel" : [{
				        "id": "Spain-Road-A62",
				        "type": "Road",
				        "name": "A-62",
				        "alternateName": "E-80",
				        "description": "Autovía de Castilla",
				        "roadClass": "motorway",
				        "length": 355,
				        "refRoadSegment": ["Spain-RoadSegment-A62-0-355-forwards", "Spain-RoadSegment-A62-0-355-backwards"],
				        "responsible": "Ministerio de Fomento - Gobierno de España"
				    },{
					    "id": "Spain-RoadSegment-A62-osm-24702186",
					    "type": "RoadSegment",
					    "name": "Valladolid-Dueñas",
					    "category": ["oneway"],
					    "refRoad": "Spain-Road-A62",
					    "totalLaneNumber": 2,
					    "maximumAllowedSpeed": 120,
					    "minimumAllowedSpeed": 60,
					    "startPoint": {
						      "type": "Point",
						      "coordinates": [-4.7299180606009, 41.6844918725019]
					    },
					    "endPoint": {
					      		"type": "Point",
					      		"coordinates": [-4.55167335377909, 41.8570461783071]
					    },
					    "allowedVehicleType": [
					        	"car", "bus", "lorry", "trailer",
					        	"tanker", "van", "caravan"
					    ],
					    "location": {
					       "type": "LineString",
					       "coordinates": [
					            [
					               -4.7299180606009, 41.6844918725019
					            ],
					            [
					              -4.72855890957602, 41.6860596957855
					            ],
					            [
					              -4.5520357341647, 41.8569278186523
					            ],
					            [
					               -4.55167335377909, 41.8570461783071
					            ]
					       ]
					    },
					    "laneUsage": ["forward", "forward"],
					    "source": "http://wwww.openstreetmap.org"
					},{
						"id": "vehicle:WasteManagement:1",
						"type": "Vehicle",
						"vehicleType": "lorry",
						"category": ["municipalServices"],
						"location": {
						    	"type": "Point",
						    	"coordinates": [ -3.164485591715449, 40.62785133667262 ]
						  	},
						"name": "C Recogida 1",
						"speed": 50,
						"cargoWeight": 314,
						"serviceStatus": "onRoute, garbageCollection",
						"serviceProvided": ["gargabeCollection", "wasteContainerCleaning"],
						"areaServed": "Centro",
						"refVehicleModel": "vehiclemodel:econic",
						"vehiclePlateIdentifier": "3456ABC"
					},{
					   "id": "malaga-bici-7",
					   "type": "BikeHireDockingStation",
					   "name": "07-Diputacion",
					   "location": {
					     "coordinates": [-4.43573, 36.699694],
					      "type": "Point"
					   },
					   "availableBikeNumber": 18,
					   "freeSlotNumber": 10,
					   "address": {
					      "streetAddress": "Paseo Antonio Banderas (Diputación)",
					      "addressLocality": "Malaga",
					      "addressCountry": "España"
					   },
					   "description": "Punto de alquiler de bicicletas próximo a Diputación",
					   "dateModified": "2017-05-09T09:25:55.00Z"
					},{
				       "id": "TrafficFlowObserved-Valladolid-osm-60821110",
				       "type": "TrafficFlowObserved",
				       "laneId": 1,
				       "address": {
				         "streetAddress": "Avenida de Salamanca",
				         "addressLocality": "Valladolid",
				         "addressCountry": "ES"
				       },
				       "location": {
				         "type": "LineString",
				         "coordinates": [
				           [
				             -4.73735395519672, 41.6538181849672
				           ],
				           [
				             -4.73414858659993, 41.6600594193478
				           ],
				           [
				             -4.73447575302641, 41.659585195093
				           ]
				         ]
				       },
				       "dateObserved": "2016-12-07T11:10:00/2016-12-07T11:15:00",
				       "dateObservedFrom": "2016-12-07T11:10:00",
				       "dateObservedTo": "2016-12-07T11:15:00",
				       "averageHeadwayTime": 0.5,
				       "intensity": 197,
				       "capacity": 0.76,
				       "averageVehicleSpeed": 52.6,
				       "averageVehicleLength": 9.87,
				       "reversedLane": False,
				       "laneDirection": "forward"
				    },{
					  "id": "porto-ParkingLot-23889",
					  "type": "OffStreetParking",
					  "name": "Parque de estacionamento Trindade",
					  "category": ["underground", "public", "feeCharged", "mediumTerm", "barrierAccess"],
					  "chargeType": ["temporaryPrice"],
					  "requiredPermit": [],
					  "layout": ["multiLevel"],
					  "maximumParkingDuration": "PT8H",
					  "location": {
					    "coordinates": [-8.60961198807, 41.150691773],
					    "type": "Point"
					  },
					  "allowedVehicleType": ["car"],
					  "totalSpotNumber": 414,
					  "availableSpotNumber": 132,
					  "address": {
					    "streetAddress": "Rua de Fernandes Tomás",
					    "addressLocality": "Porto",
					    "addressCountry": "Portugal"
					  },
					  "description": "Municipal car park located near the Trindade metro station and the Town Hall",
					  "dateModified": "2016-06-02T09:25:55.00Z"
					},{
					  "id": "santander:daoiz_velarde_1_5",
					  "type": "OnStreetParking",
					  "category": ["blueZone", "shortTerm", "forDisabled"],
					  "allowedVehicleType": "car",
					  "chargeType": ["temporaryFee"],
					  "requiredPermit": ["blueZonePermit", "disabledPermit"],
					  "permitActiveHours": {
					    "blueZonePermit": "Mo, Tu, We, Th, Fr, Sa 09:00-20:00"
					  },
					  "maximumAllowedStay": "PT2H",
					  "availableSpotNumber": 3,
					  "totalSpotNumber": 6,
					  "extraSpotNumber": 2,
					  "dateModified": "2016-06-02T09:25:55.00Z",
					  "location": {
					    "type": "Polygon",
					    "coordinates": [
					      [
					        [-3.80356167695194, 43.46296641666926 ],
					        [-3.803161973253841,43.46301091092682 ],
					        [-3.803147082548618,43.462879859445884],
					        [-3.803536474744068,43.462838666196674],
					        [-3.80356167695194, 43.46296641666926]
					      ]
					    ]
					  },
					  "areaServed": "Zona Centro",
					  "refParkingGroup": ["daoiz-velarde-1-5-main", "daoiz-velarde-1-5-disabled"]
					},{
					  "id": "accesspoint-trinidade-1",
					  "type": "ParkingAccess",
					  "name": "Trinidade main entrance",
					  "location": {
					    "coordinates": [-8.60961198807, 41.150691773],
					    "type": "Point"
					  },
					  "category": ["vehicleEntrance"],
					  "refOffStreetParking": "porto-OffStreetParking-23889",
					  "features": ["barrier"]
					},{
					  "id": "daoiz-velarde-23-load",
					  "type": "ParkingGroup",
					  "category": ["onstreet", "adjacentSpaces", "loadUnloadZone"],
					  "allowedVehicleType": "car,van,lorry",
					  "chargeType": ["free"],
					  "refParkingSite": "daoiz-velarde-23",
					  "description": "Three parking spots reserved for load and unload",
					  "totalSpotNumber": 3,
					  "availableSpotNumber": 2,
					  "location": {
					    "type": "Polygon",
					    "coordinates": [
					      [
					        [-3.80356167695194, 43.46296641666926 ],
					        [-3.803161973253841,43.46301091092682 ],
					        [-3.803147082548618,43.462879859445884],
					        [-3.803536474744068,43.462838666196674],
					        [-3.80356167695194, 43.46296641666926]
					      ]
					    ]
					  },
					  "requiredPermit": "transportPermit",
					  "permitActiveHours": {
					     "transportPermit": "Mo, Tu, We, Th, Fr, Sa 10:00-14:00"
					  }
					},{
					  "id": "santander:daoiz_velarde_1_5:3",
					  "type": "ParkingSpot",
					  "name": "A-13",
					  "location": {
					    "type": "Point",
					    "coordinates": [-3.80356167695194, 43.46296641666926]
					  },
					  "status": "free",
					  "category": ["onstreet"],
					  "refParkingSite": "santander:daoiz_velarde_1_5"
					}]},
				{
				"context" : "HEBERGEMENT"

					},{
			"context" : "ECLAIRAGE",
			"datamodel" : [{
					    
					  "id": "streetlight:guadalajara:4567",
					  "type": "Streetlight",
					  "location": {
					    "type": "Point",
					    "coordinates": [  -3.164485591715449, 40.62785133667262 ]
					  },
					  "areaServed": "Roundabouts city entrance",
					  "status": "ok",
					  "refStreetlightGroup": "streetlightgroup:G345",
					  "refStreetlightModel": "streetlightmodel:STEEL_Tubular_10m",
					  "circuit": "C-456-A467",
					  "lanternHeight": 10,
					  "locationCategory" : "centralIsland",
					  "powerState": "off",
					  "controllingMethod": "individual",
					  "dateLastLampChange": "2016-07-08T08:02:21.753Z"
					},{
					  "id": "streetlightcontrolcabinet:A45HGJK",
					  "type": "StreetlightControlCabinet",
					  "location": {
					    "type": "Point",
					    "coordinates": [  -3.164485591715449, 40.62785133667262 ]
					  },
					  "cupboardMadeOf": "plastic",
					  "brandName": "Siemens",
					  "modelName": "Simatic S7 1200",
					  "refStreetlightGroup": ["streetlightgroup:BG678", "streetlightgroup:789"],
					  "compliantWith": ["IP54"],
					  "dateLastProgramming": "2016-07-08",
					  "maximumPowerAvailable": 10,
					  "energyConsumed": 162456,
					  "dateMeteringStarted": "2013-07-07",
					  "lastMeterReading": 161237,
					  "meterReadingPeriod": 60,
					  "intensity": {
					     "R": 20.1,
					     "S": 14.4,
					     "T": 22
					  },
					  "reactivePower": {
					    "R": 45,
					    "S": 43.5,
					    "T": 42
					  }
					},{
					  "id": "streetlightgroup:mycity:A12",
					  "type": "StreetlightGroup",
					  "location": {
					    "type": "MultiLineString",
					    "coordinates": [
					      [ [100.0, 0.0], [101.0, 1.0] ],
					      [ [102.0, 2.0], [103.0, 3.0] ]
					    ]
					  },
					  "powerStatus": "on",
					  "areaServed": "Calle Comercial Centro",
					  "circuitId": "C-456-A467",
					  "dateLastSwitchingOn":  "2016-07-07T19:59:06.618Z",
					  "dateLastSwitchingOff": "2016-07-07T07:59:06.618Z",
					  "refStreetlightCabinetController": "cabinetcontroller:CC45A34",
					  "switchingOnHours": [
					    {
					      "from" :  "--11-30",
					      "to" :    "--01-07",
					      "hours" : "Mo,Su 16:00-02:00",
					      "description": "Christmas"
					    }
					  ]
					}]},
				{
			"context" : "DECHETS",
			"datamodel" : [{
					   "id": "wastecontainer:Fleming:12a",
					   "type": "WasteContainer",
					   "refWasteContainerModel": "wastecontainermodel:c1",
					   "refWasteContainerIsle":  "wastecontainerisle:Fleming:12",
					   "serialNumber": "ab56kjl",
					   "location": {
						     "type": "Point",
						     "coordinates": [  -3.164485591715449, 40.62785133667262 ]
					   },
					   "fillingLevel" : 0.4,
					   "dateLastEmptying": "2016-06-21T15:05:59.408Z",
					   "dateNextActuation": "2016-06-28",
					   "status": "ok",
					   "category": ["underground"],
					   "refDevice": ["device-Fleming:12a:1"]
					},{
					   "id": "wastecontainermodel:c1",
					   "type": "WasteContainerModel",
					   "width": 0.50,
					   "height": 0.80,
					   "depth": 0.40,
					   "cargoVolume": 150,
					   "brandName": "Contenedores Ejemplo",
					   "modelName": "C1",
					   "compliantWith": ["UNE-EN 840-2:2013"],
					   "madeOf": "plastic",
					   "features": ["wheels", "lid"],
					   "category": ["dumpster"]
					}]},
					{
			"context" : "PUBLIC",
			"datamodel" : [{
				        "id": "Santander-Garden-Piquio",
				        "type": "Garden",
				        "name": "Jardines de Piquio",
				        "description": "Jardines de Piquio. Zona El Sardinero",
				        "location": {
				            "type": "Point",
				            "coordinates": [-3.7836974, 43.4741091]
				        },
				        "address": {
				            "streetAddress": "Avenida Castañeda",
				            "addressLocality": "Santander",
				            "postalCode": "39005"
				        },
				        "openingHours": "Mo-Su",
				        "style": "french",
				        "category": ["public"],
				        "areaServed": "El Sardinero",
				        "dateLastWatering": "2017-03-31T:08:00",
				        "refRecord": ["Santander-Garden-Piquio-Record-1"]
				    },{  
						"id": "waterqualityobserved:Sevilla:D1",
					   "type": "WaterQualityObserved",
					   "dateObserved": "2017-01-31T06:45:00Z",
					   "measurand": [
					     	"NO3, 0.01, M1, Concentration of Nitrates"
					   ],
					   "location": {
						     "type": "Point",
						     "coordinates": [  -5.993307, 37.362882 ]
					   },
					   "temperature" : 24.4,
					   "conductivity": 0.005,
					   "pH": 7.4,
					   "NO3": 0.01,
					},{
					    "id": "Museum-Barcelona-MACBA-1234",
					    "type": "Museum",
					    "name": "Museo de Arte Contemporaneo de Barcelona",
					    "alternateName": "MACBA",
					    "description": "The MACBA was designed by the American architect Richard Meier and inaugurated in 1995.",
					    "address": {
					       "addressCountry": "ES",
					       "addressLocality": "Barcelona",
					       "streetAddress": "Plaza Dels Àngels, 1"
					    },
					    "museumType": ["fineArts"],
					    "artPeriod": ["contemporary"],
					    "facilities": ["shop", "cloakRoom", "guidedTour"],
					    "location": {
					       "type": "Point",
					       "coordinates": [ 2.1668771521199393, 41.38302235796602]
					    },
					    "openingHoursSpecification": [
					       {
					           "opens":  "11:00",
					           "closes": "19:30",
					           "dayOfWeek": "Mo, Wed, Thu, Fr"
					       },
					       {
					           "opens": "10:00",
					           "closes": "21:00",
					           "dayOfWeek": "Sat"
					       },
					       {
					           "opens": "10:00",
					           "closes": "15:00",
					           "dayOfWeek": "Sun"
					        }
					    ],
					    "touristArea": "Barcelona-Capital",
					    "source": "http://www.tourspain.es"
					},{
					    "id": "PointOfInterest-A-Concha-123456",
					    "type": "PointOfInterest",
					    "name": "Playa de a Concha",
					    "description": "La Playa de A Concha se presenta como una continuación de la Playa de Compostela, una de las más frecuentadas de Vilagarcía.",
					    "address": {
						      "addressCountry": "ES",
						      "addressLocality": "Vilagarcía de Arousa"
					    },
					    "category": ["113"],
					    "location": {
						      "type": "Point",
						      "coordinates": [
							        -8.768460000000001, 42.60214472222222
					      ]
					    },
					    "source": "http://www.tourspain.es",
					    "refSeeAlso": ["Beach-A-Concha-123456"]
					},{
						"id": "SPOI-ES-4326",
						"type": "SmartPointOfInteraction",
						"category": ["co-creation"],
						"areaCovered": {
							  "type": "Polygon",
						"coordinates": [[
							 [25.774, -80.190],
						     [18.466, -66.118],
						     [32.321, -64.757],
						     [25.774, -80.190]
						    ]]
						},
						"applicationUrl": "http://www.example.org",
						"availability": "Tu,Th 16:00-20:00",
						"refRelatedEntity": "POI-PlazaCazorla-3123",
						"refSmartSpot": [ "SSPOT-F94C58E29DD5", "SSPOT-F94C53E21DD2", "SSPOT-F94C51A295D9"]
					},{
						"id": "SSPOT-F94C51A295D9",
						"type": "SmartSpot",
						"announcedUrl" : "http://goo.gl/EJ81JP",
						"signalStrenght": "high",
						"bluetoothChannel": "37-38-39",
						"coverageRadius": 30,
						"announcementPeriod": 500,
						"availability": "Tu,Th 16:00-20:00",
						"refSmartPointOfInteraction": "SPOI-ES-4326"
					},{
					    "id": " Beach-A-Concha-123456 ",
					    "type": "Beach",
					    "name": "Playa de a Concha",
					    "description": "La Playa de A Concha se presenta .....",
					    "address": {
							    "addressCountry": "ES",
						        "addressLocality": "Vilagarcía de Arousa"
						    },
						"beachType": ["whiteSand", "urban", "calmWaters"],
						"occupationRate": "high",
						"facilities": ["promenade", "showers", "cleaningServices", "lifeGuard"],
						"accessType": ["privateVehicle", "onFoot", "publicTransport"],
						"location": {
							   "type": "Point",
							   "coordinates": [-8.768460000000001, 42.60214472222222]
							},
						"width": 51,
						"length": 450,
						"source": "http://www.tourspain.es"
					}]},
					{
			"context" : "METEO",
			"datamodel" : [{ 
					  "awarenessLevel": "Orange",
					  "awarenessType": "Snow/Ice",
					  "source": "http://www.meteoalarm.eu",
					  "address": {
					    "addressCountry": "ES",
					    "addressRegion": "Huesca"
					  },
					  "dateCreated": "2016-03-14T13:54:01",
					  "type": "WeatherAlarm",
					  "id": "WeatherAlarm-83b872975414bfca10832e564a1bb416-7",
					  "validity": {
					    "to": "2016-03-14T23:59:00",
					    "from": "2016-03-14T13:00:00"
					  }
					},{
			        "id": "Spain-WeatherForecast-46005_2016-12-01T18:00:00_2016-12-02T00:00:00",
			        "type": "WeatherForecast",
			        "address":
			        {
			            "addressCountry": "Spain",
			            "postalCode": "46005",
			            "addressLocality": "Valencia"
			        },
			        "dataProvider": "TEF",
			        "dateIssued": "2016-12-01T10:40:01.00Z",
			        "dateRetrieved": "2016-12-01T12:57:24.00Z",
			        "dayMaximum":
			        {
			            "feelsLikeTemperature": 15,
			            "temperature": 15,
			            "relativeHumidity": 0.9
			        },
			        "dayMinimum":
			        {
			            "feelsLikeTemperature": 11,
			            "temperature": 11,
			            "relativeHumidity": 0.7
			        },
			        "feelsLikeTemperature": 12,
			        "precipitationProbability": 0.15,
			        "relativeHumidity": 0.85,
			        "source": "http://www.aemet.es/xml/municipios/localidad_46250.xml",
			        "temperature": 12,
			        "validFrom": "2016-12-01T17:00:00.00Z",
			        "validTo": "2016-12-01T23:00:00.00Z",
			        "validity": "2016-12-01T18:00:00+01:00/2016-12-02T00:00:00+01:00",
			        "weatherType": "overcast",
			        "windDirection": null,
			        "windSpeed": 0
			    },{
		            "id": "Spain-WeatherObserved-2422-2016-11-30T08:00:00",
		            "type": "WeatherObserved",
		            "address":
		            {
		                "addressLocality": "Valladolid",
		                "addressCountry": "ES"
		            },
		            "barometricPressure": 938.9,
		            "dataProvider": "TEF",
		            "dateObserved": "2016-11-30T07:00:00.00Z",
		            "location":
		            {
		                "type": "Point",
		                "coordinates":
		                [
		                    -4.754444444,
		                    41.640833333
		                ]
		            },
		            "precipitation": 0,
		            "pressureTendency": 0.5,
		            "relativeHumidity": 1,
		            "source": "http://www.aemet.es",
		            "stationCode": "2422",
		            "stationName": "Valladolid",
		            "temperature": 3.3,
		            "windDirection": -45,
		            "windSpeed": 2
				}]},
			{
			"context" : "SORTIES", #Hotels, shopping, hebergement, boutiques
			"datamodel" : [{ 

			}
			]}
										]
		
	}
}