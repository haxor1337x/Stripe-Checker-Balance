Stripe API Key Validator Include Balance
========================

Aplikasi ini digunakan untuk memvalidasi kunci API Stripe dan mengecek saldo akun Stripe yang valid.

Cara penggunaan
---------------

1.  Pastikan Anda sudah menginstall library `stripe` dan `termcolor`. Jika belum, install dengan menjalankan perintah berikut di terminal:

Copy code

`pip install stripe pip install termcolor`

2.  Simpan kunci API Stripe yang akan divalidasi dalam file `key.txt`. Setiap baris pada file tersebut harus berisi satu API key.
    
3.  Jalankan program dengan menjalankan perintah berikut di terminal:
    

Copy code

`python stripe_validator.py`

4.  Setelah program selesai memvalidasi API key, Anda akan ditanya apakah ingin melanjutkan untuk mengecek saldo akun Stripe. Jawab `y` untuk melanjutkan dan `n` untuk keluar dari program.
    
5.  Jika Anda memilih untuk melanjutkan, program akan mengecek saldo akun Stripe yang valid dan menyimpan hasil ke dalam file `results.txt`.
    

Penjelasan kode
---------------

1.  Program akan membuka file `key.txt` dan membaca API key Stripe yang akan divalidasi.
    
2.  Program akan memvalidasi setiap API key dengan memanggil method `Balance.retrieve()` dari Stripe API. Jika berhasil, API key akan disimpan ke dalam file `validkey.txt` dan pesan validasi akan dicetak dengan warna hijau. Jika gagal, pesan error akan dicetak dengan warna merah dan program akan melanjutkan ke API key berikutnya.
    
3.  Setelah program selesai memvalidasi API key, user akan ditanya apakah ingin melanjutkan untuk mengecek saldo akun Stripe yang valid. Jika user memilih untuk melanjutkan, program akan membuka file `validkey.txt` dan membaca API key Stripe yang valid.
    
4.  Program akan mengecek saldo akun Stripe yang valid dengan memanggil method `Balance.retrieve()` dari Stripe API dan menyimpan hasil ke dalam file `results.txt`.
