# buat_data_stats.py
# Membuat kartu data-stats.svg untuk README profil GitHub.
# Angka dijumlahkan otomatis dari semua project di daftar PROJECTS.
#
# Cara pakai:
#   1. Tambah/ubah project di daftar PROJECTS (satu blok per project).
#   2. Jalankan:  python buat_data_stats.py
#   3. Upload data-stats.svg yang dihasilkan ke repo samuel-geraldo (menimpa yang lama).

from xml.sax.saxutils import escape

PROJECTS = [
    {
        "nama": "RFM & Cohort E-commerce",
        "rows_raw": 1_067_371,    # baris mentah sebelum cleaning
        "rows_clean": 776_624,    # baris setelah cleaning
        "sql_queries": 4,
        "stat_tests": 1,          # uji-t Welch AOV churned vs active
        "charts": 4,              # grafik + dashboard
        "bugs": 3,                # bug terdokumentasi (docs/bugs.md)
    },
    {
        "nama": "Saham Pangan IDX",
        "rows_raw": 5_894,        # 842 hari x 7 ticker (setelah dropna + ffill)
        "rows_clean": 5_894,
        "sql_queries": 5,
        "stat_tests": 8,          # 7 uji-t Welch + 1 regresi
        "charts": 7,              # 6 grafik unik (korelasi, Sharpe, drawdown, forecast, excess return,
                                  # return kumulatif; Sharpe versi slide tidak dihitung dua kali) + 1 dashboard Power BI
        "bugs": 4,                # README bagian Kendala & Debugging
    },
    {
        "nama": "Riset Pasar E-commerce (Magang)",   # PRIVAT: jangan tampilkan nama/merek/harga/repo
        "rows_raw": 300,          # baris hasil pencarian (225 produk unik)
        "rows_clean": 199,        # beras dengan harga/kg valid; 32 outlier hanya ditandai (167 tanpa outlier)
        "sql_queries": 0,         # tidak ada query analitik; analisis dikerjakan di Python
        "stat_tests": 0,          # hanya statistik deskriptif
        "charts": 0,
        "bugs": 5,                # terdokumentasi di file repo (diverifikasi dengan nomor baris)
    },
    # Contoh project berikutnya (hapus tanda # untuk mengaktifkan):
    # {
    #     "nama": "Bank Lead Scoring",
    #     "rows_raw": 11_162, "rows_clean": 11_162,
    #     "sql_queries": 0, "stat_tests": 0, "charts": 5, "bugs": 0,
    # },
]

OUTPUT = "data-stats.svg"

# Warna kartu (tema Tokyo Night). Ganti hex di sini kalau mau tone lain.
THEME = {
    "bg": "#1a1b27",
    "border": "#70a5fd",
    "title": "#70a5fd",
    "label": "#38bdae",
    "value": "#c0caf5",
    "hero": "#70a5fd",
    "caption": "#bf91f3",
    "sub": "#787c99",
}

def total(key):
    return sum(p[key] for p in PROJECTS)

def fmt(n):
    return f"{n:,}"

def hero(n):
    return f"{n / 1_000_000:.2f}M" if n >= 1_000_000 else f"{n / 1_000:.1f}K"

rows = [
    ("Data projects:", str(len(PROJECTS))),
    ("Rows processed:", fmt(total("rows_raw"))),
    ("Clean rows produced:", fmt(total("rows_clean"))),
    ("SQL queries:", str(total("sql_queries"))),
    ("Statistical tests:", str(total("stat_tests"))),
    ("Charts & dashboards:", str(total("charts"))),
    ("Bugs documented:", str(total("bugs"))),
]

W, y0, step = 540, 80, 26
H = y0 + (len(rows) - 1) * step + 32
body = ""
for i, (k, v) in enumerate(rows):
    y = y0 + i * step
    body += (f'  <text x="25" y="{y}" class="label">{escape(k)}</text>\n'
             f'  <text x="215" y="{y}" class="value">{escape(v)}</text>\n')

cx, cy = 445, H // 2 - 6
svg = f'''<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="t d">
  <title id="t">Samuel's Data Stats</title>
  <desc id="d">Ringkasan data yang dibersihkan dan dianalisis di seluruh project portofolio.</desc>
  <style>
    .title {{ font: 600 18px 'Segoe UI', Ubuntu, 'Helvetica Neue', Sans-Serif; fill: {THEME['title']}; }}
    .sub {{ font: 400 11px 'Segoe UI', Ubuntu, 'Helvetica Neue', Sans-Serif; fill: {THEME['sub']}; }}
    .label {{ font: 600 14px 'Segoe UI', Ubuntu, 'Helvetica Neue', Sans-Serif; fill: {THEME['label']}; }}
    .value {{ font: 600 14px 'Segoe UI', Ubuntu, 'Helvetica Neue', Sans-Serif; fill: {THEME['value']}; }}
    .hero {{ font: 700 34px 'Segoe UI', Ubuntu, 'Helvetica Neue', Sans-Serif; fill: {THEME['hero']}; }}
    .cap {{ font: 600 12px 'Segoe UI', Ubuntu, 'Helvetica Neue', Sans-Serif; fill: {THEME['caption']}; }}
  </style>
  <rect x="0.5" y="0.5" rx="4.5" width="{W-1}" height="{H-1}" fill="{THEME['bg']}" stroke="{THEME['border']}" stroke-opacity="0.35"/>
  <text x="25" y="36" class="title">Samuel's Data Stats</text>
  <text x="25" y="54" class="sub">All data projects combined</text>
{body}  <text x="{cx}" y="{cy}" class="hero" text-anchor="middle">{hero(total("rows_raw"))}</text>
  <text x="{cx}" y="{cy+22}" class="cap" text-anchor="middle">rows processed</text>
  <text x="{cx}" y="{cy+42}" class="sub" text-anchor="middle">{fmt(total("rows_clean"))} clean rows out</text>
</svg>
'''
with open(OUTPUT, "w", encoding="utf-8") as f:
    f.write(svg)

print(f"Tersimpan: {OUTPUT}")
for k, v in rows:
    print(f"  {k:<24}{v}")
