config = {
  "layers": [
    {
      "name": "Background",
      "values": [
          "Blueberry", "Glow", "Teal", "Light_Pumkin", "Pond Green",
        ],
      "trait_path": "./trait-layers/01 Background",
      "filename": [
        "Blueberry", "Glow", "Teal", "Light_Pumkin", "Pond Green",
        ],
      "weights": [
        20, 20, 20, 20, 20
      ]
    },
    {
      "name": "Base",
      "values": [
        "Dark_Brown", "Main_Gray"
      ],
      "trait_path": "./trait-layers/02 Base",
      "filename": [
        "Dark_Brown", "Main_Gray"
      ],
      "weights": [50, 50]
    },
    {
      "name": "Mouths",
      "values": [
        "Crazy_Gray", "Crazy_Light", "Cyber_Mounth", "Gray_Serious", "Gray_Smile", "Light_Serious", "Light_Smile", "Zombie_Mouth"
      ],
      "trait_path": "./trait-layers/03 Mouths",
      "filename": [
        "Crazy_Gray", "Crazy_Light", "Cyber_Mounth", "Gray_Serious", "Gray_Smile", "Light_Serious", "Light_Smile", "Zombie_Mouth"
      ],
      "weights": [10, 10, 5, 20, 15, 20, 15, 5]
    },
    {
      "name": "Eyes",
      "values": [
        "Brown_Eyes", "Gray_Eyes"
      ],
      "trait_path": "./trait-layers/04 Eyes",
      "filename": [
        "Brown_Eyes", "Gray_Eyes"
      ],
      "weights": [
        50, 50,
      ]
    },
    {
      "name": "Glasses",
      "values": [
        "Black_Shades", "Crazy Eyes", "Diamond_Eyes", "Geek_Glases", "Golden_Shades", "Laser_Eyes", "Monocle_Eyes", "No_Glasses", "Virtual_Reality"
      ],
      "trait_path": "./trait-layers/05 Glasses",
      "filename": [
        "Black_Shades", "Crazy Eyes", "Diamond_Eyes", "Geek_Glases", "Golden_Shades", "Laser_Eyes", "Monocle_Eyes", "No_Glasses", "Virtual_Reality"
      ],
      "weights": [
        12, 12, 12, 12, 12, 10, 10, 10, 10,
      ]
    },
    {
      "name": "Hats",
      "values": [
        "Baseball_Black", "Baseball_Blue", "Black_Headphones", "Bucket_Hat_Black", "Cowboy_Hat", "Edgy_Hat_Black", "Edgy_Hat_Pink", "Pink_Headphones", "World_War_Helmet"
      ],
      "trait_path": "./trait-layers/06 Hats",
      "filename": [
        "Baseball_Black", "Baseball_Blue", "Black_Headphones", "Bucket_Hat_Black", "Cowboy_Hat", "Edgy_Hat_Black", "Edgy_Hat_Pink", "Pink_Headphones", "World_War_Helmet"
      ],
      "weights": [12, 12, 12, 12, 12, 10, 10, 10, 10,]
    },
    {
      "name": "T-Shirts",
      "values": [
        "Bathrobe_Black", "Bathrobe_Gray", "Biker_Jacket_Black", "Biker_Jacket_Brown", "Blue_Baseball_T", "Flowers_T_Dark", "Flowers_T_Light", "Formal_Jacket_Gray", "Hoodie_Hat_Black", "Regular_T_Black", "Squares_Jacket_Blue", "Stripes_Blue_White", "Stripes_DarkBlue_White", "Swat_Vest"
        ],
      "trait_path": "./trait-layers/07 T-Shirts",
      "filename": [
        "Bathrobe_Black", "Bathrobe_Gray", "Biker_Jacket_Black", "Biker_Jacket_Brown", "Blue_Baseball_T", "Flowers_T_Dark", "Flowers_T_Light", "Formal_Jacket_Gray", "Hoodie_Hat_Black", "Regular_T_Black", "Squares_Jacket_Blue", "Stripes_Blue_White", "Stripes_DarkBlue_White", "Swat_Vest"
      ],
      "weights": [8, 8, 7, 7,7, 7, 7, 7,7, 7, 7, 7,]
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
