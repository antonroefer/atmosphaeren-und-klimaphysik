import rasterio
import numpy as np

# Pfad zum DEM/Bathymetrie-Raster
dem_path = "./../data/external/GEBCO/merged.tif"

# Volumen des Eises in m³
ice_volume = 29.4e15

# Dichtekorrektur von Eis zu Wasser (Volumenänderung)
ice_to_water_ratio = 918 / 997

# Erdradius und Pixelgröße
pixel_size_deg = 15 / 3600
earth_radius = 6371000  # Meter

with rasterio.open(dem_path) as src:
    transform = src.transform
    width = src.width
    height = src.height

    # Breitengrade der Zeilen
    latitudes = transform.f + np.arange(height) * transform.e

    # Zellfläche pro Zeile berechnen (m²)
    row_areas = (
        (np.pi / 180)
        * earth_radius**2
        * pixel_size_deg
        * np.abs(
            np.sin(np.radians(latitudes + pixel_size_deg))
            - np.sin(np.radians(latitudes))
        )
    )

    # Initiales Wasservolumen berechnen (nur Zellen ≤ 0)
    initial_water_volume = 0.0

    for row in range(height):
        bathy_row = src.read(1, window=((row, row + 1), (0, width)))[0]  # Zeile lesen
        water_mask = bathy_row <= 0
        initial_water_volume += np.sum(-bathy_row[water_mask] * row_areas[row])

    # Zielvolumen berechnen
    target_volume = initial_water_volume + ice_volume * ice_to_water_ratio

    # Funktion für Wasservolumen bei Meeresspiegel X
    def water_volume_at_level(level):
        volume = 0.0
        for row in range(height):
            bathy_row = src.read(1, window=((row, row + 1), (0, width)))[0]
            flooded_mask = bathy_row < level
            volume += np.sum((level - bathy_row[flooded_mask]) * row_areas[row])
        return volume

    # Adaptive Suche
    steps = [10, 1, 0.1, 0.01]
    level = 71.6

    for step in steps:
        while True:
            new_volume = water_volume_at_level(level)
            if new_volume >= target_volume:
                level -= step
                break
            level += step

print(f"Meeresspiegel Anstieg: {level:.2f} m")
