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
        if linguistik_parameter == "tidak enak":
            self.kalkulasi_tidak_enak(current_value)

        elif linguistik_parameter == "cukup enak":
            self.kalkulasi_cukup(current_value)

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
            self.fuzzy_value = self.membership_function(
                "trapesium", current_value, 5, 20, True)

    def kalkulasi_kurang_memuaskan(self, current_value):
        """
        Menghitung fuzzy value untuk kurang memuaskan.
        """
        if 30 <= current_value <= 40:
            self.fuzzy_value = 1
        elif 10 < current_value < 60:
            self.fuzzy_value = membership_function(
                "trapesium", current_value, 10, 30, False
            ) if current_value < 30 else membership_function(
                "trapesium", current_value, 40, 60, True
            )

    def kalkulasi_cukup_memuaskan(self, current_value):
        """
        Menghitung fuzzy value untuk cukup memuaskan.
        """

        if current_value == 60:
            self.fuzzy_value = 1
        elif 50 < current_value < 80:
            self.fuzzy_value = membership_function(
                "segitiga", current_value, 50, 60, False
            ) if current_value < 60 else membership_function(
                "segitiga", current_value, 60, 80, True
            )

    def kalkulasi_memuaskan(self, current_value):
        """
        Menghitung fuzzy value untuk memuaskan.
        """

        if current_value == 80:
            self.fuzzy_value = 1
        elif 70 < current_value < 90:
            self.fuzzy_value = membership_function(
                "segitiga", current_value, 70, 80, False
            ) if current_value < 90 else membership_function(
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
        elif 2 < current_value < 5:
            self.fuzzy_value = membership_function(
                "trapesium", current_value, 2, 5, True
            )

    def kalkulasi_cukup_enak(self, current_value):
        """
        Menghitung fuzzy value untuk cukup enak
        """

        if current_value == 6:
            self.fuzzy_value = 1
        elif 4 < current_value < 8:
            self.fuzzy_value = membership_function(
                "segitiga", current_value, 4, 6, False
            ) if current_value < 6 else membership_function(
                "segitiga", current_value, 6, 8, True
            )

    def kalkulasi_enak(self, current_value):
        """
        Menghitung fuzzy value untuk enak
        """

        if current_value >= 9:
            self.fuzzy_value = 1
        elif 8 < current_value < 9:
            self.fuzzy_value = membership_function(
                "trapesium", current_value, 8, 9, False
            )
