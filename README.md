# UTS Pengolahan Citra

## 1. Jelaskan apa yang dimaksud dengan image enhancement!

Image enhancement adalah perbaikan kualitas citra yang bertujuan memperoleh citra yang lebih sesuai, dan digunakan untuk aplikasi lebih lanjut (misal: mengenali objek di dalam citra) jadi singkatnya, Image Enhancement adalah proses memanipulasi citra untuk meningkatkan kualitas visualnya, sehingga lebih mudah diinterpretasikan atau dianalisis oleh manusia maupun sistem.

## 2. Peningkatan Kontras Menggunakan Histogram Equalization

[bisa dicek disini](./app.py)

## 3. Buatlah program contrast menggunakan python dengan level 1.5 kemudian bandingkan hasilnya dengan teknik Histogram Equalization pada nomor 2.

### Histogram Equalization (HE):

- Sifatnya Adaptif: Memanfaatkan histogram untuk mendistribusikan intensitas piksel sehingga kontras lebih merata.
- Natural: Cenderung mempertahankan detail visual seperti pola terang dan gelap pada gambar asli.
- Kelebihan: Cocok untuk gambar yang secara keseluruhan memiliki distribusi intensitas rendah (gelap atau buram).
- Kelemahan: Tidak selalu efektif untuk gambar dengan area terang yang dominan, karena distribusi histogram bisa bias.

### Linear Adjustment (Level 1.5):

- Sifatnya Linear: Meningkatkan atau mengurangi intensitas piksel secara proporsional dari nilai tengah (128).
- Lebih Ekstrim: Menghasilkan gambar yang lebih terang secara keseluruhan, tetapi sering menyebabkan area terang menjadi terlalu terang (saturated) dan area gelap kehilangan detail.
- Kelebihan: Mudah diterapkan, cocok untuk meningkatkan visibilitas secara cepat.
- Kelemahan: Over-enhancement sering terjadi, terutama pada gambar dengan kontras rendah yang sudah memiliki area terang atau gelap dominan.

### Kesimpulan dari Analisis:

- HE akan menunjukkan peningkatan distribusi nilai piksel yang lebih merata (histogram menyebar).
- Level 1.5 akan menunjukkan peningkatan intensitas secara linear tetapi bisa menyebabkan over-enhancement.
- Dalam kasus tertentu, HE cenderung lebih cocok karena mempertahankan detail lokal.
