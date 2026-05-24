# stat-audit--project-name--sti-2025
# Statistical Health Report — pandas-dev/pandas

> Audit statistik terhadap repository open-source **pandas-dev/pandas** menggunakan konsep Statistika dan Probabilitas (Minggu 11–14) STI 2025.  
> Analisis dilakukan menggunakan GitHub REST API untuk mengevaluasi kesehatan project, probabilitas merge PR, pola issue, dan performa maintenance repository.



# Research Questions

| ID | Pertanyaan | Teknik Statistik | Notebook |
|---|---|---|---|
| RQ1 | Berapa probabilitas Pull Request di pandas-dev/pandas berhasil di-merge? | Bernoulli MLE + CI | `02` + `03` |
| RQ2 | Apakah rata-rata jumlah issue mingguan berubah signifikan setelah major release tertentu? | Poisson MLE + Z-Test | `02` + `04` |
| RQ3 | Berapa probabilitas issue membutuhkan lebih dari 30 hari untuk ditutup? | Monte Carlo Simulation | `05` |



# Tim

| Member | Nama | NIM | Role |
|---|---|---|---|
| A | Tsabita Nuriska R | 1519625050 | Data Engineer |
| B | Nafilham | [NIM] | Estimation Analyst |
| C | Daffa | [NIM] | Inference Analyst |
| D | Yunus | [NIM] | Hypothesis Analyst |
| E | Bintang | [NIM] | Computational Analyst |


# Temuan Utama

*(Bagian ini akan diisi setelah seluruh analisis selesai dilakukan)*

1. blabla
2. TBD
3. TBD


# Struktur Repository

```text
stat-audit-moby-sti-2025/
│
├── README.md
├── AI_USAGE_LOG.md
│
├── data/
│   ├── raw/
│   │   ├── issues_raw.csv
│   │   ├── pulls_raw.csv
│   │   └── releases_raw.csv
│   │
│   └── clean/
│       ├── dataset.csv
│       ├── issues_clean.csv
│       ├── weekly_bug_reports.csv
│       └── pr_merge_dataset.csv
│
├── src/
│   ├── estimator.py
│   ├── inference.py
│   ├── hypothesis.py
│   └── simulation.py
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_estimation.ipynb
│   ├── 03_confidence_interval.ipynb
│   ├── 04_hypothesis_testing.ipynb
│   └── 05_simulation.ipynb
│
├── report/
│   └── statistical_health_report.pdf
│
├── presentation/
│   └── video_link.md
│
├── fetch_data.py
└── requirements.txt
