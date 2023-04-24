# %%
import pandas as pd
# %%
data_restoran = pd.read_excel('file/restoran.xlsx')
# %%
list_skor_pelayanan = [
    i for i in data_restoran['pelayanan']
]
# %%
list_skor_lezat_makanan = [
    i for i in data_restoran['makanan']
]

# %%
unik_skor_pelayanan = list(sorted(set(list_skor_pelayanan)))
# %%
unik_skor_lezat_makanan = list(sorted(set(list_skor_lezat_makanan)))

# %%
"""
Linguistik Makanan:
1. tidak enak( 1 -5)
1,2, pasti tidak enak
3,4 diantara 
5 end
trapesium 

2. Cukup (4-8)
4 titik awal
5 diantara
6 pasti
7 diantara bagian bawah
8 end

3. Enak (7-10)
7 titik nol
8 diantara
9-10 pasti
trapesium

Linguistik pelayanan:
1. tidak memuaskan(1-20)
1-5 pasti
6-19 diantara
20 end
trapesium



2. kurang memuaskan(10-60)
10 start
11-20 diantara
30-40 pasti
50 diantara
60 end
trapesium

3. cukup memuaskan(50-80)
50 start 
60 pasti
70 diantara bawah
80 end
segitiga

4. memuaskan(70-90)
start 70
pasti 80
end 90
segitiga

5. sangat memuaskan(80-100)
start 80
90-100 pasti
trapesium
 



output rating (1-10)

low, medium, high

low
pasti (1-3)
end(5)

medium
start(3)
pasti(5-6)
end(9)

high
start(6)
pasti(9-10)



"""


# %%
