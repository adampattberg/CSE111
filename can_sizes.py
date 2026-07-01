import math

def main():

    name = "#1 Picnic"
    r = 6.83
    h = 10.16
    vol = compute_volume(r, h)
    surf_area = compute_surface_area(r, h)
    stor_eff = compute_storage_eff(vol, surf_area)
    print(f"The storage efficiency of {name} is {stor_eff:.2f}")
    
    name = "#1 Tall"
    r = 7.78
    h = 11.91
    vol = compute_volume(r, h)
    surf_area = compute_surface_area(r, h)
    stor_eff = compute_storage_eff(vol, surf_area)
    print(f"The storage efficiency of {name} is {stor_eff:.2f}")

    name = "#2"
    r = 8.73
    h = 11.59
    vol = compute_volume(r, h)
    surf_area = compute_surface_area(r, h)
    stor_eff = compute_storage_eff(vol, surf_area)
    print(f"The storage efficiency of {name} is {stor_eff:.2f}")

    name = "#2.5"
    r = 10.32
    h = 11.91
    vol = compute_volume(r, h)
    surf_area = compute_surface_area(r, h)
    stor_eff = compute_storage_eff(vol, surf_area)
    print(f"The storage efficiency of {name} is {stor_eff:.2f}")

    name = "#3 Cylinder"
    r = 10.79
    h = 17.78
    vol = compute_volume(r, h)
    surf_area = compute_surface_area(r, h)
    stor_eff = compute_storage_eff(vol, surf_area)
    print(f"The storage efficiency of {name} is {stor_eff:.2f}")

    name = "#5"
    r = 13.02
    h = 14.29
    vol = compute_volume(r, h)
    surf_area = compute_surface_area(r, h)
    stor_eff = compute_storage_eff(vol, surf_area)
    print(f"The storage efficiency of {name} is {stor_eff:.2f}")

    name = "#6Z"
    r = 5.40
    h = 8.89
    vol = compute_volume(r, h)
    surf_area = compute_surface_area(r, h)
    stor_eff = compute_storage_eff(vol, surf_area)
    print(f"The storage efficiency of {name} is {stor_eff:.2f}")

    name = "#8Z Short"
    r = 6.83
    h = 7.62
    vol = compute_volume(r, h)
    surf_area = compute_surface_area(r, h)
    stor_eff = compute_storage_eff(vol, surf_area)
    print(f"The storage efficiency of {name} is {stor_eff:.2f}")

    name = "#10"
    r = 15.72
    h = 17.78
    vol = compute_volume(r, h)
    surf_area = compute_surface_area(r, h)
    stor_eff = compute_storage_eff(vol, surf_area)
    print(f"The storage efficiency of {name} is {stor_eff:.2f}")

    name = "#211"
    r = 6.83
    h = 12.38
    vol = compute_volume(r, h)
    surf_area = compute_surface_area(r, h)
    stor_eff = compute_storage_eff(vol, surf_area)
    print(f"The storage efficiency of {name} is {stor_eff:.2f}")

    name = "#300"
    r = 7.62
    h = 11.27
    vol = compute_volume(r, h)
    surf_area = compute_surface_area(r, h)
    stor_eff = compute_storage_eff(vol, surf_area)
    print(f"The storage efficiency of {name} is {stor_eff:.2f}")

    name = "#303"
    r = 8.10
    h = 11.11
    vol = compute_volume(r, h)
    surf_area = compute_surface_area(r, h)
    stor_eff = compute_storage_eff(vol, surf_area)
    print(f"The storage efficiency of {name} is {stor_eff:.2f}")

def compute_volume(radius, height):
    volume = math.pi * (radius**2) * height
    return volume

def compute_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

def compute_storage_eff(can_volume, can_surface_area):
    storage_efficiency = can_volume / can_surface_area
    return storage_efficiency

main()