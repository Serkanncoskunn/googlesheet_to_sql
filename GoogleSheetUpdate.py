import tkinter as tk
from tkinter import messagebox, ttk
import gspread
import pyodbc
import re
import json
from urllib.parse import urlparse

# Kullanıcı bilgilerini kaydetme ve yükleme
CONFIG_FILE = "config.json"

def save_config(data):
    with open(CONFIG_FILE, "w") as f:
        json.dump(data, f)

def load_config():
    try:
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Google Sheets URL'si üzerinden sheet_id'yi al
def extract_sheet_id(url):
    parsed_url = urlparse(url)
    sheet_id = parsed_url.path.split('/')[3]  
    return sheet_id

# Google Sheets verilerini SQL Server'a aktar
def update_sql_table(sheet_url, client_file, server, database, username, password, table_name):
    try:
        gc = gspread.service_account(filename=client_file)
        sheet_id = extract_sheet_id(sheet_url)
        spreadsheet = gc.open_by_key(sheet_id)
        sheet = spreadsheet.get_worksheet(0)  

        rows = sheet.get_all_records()
        columns = [re.sub(r'\s+', '_', col) for col in rows[0].keys()] if rows else []

        conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};'
        connection = pyodbc.connect(conn_str)
        cursor = connection.cursor()

        if columns:
            # SQL Server'da aynı isimde bir tablo varsa, sil
            drop_table_sql = f"IF OBJECT_ID('{table_name}', 'U') IS NOT NULL DROP TABLE {table_name}"
            cursor.execute(drop_table_sql)

            # Yeni tabloyu oluştur
            create_table_sql = f"""
            CREATE TABLE {table_name} (
                {', '.join([f'[{col}] VARCHAR(255)' for col in columns])}
            );
            """
            cursor.execute(create_table_sql)

            # Verileri tabloya ekle
            for row in rows:
                sql = f"INSERT INTO {table_name} ({', '.join([f'[{col}]' for col in columns])}) VALUES ({', '.join(['?' for _ in columns])})"
                cursor.execute(sql, tuple(row[col] for col in rows[0].keys()))

            connection.commit()

        cursor.close()
        connection.close()
        messagebox.showinfo("Başarı", "Veri başarıyla güncellendi!")
    except Exception as e:
        messagebox.showerror("Hata", f"Bir hata oluştu: {str(e)}")

# GUI Penceresi
def create_gui():
    root = tk.Tk()
    root.title("Google Sheets - SQL Güncelleme")

    labels = ["SQL Server Adı:", "Veritabanı Adı:", "Kullanıcı Adı:", "Şifre:", "Google Cloud JSON Dosyası:", "Google Sheets URL:", "SQL Tablo Adı:"]
    entries = {}
    saved_config = load_config()

    for label in labels:
        tk.Label(root, text=label).pack(pady=5)
        entry = tk.Entry(root, width=50, show="*" if "Şifre" in label else None)
        entry.insert(0, saved_config.get(label, ""))  # Önceden kaydedilmiş değeri yükle
        entry.pack(pady=5)
        entries[label] = entry

    remember_var = tk.BooleanVar(value=True)
    remember_check = tk.Checkbutton(root, text="Bilgileri Hatırla", variable=remember_var)
    remember_check.pack(pady=5)

    def start_update():
        config_data = {}
        for label in labels:
            config_data[label] = entries[label].get()

        if remember_var.get():
            save_config(config_data)

        update_sql_table(
            config_data["Google Sheets URL:"],
            config_data["Google Cloud JSON Dosyası:"],
            config_data["SQL Server Adı:"],
            config_data["Veritabanı Adı:"],
            config_data["Kullanıcı Adı:"],
            config_data["Şifre:"],
            config_data["SQL Tablo Adı:"]
        )

    start_button = tk.Button(root, text="Veriyi Güncelle", command=start_update)
    start_button.pack(pady=20)

    root.mainloop()

# GUI'yi başlat
create_gui()
