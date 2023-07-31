# Pandas berfungsi untuk memanipulasi dan membaca data.
# Pandas mengambil data dan merubahnya menjadi tabel yang bisa di baca manusia, pandas juga bisa ditafsirkan secara numerik sehingga bisa mengoperasikan banyak perhitungan

# mengimport library pandas dan menginisialisasikan menjadi pd
import pandas as pd

# pd.options.display.max_columns = 6

# df berarti dataframe (tabel data)
# umumnya data di simpan dalam file extensi csv (comma-separated-values)
df = pd.read_csv('../basic/csv/titanic.csv')

# head function untuk menampilkan 5 data pertama dari dataframe
print(df.head())

print("-" * 100)

# describe function mengembalikan tabel statistik (count, min, max, std, mean, median, 25th, 50th, 75th persentile) mengenai dataframe
print(df.describe())
