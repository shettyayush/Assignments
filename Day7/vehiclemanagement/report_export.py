import csv

def export_vehicle_data(filename, vehicles):
    """
    Export vehicle data to a CSV file.
    """

    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            # Write header
            writer.writerow([
                "Brand",
                "Model",
                "Year",
                "Owner",
                "Battery Capacity"
            ])

            # Write vehicle data
            for v in vehicles:

                # Get owner safely
                owner = v.get_owner()
                if owner is None:
                    owner = "No Owner Assigned"
                else:
                    owner = owner.replace("Owner: ", "").replace("owner: ", "")

                # Get battery capacity (for ElectricVehicle)
                battery_capacity = getattr(v, "battery_capacity", "N/A")

                writer.writerow([
                    v.brand,
                    v.model,
                    v.year,
                    owner,
                    battery_capacity
                ])

        return f"Vehicle data exported to '{filename}' successfully."

    except IOError as e:
        return f"Error writing to file: {e}"