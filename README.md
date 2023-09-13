1.Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Untuk mengimplementasikan checklist yang diberikan, saya memulai dengan membuat proyek Django baru dengan menggunakan perintah django-admin startproject projectname di terminal. Setelah proyek berhasil dibuat, saya membuat aplikasi baru dengan nama 'main' menggunakan perintah python manage.py startapp main. Aplikasi ini kemudian saya tambahkan ke dalam INSTALLED_APPS di file settings.py proyek saya.

Selanjutnya, saya melakukan konfigurasi routing di file urls.py proyek saya dengan menambahkan path('main/', include('main.urls')) ke dalam urlpatterns. Hal ini memungkinkan proyek Django saya untuk menjalankan aplikasi 'main' yang baru saja saya buat. Di dalam aplikasi 'main', saya membuat model baru dengan nama 'Item' di file models.py. Model 'Item' ini memiliki atribut 'name', 'amount', dan 'description' dengan tipe data sesuai yang diminta. Saya juga membuat fungsi view baru di file views.py aplikasi main yang merender template HTML dan mengembalikan respons HTTP.

Untuk memetakan fungsi view yang baru saja dibuat, saya memperbarui file urls.py aplikasi main dengan menambahkan path('', views.index, name='index') ke dalam urlpatterns. Setelah aplikasi selesai dibuat, saya melakukan deployment ke Adaptable. Untuk ini, saya membuat file requirements.txt yang mencantumkan semua dependencies yang diperlukan oleh aplikasi. Selanjutnya, saya menggunakan GitHub Actions sebagai runner dan Heroku sebagai platform hosting aplikasi.

Terakhir, saya membuat file README.md di root direktori proyek saya. Di dalam file ini, saya menuliskan tautan menuju aplikasi yang sudah di-deploy dan menjawab pertanyaan yang diberikan. Saya menggunakan Markdown untuk formatting teks di file README.md. Dengan demikian, teman-teman saya dapat mengakses aplikasi yang sudah saya buat melalui Internet.

2.Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

Request Client  --> URLs (urls.py) --> Views (views.py) --> Models (models.py) --> Template (HTML)
Proses komunikasi dalam aplikasi web berbasis Django melibatkan beberapa komponen utama yang saling berinteraksi. Ketika seorang user atau client mengirimkan permintaan (request) ke server dengan membuka alamat URL di browser, Django memulai proses penanganan permintaan tersebut.

Dalam langkah pertama, permintaan dari user diterima oleh Django dan dicocokkan dengan pola URL yang telah didefinisikan dalam file urls.py. Jika terdapat pola URL yang cocok dengan permintaan tersebut, Django akan mengarahkan permintaan tersebut ke fungsi view yang sesuai.

Fungsi view, yang terdapat dalam file views.py, memiliki tugas utama untuk memproses permintaan yang diterima. Proses ini dapat melibatkan interaksi dengan model yang didefinisikan dalam file models.py. Model ini merepresentasikan struktur data dalam basis data dan memungkinkan fungsi view untuk melakukan operasi CRUD (Create, Read, Update, Delete) terhadap data.

Selain berinteraksi dengan model, fungsi view juga berperan dalam merender template HTML. Data yang diperlukan untuk tampilan HTML dimasukkan ke dalam template ini, dan hasil render template akan dikembalikan sebagai bagian dari respons.

Kemudian, Django mengirimkan respons yang dihasilkan kembali kepada user atau client. Respons ini dapat berupa halaman HTML, file JSON, atau format lainnya, tergantung pada logika yang diimplementasikan dalam fungsi view. Dengan cara ini, komponen-komponen seperti urls.py, views.py, models.py, dan berkas HTML saling berinteraksi untuk menerima, memproses, dan mengembalikan halaman web yang diminta oleh user sebagai respons atas permintaan mereka.

3.Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Virtual environment (venv) adalah alat dalam Python yang memungkinkan pengembang untuk menciptakan lingkungan terisolasi bagi proyek mereka. Di setiap virtual environment, terdapat interpreter Python dan direktori instalasi paket yang independen, sehingga memastikan bahwa dependensi proyek terisolasi dan dikelola secara terpisah dari lingkungan Python global. Hal ini membantu mencegah konflik antara proyek yang memerlukan versi yang berbeda dari paket yang sama.

