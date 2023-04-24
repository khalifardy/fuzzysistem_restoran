def membership_function(tipe, current_value, start_value, end_value, after):
    penyebut = end_value - start_value
    if tipe == 'segitiga' or tipe == 'trapesium':
        if after:
            return (end_value-current_value)/penyebut
        else:
            return (current_value-start_value)/penyebut
    elif tipe == 'sigmoid':
        if after:
            return 1 - 2*(((end_value-current_value)/penyebut)**2)
        else:
            return 2*(((current_value-start_value)/penyebut)**2)


class Fuzifikasi:
    "Kelas Merubah nilai crisp ke Fuzzy Value"

    def __init__(self):
        self.fuzzy_value = 0

    def pelayanan(self, current_value, linguistik_parameter):

        if self.fuzzy_value > 0:
            self.reset_fuzzy_value()
        if linguistik_parameter == "tidak memuaskan":
            self.kalkulasi_tidak_memuaskan(current_value)

        elif linguistik_parameter == 'kurang memuaskan':
            self.kalkulasi_kurang_memuaskan(current_value)

        elif linguistik_parameter == "cukup memuaskan":
            self.kalkulasi_cukup_memuaskan(current_value)

        elif linguistik_parameter == "memuaskan":
            self.kalkulasi_memuaskan(current_value)

        elif linguistik_parameter == 'sangat memuaskan' and current_value > 80:
            self.kalkulasi_sangat_memuaskan(current_value)

        return self.fuzzy_value

    def makanan(self, current_value, linguistik_parameter):

        if self.fuzzy_value > 0:
            self.reset_fuzzy_value()
        if linguistik_parameter == "tidak enak":
            self.kalkulasi_tidak_enak(current_value)

        elif linguistik_parameter == "cukup enak":
            self.kalkulasi_cukup_enak(current_value)

        elif linguistik_parameter == "enak":
            self.kalkulasi_enak(current_value)

        return self.fuzzy_value

    def kalkulasi_tidak_memuaskan(self, current_value):
        """
        Menghitung fuzzy value untuk tidak memuaskan.
        """
        if int(current_value) in [i+1 for i in range(5)]:
            self.fuzzy_value = 1
        elif current_value < 20:
            self.fuzzy_value = membership_function(
                "trapesium", current_value, 5, 20, True)

    def kalkulasi_kurang_memuaskan(self, current_value):
        """
        Menghitung fuzzy value untuk kurang memuaskan.
        """
        if 20 <= current_value <= 40:
            self.fuzzy_value = 1
        elif 5 < current_value < 60:
            self.fuzzy_value = membership_function(
                "trapesium", current_value, 5, 20, False
            ) if current_value < 30 else membership_function(
                "trapesium", current_value, 40, 60, True
            )

    def kalkulasi_cukup_memuaskan(self, current_value):
        """
        Menghitung fuzzy value untuk cukup memuaskan.
        """

        if current_value == 60:
            self.fuzzy_value = 1
        elif 40 < current_value < 80:
            self.fuzzy_value = membership_function(
                "segitiga", current_value, 40, 60, False
            ) if current_value < 60 else membership_function(
                "segitiga", current_value, 60, 80, True
            )

    def kalkulasi_memuaskan(self, current_value):
        """
        Menghitung fuzzy value untuk memuaskan.
        """

        if current_value == 80:
            self.fuzzy_value = 1
        elif 60 < current_value < 90:
            self.fuzzy_value = membership_function(
                "segitiga", current_value, 60, 80, False
            ) if current_value < 80 else membership_function(
                "segitiga", current_value, 80, 90, True
            )

    def kalkulasi_sangat_memuaskan(self, current_value):
        """
        Menghitung fuzzy value untuk sangat memuaskan.
        """

        if int(current_value) >= 90:
            self.fuzzy_value = 1
        elif 80 < current_value < 90:
            self.fuzzy_value = membership_function(
                "trapesium", current_value, 80, 90, False
            )

    def kalkulasi_tidak_enak(self, current_value):
        """
        menghitung fuzzy value untuk tidak enak
        """

        if 1 <= current_value <= 2:
            self.fuzzy_value = 1
        elif 2 < current_value < 6:
            self.fuzzy_value = membership_function(
                "trapesium", current_value, 2, 6, True
            )

    def kalkulasi_cukup_enak(self, current_value):
        """
        Menghitung fuzzy value untuk cukup enak
        """

        if current_value == 6:
            self.fuzzy_value = 1
        elif 2 < current_value < 8:
            self.fuzzy_value = membership_function(
                "segitiga", current_value, 2, 6, False
            ) if current_value < 6 else membership_function(
                "segitiga", current_value, 6, 8, True
            )

    def kalkulasi_enak(self, current_value):
        """
        Menghitung fuzzy value untuk enak
        """

        if current_value >= 8:
            self.fuzzy_value = 1
        elif 6 < current_value < 8:
            self.fuzzy_value = membership_function(
                "trapesium", current_value, 6, 8, False
            )

    def reset_fuzzy_value(self):
        self.fuzzy_value = 0


