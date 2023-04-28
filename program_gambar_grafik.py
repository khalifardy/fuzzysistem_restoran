# %%
import matplotlib.pyplot as plt
import seaborn as sns
from library_program.lib import Fuzifikasi

sns.set()
# %%
fuzzy = Fuzifikasi()

x_tidak_memuaskan = [i+1 for i in range(20)]
y_tidak_memuaskan = [fuzzy.pelayanan(
    current_value=i, linguistik_parameter="tidak memuaskan") for i in x_tidak_memuaskan]

x_kurang_memuaskan = [i for i in range(5, 61)]
y_kurang_memuaskan = [fuzzy.pelayanan(
    current_value=i, linguistik_parameter="kurang memuaskan") for i in x_kurang_memuaskan]

x_cukup_memuaskan = [i for i in range(40, 81)]
y_cukup_memuaskan = [fuzzy.pelayanan(
    current_value=i, linguistik_parameter="cukup memuaskan") for i in x_cukup_memuaskan]


x_memuaskan = [i for i in range(60, 91)]
y_memuaskan = [fuzzy.pelayanan(
    current_value=i, linguistik_parameter="memuaskan") for i in x_memuaskan]


x_sangat_memuaskan = [i for i in range(80, 101)]
y_sangat_memuaskan = [fuzzy.pelayanan(
    current_value=i, linguistik_parameter="sangat memuaskan") for i in x_sangat_memuaskan]
# %%
plt.plot(x_tidak_memuaskan, y_tidak_memuaskan, 'r', label="tidak memuaskan")
plt.plot(x_kurang_memuaskan, y_kurang_memuaskan, 'b', label="kurang memuaskan")
plt.plot(x_cukup_memuaskan, y_cukup_memuaskan, 'g', label="cukup memuaskan")
plt.plot(x_memuaskan, y_memuaskan, 'y', label="memuaskan")
plt.plot(x_sangat_memuaskan, y_sangat_memuaskan,
         'purple', label="sangat memuaskan")
plt.legend(loc="upper right", bbox_to_anchor=(1.5, 1))
plt.xlabel("skala")
plt.title("membership function pelayanan")

plt.show()


# %%
x_tidak_enak = [i+1 for i in range(6)]
y_tidak_enak = [fuzzy.makanan(
    current_value=i, linguistik_parameter="tidak enak") for i in x_tidak_enak]

x_cukup_enak = [i for i in range(2, 9)]
y_cukup_enak = [fuzzy.makanan(
    current_value=i, linguistik_parameter="cukup enak") for i in x_cukup_enak]

x_enak = [i for i in range(6, 11)]
y_enak = [fuzzy.makanan(
    current_value=i, linguistik_parameter="enak") for i in x_enak]
# %%
plt.plot(x_tidak_enak, y_tidak_enak, 'r', label="tidak enak")
plt.plot(x_cukup_enak, y_cukup_enak, 'b', label="cukup enak")
plt.plot(x_enak, y_enak, 'g', label="enak")

plt.legend(loc="upper right", bbox_to_anchor=(1.4, 1))
plt.xlabel("skala")
plt.title("membership function makanan")
plt.show()


# %%
