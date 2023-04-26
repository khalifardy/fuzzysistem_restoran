from fastapi import FastAPI, Response, File
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from library_program.lib import Fuzifikasi, Defuzifikasi, inferensi

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
    "https://restoranadvice.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/suggest_restoran")
async def download_excel(file: bytes = File(...)):

    data_raw = pd.read_excel(file)
    copy_data = data_raw.copy()
    fuzzy = Fuzifikasi()
    defuzy = Defuzifikasi()

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

    high = []
    medium = []
    low = []

    for i in range(len(copy_data)):
        inf_high = inferensi("high", copy_data, i)
        inf_medium = inferensi("medium", copy_data, i)
        inf_low = inferensi("low", copy_data, i)

        high.append(inf_high)
        medium.append(inf_medium)
        low.append(inf_low)

    copy_data = copy_data.assign(
        fuzzy_value_high=high,
        fuzzy_value_medium=medium,
        fuzzy_value_low=low
    )

    mandani_value = []
    mandani_label = []
    sugeno_value = []
    sugeno_label = []

    for i in range(len(copy_data)):
        mandani = defuzy.mandani(copy_data, i)
        sugeno = defuzy.sugeno(copy_data, i)

        mandani_value.append(mandani[0])
        mandani_label.append(mandani[1])
        sugeno_value.append(sugeno[0])
        sugeno_label.append(sugeno[1])

    copy_data = copy_data.assign(
        mandani_value=mandani_value,
        sugeno_value=sugeno_value,
        mandani_label=mandani_label,
        sugeno_label=sugeno_label
    )

    copy_data = copy_data.sort_values('sugeno_value', ascending=False)
    copy_data = copy_data[:10]["id"]

    excel_files = "peringkat.xlsx"
    copy_data.to_excel(excel_files, index=False)

    return FileResponse(excel_files,
                        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                        filename="peringkat.xlsx")
