import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Path ke file kredensial JSON yang diunduh
json_keyfile = 'path/to/your/credentials.json'

# Buat koneksi menggunakan kredensial
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(json_keyfile, scope)
client = gspread.authorize(creds)

# Buka spreadsheet berdasarkan nama atau URL
spreadsheet = client.open('Nama_Spreadsheet')

# Pilih lembar kerja (worksheet) berdasarkan nama
worksheet = spreadsheet.get_worksheet(0)

# Baca nilai sel tertentu
cell_value = worksheet.cell(1, 1).value
print(f'Nilai di sel A1: {cell_value}')

# Baca seluruh nilai dalam lembar kerja
all_values = worksheet.get_all_values()
print('Seluruh Nilai dalam Lembar Kerja:')
for row in all_values:
    print(row)
