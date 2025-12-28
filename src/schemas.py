from pydantic import BaseModel, Field

class CropPriceFeatures(BaseModel):
    # Numerical features (float64 in pandas -> float in Pydantic)
    Temperature_C: float = Field(..., alias='Temperature (°C)')
    Rainfall_mm: float = Field(..., alias='Rainfall (mm)')
    Supply_Volume_tons: float = Field(..., alias='Supply Volume (tons)')
    Demand_Volume_tons: float = Field(..., alias='Demand Volume (tons)')
    Transportation_Cost_per_ton: float = Field(..., alias='Transportation Cost (₹/ton)')
    Fertilizer_Usage_kg_hectare: float = Field(..., alias='Fertilizer Usage (kg/hectare)')
    Pest_Infestation: float = Field(..., alias='Pest Infestation (0-1)')
    Market_Competition: float = Field(..., alias='Market Competition (0-1)')

    # Engineered features (int32 in pandas -> int in Pydantic)
    Year: int
    Month: int

    # One-hot encoded Date features (bool in pandas -> bool in Pydantic)
    Date_2023_01: bool = Field(False, alias='Date_2023-01')
    Date_2023_02: bool = Field(False, alias='Date_2023-02')
    Date_2023_03: bool = Field(False, alias='Date_2023-03')
    Date_2023_04: bool = Field(False, alias='Date_2023-04')
    Date_2023_05: bool = Field(False, alias='Date_2023-05')
    Date_2023_06: bool = Field(False, alias='Date_2023-06')
    Date_2023_07: bool = Field(False, alias='Date_2023-07')
    Date_2023_08: bool = Field(False, alias='Date_2023-08')
    Date_2023_09: bool = Field(False, alias='Date_2023-09')
    Date_2023_10: bool = Field(False, alias='Date_2023-10')
    Date_2023_11: bool = Field(False, alias='Date_2023-11')
    Date_2023_12: bool = Field(False, alias='Date_2023-12')
    Date_2024_01: bool = Field(False, alias='Date_2024-01')
    Date_2024_02: bool = Field(False, alias='Date_2024-02')
    Date_2024_03: bool = Field(False, alias='Date_2024-03')
    Date_2024_04: bool = Field(False, alias='Date_2024-04')
    Date_2024_05: bool = Field(False, alias='Date_2024-05')
    Date_2024_06: bool = Field(False, alias='Date_2024-06')
    Date_2024_07: bool = Field(False, alias='Date_2024-07')
    Date_2024_08: bool = Field(False, alias='Date_2024-08')
    Date_2024_09: bool = Field(False, alias='Date_2024-09')
    Date_2024_10: bool = Field(False, alias='Date_2024-10')
    Date_2024_11: bool = Field(False, alias='Date_2024-11')
    Date_2024_12: bool = Field(False, alias='Date_2024-12')

    # One-hot encoded State features
    State_Karnataka: bool = False
    State_Maharashtra: bool = False
    State_Punjab: bool = False
    State_Tamil_Nadu: bool = Field(False, alias='State_Tamil Nadu')
    State_Uttar_Pradesh: bool = Field(False, alias='State_Uttar Pradesh')
    State_West_Bengal: bool = Field(False, alias='State_West Bengal')

    # One-hot encoded City features
    City_Amritsar: bool = False
    City_Bangalore: bool = False
    City_Belgaum: bool = False
    City_Bellary: bool = False
    City_Chennai: bool = False
    City_Coimbatore: bool = False
    City_Davanagere: bool = False
    City_Durgapur: bool = False
    City_Gulbarga: bool = False
    City_Hubli: bool = False
    City_Kanpur: bool = False
    City_Kolkata: bool = False
    City_Lucknow: bool = False
    City_Ludhiana: bool = False
    City_Madurai: bool = False
    City_Mangalore: bool = False
    City_Mumbai: bool = False
    City_Mysore: bool = False
    City_Nagpur: bool = False
    City_Patiala: bool = False
    City_Pune: bool = False
    City_Shimoga: bool = False
    City_Siliguri: bool = False
    City_Udupi: bool = False
    City_Varanasi: bool = False

    # One-hot encoded Crop Type features
    Crop_Type_Barley: bool = Field(False, alias='Crop Type_Barley')
    Crop_Type_Coffee: bool = Field(False, alias='Crop Type_Coffee')
    Crop_Type_Cotton: bool = Field(False, alias='Crop Type_Cotton')
    Crop_Type_Groundnut: bool = Field(False, alias='Crop Type_Groundnut')
    Crop_Type_Jute: bool = Field(False, alias='Crop Type_Jute')
    Crop_Type_Maize: bool = Field(False, alias='Crop Type_Maize')
    Crop_Type_Millets: bool = Field(False, alias='Crop Type_Millets')
    Crop_Type_Mustard: bool = Field(False, alias='Crop Type_Mustard')
    Crop_Type_Onion: bool = Field(False, alias='Crop Type_Onion')
    Crop_Type_Potato: bool = Field(False, alias='Crop Type_Potato')
    Crop_Type_Pulses: bool = Field(False, alias='Crop Type_Pulses')
    Crop_Type_Rice: bool = Field(False, alias='Crop Type_Rice')
    Crop_Type_Sesame: bool = Field(False, alias='Crop Type_Sesame')
    Crop_Type_Soybean: bool = Field(False, alias='Crop Type_Soybean')
    Crop_Type_Sugarcane: bool = Field(False, alias='Crop Type_Sugarcane')
    Crop_Type_Sunflower: bool = Field(False, alias='Crop Type_Sunflower')
    Crop_Type_Tea: bool = Field(False, alias='Crop Type_Tea')
    Crop_Type_Tobacco: bool = Field(False, alias='Crop Type_Tobacco')
    Crop_Type_Tomato: bool = Field(False, alias='Crop Type_Tomato')
    Crop_Type_Wheat: bool = Field(False, alias='Crop Type_Wheat')

    # One-hot encoded Season features
    Season_Kharif: bool = False
    Season_Post_Monsoon: bool = Field(False, alias='Season_Post-Monsoon')
    Season_Rabi: bool = False
    Season_Zaid: bool = False