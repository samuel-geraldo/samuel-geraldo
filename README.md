# Samuel Geraldo

**Saya menganalisis perilaku pelanggan dan pasar, dari data mentah sampai rekomendasi yang bisa dieksekusi.**

Mahasiswa Sistem Informasi UPN Veteran Jakarta, sedang mencari magang Data Analyst / Data Scientist. Setiap project saya mulai dari satu pertanyaan bisnis, bukan dari dataset, dan bug nyata yang saya temui sepanjang jalan saya dokumentasikan.

[LinkedIn](https://linkedin.com/in/samuel-geraldo) · [Email](mailto:samuelgeraldo234@gmail.com) · Jakarta

---

## Pertanyaan yang sudah saya jawab dengan data

### Siapa pelanggan paling bernilai, dan siapa yang cenderung pergi?
**[RFM Segmentation & Cohort Analysis](https://github.com/samuel-geraldo/rfm-cohort-ecommerce)**: 5.861 customer e-commerce, 2009–2011

- 14% customer (segmen Champions) menyumbang 51,5% revenue
- Customer non-UK punya AOV sekitar 1,8x customer UK, dengan frekuensi belanja yang mirip
- Customer churn (>180 hari tidak aktif) punya AOV lebih rendah secara signifikan (uji-t, p = 0,018)
- Metode: RFM quintile scoring, cohort retention matrix, uji-t

### Apakah performa saham pangan berubah setelah Oktober 2024, dan apakah ditentukan posisi di rantai pasok?
**[Analisis Saham Rantai Pasok Pangan IDX](https://github.com/samuel-geraldo/analisis-pangan-idx)**: 6 emiten + IHSG, Januari 2023 sampai sekarang

- JPFA satu-satunya saham yang menguat di kedua periode (+25,9% lalu +48,4%), sementara ICBP berbalik dari +30,7% ke -42,6% dan BISI dari -2,9% ke -50,3%
- Perbedaan antar-periode ini belum signifikan secara statistik (uji-t Welch, semua p > 0,05), dan posisi rantai pasok tidak menjelaskan return (R² = 0,0001, n = 6). Angkanya tampak dramatis tapi belum bisa dibedakan dari fluktuasi normal
- Metode: pipeline Python/pandas/yfinance, database SQLite dengan 5 query analitik (window function, CTE, self-join), dashboard Power BI (MA20, MA50, RSI14)

---

## Cara saya bekerja

- Mulai dari pertanyaan bisnis, baru pilih metode
- Setiap klaim harus bisa direproduksi lewat kode di repo
- Bug nyata dicatat per project, jadi proses berpikirnya bisa dibaca, bukan cuma hasil akhirnya

## Tools

**Analisis:** Python (pandas), SQL (SQLite)
**Visualisasi:** Power BI, matplotlib, seaborn
**Workflow:** Jupyter Notebook, Git & GitHub