Selain itu, penggunaan virtual environment juga memungkinkan portabilitas proyek yang lebih baik. Dengan menyertakan virtual environment bersama dengan kode proyek, pengembang lain dapat dengan mudah mereplikasi lingkungan proyek dan menjalankannya tanpa masalah dependensi atau konflik. Ini sangat membantu dalam berbagi dan mendistribusikan proyek.

Kontrol versi juga menjadi lebih efisien dengan virtual environment, karena pengembang dapat memasukkannya ke dalam sistem kontrol versi seperti Git. Dengan begitu, mereka dapat melacak dan mengelola dependensi proyek bersama dengan kode, memastikan bahwa semua anggota tim memiliki lingkungan yang seragam dan dapat dengan mudah mengatur proyek di mesin lokal mereka.

Tidak hanya itu, virtual environment membuat instalasi dan pengelolaan dependensi menjadi lebih mudah. Pengembang dapat dengan simpel menginstal dan mengelola dependensi proyek tanpa berdampak pada lingkungan Python global. Dengan menggunakan alat seperti pip, mereka dapat menginstal paket dalam virtual environment, yang akan terisolasi dari sistem lainnya. Hal ini mempermudah pengelolaan dependensi yang spesifik untuk proyek dan menjaga dependensi tersebut terpisah dari proyek lain.

Meskipun memungkinkan untuk membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, sangat disarankan untuk mengadopsi virtual environment karena alasan yang telah disebutkan di atas. Tanpa virtual environment, dependensi proyek akan terinstal secara global, yang dapat menyebabkan konflik dan masalah kompatibilitas dengan proyek atau paket sistem lainnya. Menggunakan virtual environment adalah langkah cerdas untuk memastikan lingkungan yang bersih dan terisolasi untuk proyek Django, yang pada gilirannya akan memudahkan pengelolaan dependensi dan menjaga stabilitas proyek secara konsisten.

4.Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

MVC (Model-View-Controller), MVT (Model-View-Template), dan MVVM (Model-View-ViewModel) adalah tiga arsitektur yang umum digunakan dalam pengembangan perangkat lunak. Mereka memiliki peran dan struktur yang berbeda dalam bagaimana aplikasi dirancang dan diorganisasi.

Dalam MVC, Model bertanggung jawab untuk logika bisnis dan mengelola state aplikasi, View menampilkan data kepada pengguna, dan Controller menghubungkan Model dan View. Controller mengelola interaksi pengguna, memproses permintaan, dan memperbarui View saat Model berubah.

Di sisi lain, MVT adalah varian yang digunakan oleh Django, kerangka kerja web Python. Model dalam MVT tetap memiliki peran yang sama dengan Model dalam MVC, yaitu mengelola logika bisnis dan state aplikasi. View dalam MVT juga mirip dengan View dalam MVC, yaitu menampilkan data dan menangani interaksi pengguna. Perbedaan utama terletak pada Template, yang merupakan komponen unik dalam MVT. Template menggabungkan logika bisnis dengan tampilan, menghasilkan tampilan akhir yang diberikan kepada pengguna.

Sementara itu, MVVM adalah arsitektur yang umum digunakan dalam pengembangan aplikasi berbasis JavaScript atau mobile. Seperti MVT dan MVC, Model dalam MVVM bertanggung jawab atas logika bisnis dan mengelola state aplikasi. View menampilkan data dan menangani interaksi pengguna, sementara ViewModel bertindak sebagai penghubung antara Model dan View. ViewModel mengelola state View dan meneruskan perintah dari View ke Model. MVVM memanfaatkan konsep pengikatan data (data binding) yang memudahkan pengujian unit dan pemisahan antara pengembangan antarmuka pengguna (UI) dan logika bisnis aplikasi.

Perbedaan utama antara ketiganya terletak dalam struktur dan fokus pengembangannya. MVC dan MVT memiliki struktur yang mirip, sedangkan MVVM memiliki pendekatan yang sedikit berbeda dengan adanya ViewModel. Pilihan antara ketiganya tergantung pada kebutuhan proyek dan jenis aplikasi yang sedang dikembangkan.
