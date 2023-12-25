import urllib.parse

def generate_static_map_url():
    base_url = "https://maps.googleapis.com/maps/api/staticmap"
    params = {
        "center": "latitude,longitude",  # Ganti dengan koordinat geografis yang diinginkan
        "zoom": "13",  # Ganti dengan tingkat zoom yang diinginkan
        "size": "600x400",  # Ganti dengan ukuran gambar yang diinginkan
        "markers": "latitude,longitude",  # Ganti dengan koordinat geografis untuk penanda
    }

    # Menggabungkan parameter ke URL
    map_url = f"{base_url}?{urllib.parse.urlencode(params)}"

    return map_url

# Mendapatkan URL peta statis tanpa API key
static_map_url = generate_static_map_url()
print("Static Map URL:", static_map_url)
