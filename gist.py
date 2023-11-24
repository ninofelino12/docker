import requests
import json
import webbrowser

def get_gists(username):
    url = f"https://api.github.com/users/{username}/gists"
    response = requests.get(url)

    if response.status_code == 200:
        gists = json.loads(response.text)
        return gists
    else:
        return None

# Ganti "your_username" dengan nama pengguna GitHub Anda
username = "ninofelino12"
gists = get_gists(username)

if gists:
    print(f"Daftar Gist untuk pengguna {username}:\n")
    for gist in gists:
        print(f"Nama: {gist['description'] if gist['description'] else 'Tidak ada deskripsi'}")
        print(f"URL: {gist['html_url']}")
        print(f"==================================\n")
        webbrowser.open(gist['html_url'])
else:
    print(f"Tidak dapat mengambil daftar Gist untuk pengguna {username}")
