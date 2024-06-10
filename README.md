# Dashboard Anti Drop Out Jaya Maju
simple python ML with Gradient Boosting ML to help Jaya Institute identify factors that make their student dropouts. with added prediction of which student going to Dropouts

# Proyek Akhir : Menyelesaikan Permasalahan Dropouts di Jaya Institute
## Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

apabila trend ini terus terjadi di Jaya Institute, bukan hanya mencoreng nama sebagai institute pendidikan karena banyaknya siswa yang Dropout, namun Jaya Institute tidak akan dapat kepercayaan lagi oleh wali siswa untuk menitipkan anaknya belajar disana. jika trend ini tidak dihentikan maka kedepannya business continuity jaya institute akan terganggu, bukan tidak mungkin pada suatu hari Jaya Institute akan tinggal nama.
project ini adalah salah satu dari upaya counter measure dari Jaya Institute untuk menanggulangi permasalahan yang terjadi.

### Permasalahan Bisnis

1. Dropout yang tinggi pada siswa di Jaya Institute
2. banyak faktor attrition yang terlibat, namun tidak mengetahui faktor utama.
3. kesulitan menentukan faktor utama untuk menurunkan penyebab utama dari keinginan siswa untuk dropout.
4. tidak ada notice/antisipasi untuk siswa yang berpotensi dropout, sehingga membuat institusi tidak dapat melakukan konseling dan bimbingan khusus sebelum terjadi.

### Cakupan Proyek

lingkup project : 
1. Pembuatan model machine learning prediction untuk memprediksi apakah siswa yang masih aktif akan melakukan dropout
2. Pembuatan Dashboard sederhana untuk visualisasi data memantau kondisi siswa, terutama untuk mencegah dropout dengan prediksi dari machine learning.
3. Pembuatan website dashboard sederhana dari streamlit, yang berfungsi memberikan parameter-parameter yang diketahui dan memprediksi kemungkinan dropout dari siswa tersebut.

batasan project : 
1. menggunakan analisa dan pengolahan data bersumber dari data yang diberikan.
2. pemodelan penggunakan bahasa pemrograman python
3. database menggunakan supabase
4. dashboard menggunakan metabase(versi local)
5. streamlit

tujuan project : 
1. pemantauan kondisi siswa dan kategorinya pada Jaya Institute secara realtime melalui dashboard dan visualisasi data.
2. tabel prediksi dropout untuk siswa di Jaya Institute. dapat dimanfaatkan oleh manajemen institute untuk mengetahui siapa saja siswa yang berpotensi untuk dropout dan melakukan sikap yang diperlukan.

### Persiapan

Setup environment libary:
joblib==1.2.0
matplotlib==3.7.2
pandas==2.2.2
scikit_learn==1.3.0
seaborn==0.13.2
SQLAlchemy==2.0.21


## Setup Environment - Anaconda
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

#### Setup Environment - Shell/Terminal
```
mkdir dashboard_jayainst
cd dashboard_jayainst
pipenv install
pipenv shell
pip install -r requirements.txt
```



## Business Dashboard

Dashboard dibuat dengan tools Docker dan Metabase dengan akses database dari supabase.
Item pada Dashboard adalah :
1. Jumlah Siswa all time
2. Jumlah Siswa Aktif/Enrolled.
3. Jumlah Siswa Lulus/Graduated
4. Jumlah Siswa Dropout
5. Pie Chart perbandingan antar Status Siswa
6. top 10 faktor utama yang menyebabkan siswa dropout.
7. tabel prediksi siswa yang akan dropout.
8. tabel detail informasi karyawan. dengan fungsi filter, sehingga jika diprint dapat disesuaikan tampilannya.

Penggunaan utama dari Dashboard ini adalah instituti dapat memantau kondisi helicopter view terkait siswanya, terutama dapat konteks Status dari Dropout sampai dengan Graduated.
institusi juga dapat memantau faktor utama dari Siswa dropout dan melakukan penyesuaian yang diperlukan.

## Conclusion

Pembuatan Dashboard ini harapannya dapat meningkatkan ketangkasan institusi dalam menanggulangi problem dropout. dengan dashboard ini institusi dapat memantau secara langsung siapa aja siswa yang dapat berpotensi untuk dropout.
selain itu perusahaan juga dapat memantau faktor utama yang menyebabkan siswa ingin dropout, dan melakukan adjustment yang sesuai.

melalui model machine learning, dapat diketahui berikut ada top 10 faktor utama siswa memutuskan dropout.


Pembuatan Dashboard khusus harapannya dapat menanggulangi issue attrition pada perusahaan. perusahaan dapat dengan real-time memantau faktor-faktor utama yang menyebabkan karyawan attrite.
dalam dashboard juga ada fitur prediksi bagi pegawai yang akan attrite. 
![download](https://github.com/hudasf/Dashboard-Jaya-Institute/assets/17269323/7ea7bbc6-5483-44bd-8b3d-c76ae939c944)
yang paling pertama adalah Curricular_units_2nd_sem_approved. yaitu faktor dari credit yang di approve oleh institusi, artinya adalah credit yang berhasil diselesaikan oleh siswa.
data mengatakan, semakin sedikit credit yang berhasil diselesaikan siswa pada semester 2, mengakibatkan siswa memutuskan untuk melakukan dropout, hal ini juga didukung oleh faktor nomor 4 yaitu : Curricular_units_2nd_sem_grade, yang mana jika siswa sedikit menyelesaikan credit dan mengakibatkan grade nya pada semester 2 rendah akan meningkatkan keinginan untuk dropout.
faktor terbesar lainnya adalah Tuition_fees_up_to_date, yaitu faktor pembiayaan. ketika seorang siswa tidak dapat menyelesaikan semester 2 dengan baik, namun biaya yang dikeluarkan tetap full akan memberatkan siswa dalam melanjutkan pendidikannya, dan besar kemungkinan siswa akan memutuskan untuk dropout.

maka dari itu institusi perlu membuat kebijakan atau strategi baru untuk menanggulangi hal tsb.

### Rekomendasi Action Items

Beberapa rekomendasi untuk menekan angka dropout pada institusi
1. buat kebijakan keringan skema untuk credits yang perlu pengulangan karena tidak lulus.
2. berikan bimbingan khusus pada mid term untuk siswa yang terprediksi akan mendapatkan hasil kurang baik disemester 2.
3. lakukan kebijakan semester pendek untuk memperbaiki nilai siswa, sehingga siswa melihat ada harapan walaupun grade mereka tidak bagus di semester 2.
4. pada dashboard ada prediksi untuk siswa yang berpotensi dropout, segera lakukan konseling dan bimbingan untuk siswa tersebut sebelum dia memutuskan dropout.
5. pada dashboard streamlit ada juga rekayasa parameter siswa untuk memprediksi apakah siswa tersebut akan dropout. hal ini dapat digunakan tim institusi untuk memprediksi segera walapun hasil dari siswa belum muncul. sehingga institusi bisa menentukan langkah strategis sebelum masalah muncul. contohnya seperti melakukan review singkat materi kepada siswa sebelum ujian dimulai.
rjalin, dan menjamin business sustainability dari sisi talent dan karyawan.

USERNAME : vnhyde@gmail.com  
PASSWORD : metabase123

