import math

# Constants for the atmosphere
mass_of_atmosphere = 5.148e18  # kg
specific_heat_capacity_atmosphere = 1.2e3  # J / kg / K
temperature_change_atmos = 1  # K

# Calculate the energy required for the atmosphere
energy_required_atmosphere = (
    mass_of_atmosphere * specific_heat_capacity_atmosphere * temperature_change_atmos
)

# Output the result for the atmosphere
print(
    f"Energie benötigt, um die gesamte Atmosphäre um 1K zu erwärmen: {energy_required_atmosphere:.2e} J"
)

# Constants
specific_heat_capacity = 4.20e3  # J / kg / K
density_of_water = 1025  # kg / m^3
volume_of_ocean = 1.4e21 * (8.5 / (70.8))  # m^3
temperature_change = 0.1  # K

# Calculate the mass of the ocean
mass_of_ocean = density_of_water * volume_of_ocean  # in kg

# Calculate the energy required
energy_required = mass_of_ocean * specific_heat_capacity * temperature_change  # in J

# Output the result
print(
    f"Energie benötigt, um die oberen 1000m des Ozeans um 0.1K zu erwärmen: {energy_required:.2e} J"
)

# Constants for land ice
volume_of_land_ice = 29.4e6 * 1e6 * 1e3  # m^3 (convert km^3 to m^3)
density_of_ice = 917  # kg / m^3
specific_heat_capacity_ice = 2.1e3  # J / kg / K
latent_heat_of_fusion = 334e3  # J / kg
temperature_change_ice = 25  # K (from -25°C to 0°C)

# Calculate the mass of the land ice
mass_of_land_ice = density_of_ice * volume_of_land_ice  # in kg

# Calculate the energy required to warm the ice to 0°C
energy_to_warm_ice = (
    mass_of_land_ice * specific_heat_capacity_ice * temperature_change_ice
)  # in J

# Calculate the energy required to melt the land ice
energy_to_melt_land_ice = mass_of_land_ice * latent_heat_of_fusion  # in J

# Total energy required
total_energy_for_land_ice = energy_to_warm_ice + energy_to_melt_land_ice

# Output the result for land ice
print(
    f"Energie benötigt, um das gesamte globale Landeis von -25°C auf 0°C zu erwärmen und zu schmelzen: {total_energy_for_land_ice:.2e} J"
)