class Defuzifikasi:
    def __init__(self):
        self.crisp_value = 0

    def mandani(self, data, posisi):
        penyebut = 0
        pembilang = 0

        data_ = data.loc[posisi]

        if type(data_['fuzzy_value_high']) != type(""):
            penyebut += self.total_penyebut(data_['fuzzy_value_high'], 8, 10)
            pembilang += self.total_pembilang(data_['fuzzy_value_high'], 8, 10)

        if type(data_['fuzzy_value_medium']) != type(""):
            penyebut += self.total_penyebut(data_['fuzzy_value_medium'], 4, 7)
            pembilang += self.total_pembilang(
                data_['fuzzy_value_medium'], 4, 7)

        if type(data_['fuzzy_value_low']) != type(""):
            penyebut += self.total_penyebut(data_['fuzzy_value_low'], 1, 4)
            pembilang += self.total_pembilang(data_['fuzzy_value_low'], 1, 4)

        print(pembilang)
        print(penyebut)

        hasil = pembilang/penyebut

        label = "High" if hasil >= 8 else "medium" if 6 <= hasil < 8 else "low"

        return (hasil, label)

    def sugeno(self, data, posisi):
        penyebut = 0
        pembilang = 0

        data_ = data.loc[posisi]

        if type(data_['fuzzy_value_high']) != type(""):
            penyebut += data_['fuzzy_value_high']
            pembilang += data_['fuzzy_value_high'] * 10

        if type(data_['fuzzy_value_medium']) != type(""):
            penyebut += data_['fuzzy_value_medium']
            pembilang += data_['fuzzy_value_medium'] * 6

        if type(data_['fuzzy_value_low']) != type(""):
            penyebut += data_['fuzzy_value_low']
            pembilang += data_['fuzzy_value_low'] * 3

        hasil = pembilang/penyebut

        label = "High" if hasil >= 8 else "medium" if 6 <= hasil < 8 else "low"

        return (hasil, label)

    def total_penyebut(self, fuzzy_value, start, end):
        total = fuzzy_value*(end-start)
        return total

    def total_pembilang(self, fuzzy_value, start, end):
        total = 0
        for i in range(start, end):
            total += i

        total *= fuzzy_value

        return total


