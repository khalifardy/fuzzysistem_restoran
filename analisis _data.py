# %%
import pandas as pd
from library_program.lib import Fuzifikasi
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
# %%
data_restoran = pd.read_excel('file/restoran.xlsx')
copy_data = data_restoran.copy()
fuzzy = Fuzifikasi()
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
tidak_memuaskan = []
kurang_memuaskan = []
cukup_memuaskan = []
memuaskan = []
sangat_memuaskan = []

tidak_enak = []
cukup = []
enak = []
for i in range(len(copy_data)):
    pelayanan_tidak_memuaskan = fuzzy.pelayanan(
        linguistik_parameter="tidak memuaskan",
        current_value=copy_data.loc[i]['pelayanan'])
    pelayanan_kurang_memuaskan = fuzzy.pelayanan(
        linguistik_parameter="kurang memuaskan",
        current_value=copy_data.loc[i]['pelayanan'])
    pelayanan_cukup_memuaskan = fuzzy.pelayanan(
        linguistik_parameter="cukup memuaskan",
        current_value=copy_data.loc[i]['pelayanan'])
    pelayanan_memuaskan = fuzzy.pelayanan(
        linguistik_parameter="memuaskan",
        current_value=copy_data.loc[i]['pelayanan'])
    pelayanan_sangat_memuaskan = fuzzy.pelayanan(
        linguistik_parameter="sangat memuaskan",
        current_value=copy_data.loc[i]['pelayanan'])

    tidak_memuaskan.append(pelayanan_tidak_memuaskan)
    kurang_memuaskan.append(pelayanan_kurang_memuaskan)
    cukup_memuaskan.append(pelayanan_cukup_memuaskan)
    memuaskan.append(pelayanan_memuaskan)
    sangat_memuaskan.append(pelayanan_sangat_memuaskan)

    makanan_tidak_enak = fuzzy.makanan(
        linguistik_parameter="tidak enak",
        current_value=copy_data.loc[i]['makanan'])
    makanan_cukup_enak = fuzzy.makanan(
        linguistik_parameter="cukup enak",
        current_value=copy_data.loc[i]['makanan'])
    makanan_enak = fuzzy.makanan(linguistik_parameter="enak",
                                 current_value=copy_data.loc[i]['makanan'])

    tidak_enak.append(makanan_tidak_enak)
    cukup.append(makanan_cukup_enak)
    enak.append(makanan_enak)

copy_data = copy_data.assign(fuzzy_pelayanan_tidak_memuaskan=tidak_memuaskan,
                             fuzzy_pelayanan_kurang_memuaskan=kurang_memuaskan,
                             fuzzy_pelayanan_cukup_memuaskan=cukup_memuaskan,
                             fuzzy_pelayanan_memuaskan=memuaskan,
                             fuzzy_pelayanan_sangat_memuaskan=sangat_memuaskan,
                             fuzzy_makanan_tidak_enak=tidak_enak,
                             fuzzy_makanan_cukup_enak=cukup,
                             fuzzy_makanan_enak=enak)


# %%
copy_data.to_excel("data.xlsx", index=False)

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
fig, ax = plt.subplots(nrows=3, ncols=2, figsize=(10, 5))
ax[0][0].scatter(copy_data["pelayanan"],
                 copy_data["fuzzy_pelayanan_tidak_memuaskan"])
ax[0][0].set_xlabel("crisp value")
ax[0][0].set_ylabel("fuzzy value")
ax[0][0].set_title("pelayanan tidak memuaskan")
ax[0][1].scatter(copy_data["pelayanan"],
                 copy_data["fuzzy_pelayanan_kurang_memuaskan"], c="orange")
ax[0][1].set_xlabel("crisp value")
ax[0][1].set_ylabel("fuzzy value")
ax[0][1].set_title("pelayanan kurang memuaskan")
ax[1][0].scatter(copy_data["pelayanan"],
                 copy_data["fuzzy_pelayanan_cukup_memuaskan"], c="green")
ax[1][0].set_xlabel("crisp value")
ax[1][0].set_ylabel("fuzzy value")
ax[1][0].set_title("pelayanan cukup memuaskan")
ax[1][1].scatter(copy_data["pelayanan"],
                 copy_data["fuzzy_pelayanan_memuaskan"], c="red")
ax[1][1].set_xlabel("crisp value")
ax[1][1].set_ylabel("fuzzy value")
ax[1][1].set_title("pelayanan memuaskan")
ax[2][0].scatter(copy_data["pelayanan"],
                 copy_data["fuzzy_pelayanan_sangat_memuaskan"], c="purple")
ax[2][0].set_xlabel("crisp value")
ax[2][0].set_ylabel("fuzzy value")
ax[2][0].set_title("pelayanan sangat memuaskan")
ax[-1][-1].remove()

fig.subplots_adjust(hspace=1.2, wspace=0.2)
# %%
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(10, 5))
ax[0].scatter(copy_data["makanan"],
              copy_data["fuzzy_makanan_tidak_enak"])
ax[0].set_xlabel("crisp value")
ax[0].set_ylabel("fuzzy value")
ax[0].set_title("makanan tidak enak")
ax[1].scatter(copy_data["makanan"],
              copy_data["fuzzy_makanan_cukup_enak"], c="orange")
ax[1].set_xlabel("crisp value")
ax[1].set_ylabel("fuzzy value")
ax[1].set_title("makanan cukup enak")
ax[2].scatter(copy_data["makanan"],
              copy_data["fuzzy_makanan_enak"], c="green")
ax[2].set_xlabel("crisp value")
ax[2].set_ylabel("fuzzy value")
ax[2].set_title("makanan enak")

fig.subplots_adjust(hspace=1.2, wspace=0.2)
fig.tight_layout()
# %%
