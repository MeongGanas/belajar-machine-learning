# Pandas berfungsi untuk memanipulasi dan membaca data.
# Pandas mengambil data dan merubahnya menjadi tabel yang bisa di baca manusia, pandas juga bisa ditafsirkan secara numerik sehingga bisa mengoperasikan banyak perhitungan

# mengimport library pandas dan menginisialisasikan menjadi pd
import pandas as pd

# df berarti dataframe (tabbel data)
df = pd.read_csv('../csv/titanic.csv')

print(df.head())