def inferensi(crisp_value, data, posisi):
    hasil = ""
    temp = 0
    data_i = data.loc[posisi]
    if crisp_value == "low":
        if data_i["fuzzy_pelayanan_tidak_memuaskan"] != 0 and data_i["fuzzy_makanan_tidak_enak"] != 0:
            if data_i["fuzzy_pelayanan_tidak_memuaskan"] <= data_i["fuzzy_makanan_tidak_enak"]:
                temp = data_i["fuzzy_pelayanan_tidak_memuaskan"]
            else:
                temp = data_i["fuzzy_makanan_tidak_enak"]

            if hasil == "":
                hasil = temp
            else:
                if hasil <= temp:
                    hasil = temp

        if data_i["fuzzy_pelayanan_kurang_memuaskan"] != 0 and data_i["fuzzy_makanan_tidak_enak"] != 0:

            if data_i["fuzzy_pelayanan_kurang_memuaskan"] <= data_i["fuzzy_makanan_tidak_enak"]:
                temp = data_i["fuzzy_pelayanan_kurang_memuaskan"]
            else:
                temp = data_i["fuzzy_makanan_tidak_enak"]

            if hasil == "":
                hasil = temp
            else:
                if hasil <= temp:
                    hasil = temp

        if data_i["fuzzy_pelayanan_cukup_memuaskan"] != 0 and data_i["fuzzy_makanan_tidak_enak"] != 0:
            if data_i["fuzzy_pelayanan_cukup_memuaskan"] <= data_i["fuzzy_makanan_tidak_enak"]:
                temp = data_i["fuzzy_pelayanan_cukup_memuaskan"]
            else:
                temp = data_i["fuzzy_makanan_tidak_enak"]

            if hasil == "":
                hasil = temp
            else:
                if hasil <= temp:
                    hasil = temp

        if data_i["fuzzy_pelayanan_tidak_memuaskan"] != 0 and data_i["fuzzy_makanan_cukup_enak"] != 0:
            if data_i["fuzzy_pelayanan_tidak_memuaskan"] <= data_i["fuzzy_makanan_cukup_enak"]:
                temp = data_i["fuzzy_pelayanan_cukup_memuaskan"]
            else:
                temp = data_i["fuzzy_makanan_cukup_enak"]

            if hasil == "":
                hasil = temp
            else:
                if hasil <= temp:
                    hasil = temp

        if data_i["fuzzy_pelayanan_kurang_memuaskan"] != 0 and data_i["fuzzy_makanan_cukup_enak"] != 0:
            if data_i["fuzzy_pelayanan_kurang_memuaskan"] <= data_i["fuzzy_makanan_cukup_enak"]:
                temp = data_i["fuzzy_pelayanan_kurang_memuaskan"]
            else:
                temp = data_i["fuzzy_makanan_cukup_enak"]

            if hasil == "":
                hasil = temp
            else:
                if hasil <= temp:
                    hasil = temp

        if data_i["fuzzy_pelayanan_tidak_memuaskan"] != 0 and data_i["fuzzy_makanan_enak"] != 0:
            if data_i["fuzzy_pelayanan_tidak_memuaskan"] <= data_i["fuzzy_makanan_enak"]:
                temp = data_i["fuzzy_pelayanan_tidak_memuaskan"]
            else:
                temp = data_i["fuzzy_makanan_enak"]

            if hasil == "":
                hasil = temp
            else:
                if hasil <= temp:
                    hasil = temp
    elif crisp_value == "medium":
        if data_i["fuzzy_pelayanan_memuaskan"] != 0 and data_i["fuzzy_makanan_tidak_enak"] != 0:
            if data_i["fuzzy_pelayanan_memuaskan"] <= data_i["fuzzy_makanan_tidak_enak"]:
                temp = data_i["fuzzy_pelayanan_memuaskan"]
            else:
                temp = data_i["fuzzy_makanan_tidak_enak"]

            if hasil == "":
                hasil = temp
            else:
                if hasil <= temp:
                    hasil = temp

        if data_i["fuzzy_pelayanan_sangat_memuaskan"] != 0 and data_i["fuzzy_makanan_tidak_enak"] != 0:
            if data_i["fuzzy_pelayanan_sangat_memuaskan"] <= data_i["fuzzy_makanan_tidak_enak"]:
                temp = data_i["fuzzy_pelayanan_sangat_memuaskan"]
            else:
                temp = data_i["fuzzy_makanan_tidak_enak"]

            if hasil == "":
                hasil = temp
            else:
                if hasil <= temp:
                    hasil = temp

        if data_i["fuzzy_pelayanan_cukup_memuaskan"] != 0 and data_i["fuzzy_makanan_cukup_enak"] != 0:
            if data_i["fuzzy_pelayanan_cukup_memuaskan"] <= data_i["fuzzy_makanan_cukup_enak"]:
                temp = data_i["fuzzy_pelayanan_cukup_memuaskan"]
            else:
                temp = data_i["fuzzy_makanan_cukup_enak"]

            if hasil == "":
                hasil = temp
            else:
                if hasil <= temp:
                    hasil = temp

        if data_i["fuzzy_pelayanan_memuaskan"] != 0 and data_i["fuzzy_makanan_cukup_enak"] != 0:
            if data_i["fuzzy_pelayanan_memuaskan"] <= data_i["fuzzy_makanan_cukup_enak"]:
                temp = data_i["fuzzy_pelayanan_memuaskan"]
            else:
                temp = data_i["fuzzy_makanan_cukup_enak"]

            if hasil == "":
                hasil = temp
            else:
                if hasil <= temp:
                    hasil = temp

        if data_i["fuzzy_pelayanan_kurang_memuaskan"] != 0 and data_i["fuzzy_makanan_enak"] != 0:
            if data_i["fuzzy_pelayanan_kurang_memuaskan"] <= data_i["fuzzy_makanan_enak"]:
                temp = data_i["fuzzy_pelayanan_kurang_memuaskan"]
            else:
                temp = data_i["fuzzy_makanan_enak"]

            if hasil == "":
                hasil = temp
            else:
                if hasil <= temp:
                    hasil = temp

        if data_i["fuzzy_pelayanan_cukup_memuaskan"] != 0 and data_i["fuzzy_makanan_enak"] != 0:
            if data_i["fuzzy_pelayanan_cukup_memuaskan"] <= data_i["fuzzy_makanan_enak"]:
                temp = data_i["fuzzy_pelayanan_cukup_memuaskan"]
            else:
                temp = data_i["fuzzy_makanan_enak"]

            if hasil == "":
                hasil = temp
            else:
                if hasil <= temp:
                    hasil = temp

    elif crisp_value == "high":
        if data_i["fuzzy_pelayanan_sangat_memuaskan"] != 0 and data_i["fuzzy_makanan_cukup_enak"] != 0:
            if data_i["fuzzy_pelayanan_sangat_memuaskan"] <= data_i["fuzzy_makanan_cukup_enak"]:
                temp = data_i["fuzzy_pelayanan_sangat_memuaskan"]
            else:
                temp = data_i["fuzzy_makanan_cukup_enak"]

            if hasil == "":
                hasil = temp
            else:
                if hasil <= temp:
                    hasil = temp

        if data_i["fuzzy_pelayanan_memuaskan"] != 0 and data_i["fuzzy_makanan_enak"] != 0:
            if data_i["fuzzy_pelayanan_memuaskan"] <= data_i["fuzzy_makanan_enak"]:
                temp = data_i["fuzzy_pelayanan_memuaskan"]
            else:
                temp = data_i["fuzzy_makanan_enak"]

            if hasil == "":
                hasil = temp
            else:
                if hasil <= temp:
                    hasil = temp

        if data_i["fuzzy_pelayanan_sangat_memuaskan"] != 0 and data_i["fuzzy_makanan_enak"] != 0:
            if data_i["fuzzy_pelayanan_sangat_memuaskan"] <= data_i["fuzzy_makanan_enak"]:
                temp = data_i["fuzzy_pelayanan_sangat_memuaskan"]
            else:
                temp = data_i["fuzzy_makanan_enak"]

            if hasil == "":
                hasil = temp
            else:
                if hasil <= temp:
                    hasil = temp
    return hasil
