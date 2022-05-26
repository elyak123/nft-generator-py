config = {
  "layers": [
    {
      "name": "01 Background",
      "values": [
          "Back_7", "Back_8", "Back_9", "Back_10", "Back_11",
        ],
      "trait_path": "./trait-layers/01 Background",
      "filename": [
          "Back_7", "Back_8", "Back_9", "Back_10", "Back_11",
        ],
      "weights": [
        20, 20, 20, 20, 20
      ]
    },
    {
      "name": "Base",
      "values": [
        "Main_cafe-01_nuevo", "Main_gris-01_nuevo"
      ],
      "trait_path": "./trait-layers/02 Base",
      "filename": [
        "Main_cafe-01_nuevo", "Main_gris-01_nuevo"
      ],
      "weights": [50, 50]
    },
    {
      "name": "03 Mouths",
      "values": [
        "Boca_cafe_cerrada", "Boca_cafe", "Boca_gris_cerrada", "Boca_gris",
      ],
      "trait_path": "./trait-layers/03 Mouths",
      "filename": [
        "Boca_cafe_cerrada", "Boca_cafe", "Boca_gris_cerrada", "Boca_gris",
      ],
      "weights": [25, 25, 25, 25]
    },
    {
      "name": "04 Eyes",
      "values": [
        "Ojos_cafes-01", "Ojos_gris-01"
      ],
      "trait_path": "./trait-layers/04 Eyes",
      "filename": [
        "Ojos_cafes-01", "Ojos_gris-01"
      ],
      "weights": [
        50, 50,
      ]
    },
    {
      "name": "05 Glasses",
      "values": [
        "Black-Glasses-Transparent", "Black-Glasses-Yellow", "Black-Glasses",
      ],
      "trait_path": "./trait-layers/05 Glasses",
      "filename": [
        "Black-Glasses-Transparent", "Black-Glasses-Yellow", "Black-Glasses",
      ],
      "weights": [
        10, 10, 10,
      ]
    },
    {
      "name": "06 Hats",
      "values": [
        "Cap_1", "Cap_2", "HeadPhones_Beat",
      ],
      "trait_path": "./trait-layers/06 Hats",
      "filename": [
        "Cap_1", "Cap_2", "HeadPhones_Beat",
      ],
      "weights": [33, 33, 34]
    },
    {
      "name": "07 T-Shirts",
      "values": [
        "Hoddie_1", "TShirt_flowers_2", "TShirt_flowers", "TShirt_RayasMarinero_azul",
        ],
      "trait_path": "./trait-layers/07 T-Shirts",
      "filename": [
        "Hoddie_1", "TShirt_flowers_2", "TShirt_flowers", "TShirt_RayasMarinero_azul",
      ],
      "weights": [16, 16, 16, 16,]
    },
  ],
  "incompatibilities": [
    # {
    #   "layer": "Head",
    #   "value": "Face_2",
    #   "incompatible_with": [
    #     "Black-Glasses-Transparent", "Black-Glasses-Yellow", "Black-Glasses", "Lens_1", "Lens_2", "Lens_3",
    #     "Hat_1", "Hat_2", "HeadPhones_Beat"
    #   ]
    # },
    # {
    #   "layer": "Head",
    #   "value": "Head_2",
    #   "incompatible_with": [
    #     "Black-Glasses-Transparent", "Black-Glasses-Yellow", "Black-Glasses", "Lens_1", "Lens_2", "Lens_3",
    #     "Hat_1", "Hat_2", "HeadPhones_Beat"
    #   ]
    # },
    # {
    #   "layer": "Head",
    #   "value": "Helmet_1",
    #   "incompatible_with": [
    #     "Black-Glasses-Transparent", "Black-Glasses-Yellow", "Black-Glasses", "Lens_1", "Lens_2", "Lens_3",
    #     "Hat_1", "Hat_2", "HeadPhones_Beat"
    #   ]
    # }
    # {
    #   "layer": "Background",
    #   "value": "Blue",
    #   "incompatible_with": ["Python Logo 2"]
    # },  #  @dev : Blue backgrounds will never have the attribute "Python Logo 2".
  ],
  "baseURI": ".",
  "name": "NFT #",
  "description": "This is a description for this NFT series."
}
