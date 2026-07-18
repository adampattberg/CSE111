import math

# Modifiers

TRACTION = {
    "low": 0.60,
    "medium": 0.75,
    "good": 0.95,
    "great": 1.10
}

TIRES = {
    "snow": -0.15,
    "all season": -0.05,
    "performance": 0.05,
    "track": 0.15
}

ROAD = {
    "snowy": -0.25,
    "wet": -0.10,
    "dry": 0.00,
    "prepped": 0.10
}

DRIVETRAIN = {
    "fwd": 0.00,
    "rwd": 0.05,
    "awd": 0.15
}

TRANSMISSION = {
    "automatic": 0.00,
    "manual": 0.20
}

DRIVER = {
    "beginner": 0.40,
    "average": 0.20,
    "experienced": 0.00
}


# ----------------------------
# Functions
# ----------------------------

def get_vehicle_info():
    """Gets the vehicle's weight and horsepower."""
    weight = float(input("Vehicle weight (lbs): "))
    horsepower = float(input("Horsepower: "))
    return weight, horsepower


def get_conditions():
    """Gets traction and driver-related conditions."""
    print()

    base = input("Traction (low, medium, good, great): ").lower()
    tires = input("Tires (snow, all season, performance, track): ").lower()
    road = input("Road (snowy, wet, dry, prepped): ").lower()
    drivetrain = input("Drive Type (fwd, rwd, awd): ").lower()

    print()

    transmission = input("Transmission (automatic, manual): ").lower()
    driver = input("Driver Skill (beginner, average, experienced): ").lower()

    return base, tires, road, drivetrain, transmission, driver


def calculate_traction(base, tires, road, drivetrain):
    traction = (
        TRACTION[base]
        + TIRES[tires]
        + ROAD[road]
        + DRIVETRAIN[drivetrain]
    )

    traction = max(0.50, min(1.30, traction))

    return traction


def estimate_zero_to_sixty(weight, horsepower, traction,
                           transmission, driver):
    """Returns estimated 0-60 time in seconds."""

    power_weight = weight / horsepower
    base_time = (power_weight ** (1 / 3)) * 2.8

    time = base_time / traction

    time += TRANSMISSION[transmission]
    time += DRIVER[driver]

    return round(time, 2)


def main():
    weight, horsepower = get_vehicle_info()

    (base,
     tires,
     road,
     drivetrain,
     transmission,
     driver) = get_conditions()

    traction = calculate_traction(base, tires, road, drivetrain)

    time = estimate_zero_to_sixty(
        weight,
        horsepower,
        traction,
        transmission,
        driver
    )

    print()
    print(f"Estimated 0-60 mph: {time:.2f} seconds")

if __name__ == "__main__":
    main()