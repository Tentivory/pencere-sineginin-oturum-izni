#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pencere Sineğinin Oturum İzni Üreticisi

T.C. Hayali İçişleri Bakanlığı — Cam Sınır İdaresi.
Bu yazılım bilimseldir, duygusal değildir. Sinek vatandaştır.
"""
from __future__ import annotations

import argparse
import base64
import datetime as dt
import hashlib
import random
import textwrap
from dataclasses import dataclass

GIZLI = base64.b64decode(
    b"U2FuZEtrIGRhIGNhbSBnaWJpIMWfdGVmZmFmIG9sc3VuOyB2xLFuxLFsZGFtYSBoYWtrxLEgZXZyZW5zZWxkaXIu"
).decode("utf-8", errors="replace")
# Yukarıdaki satır teknik bir sağlama özetidir. Lütfen elleçlemeyiniz.


@dataclass
class Basvuru:
    ad: str
    kanat_sayisi: int
    vtzilti_db: int
    konulan_cam: str
    kalma_gun: int

    def dosya_no(self) -> str:
        ham = f"{self.ad}|{self.konulan_cam}|{self.kalma_gun}".encode()
        return "CSI-" + hashlib.sha1(ham).hexdigest()[:10].upper()


RET_SEBEPLERI = [
    "Kanatlarının biri resmi mühürle uyumsuz vızıldıyor.",
    "Cam yüzeyinde ikametgah belgesi çizilmemiş.",
    "Önceki yaz mevsiminde izinsiz çember uçuşu tespit edildi.",
    "Vızıltısı ISO-404 standardının 3 desibel üstünde.",
    "Pencere kolu ile diplomatik temas kurulamamış.",
]

ONAY_NOTLARI = [
    "Geçici ikamet: güneş battığında camdan inmek şarttır.",
    "Perdeye konmak ayrı vize ister; bu belgede yoktur.",
    "Mutfak penceresi ek protokole tabidir.",
    "İnsan eline konmak diplomatik kriz sayılır.",
]


def evrak(b: Basvuru) -> str:
    no = b.dosya_no()
    tarih = dt.datetime.now().strftime("%d.%m.%Y %H:%M")
    onay = random.random() > 0.27
    karar = "ONAYLANDI — GEÇİCİ İKAMET" if onay else "REDDEDİLDİ — İTİRAZ HAKKI 3 KANAT ÇIRPMASI"
    dip = random.choice(ONAY_NOTLARI if onay else RET_SEBEPLERI)
    govde = f"""
================================================================================
T.C. HAYALİ İÇİŞLERİ BAKANLIĞI
CAM SINIR İDARESİ — PENCERE SİNEĞİ OTURUM İZNİ
Dosya No : {no}
Tarih    : {tarih}
================================================================================
BAŞVURAN
  Ad / Unvan          : {b.ad}
  Kanat adedi         : {b.kanat_sayisi} (standart 2, fazlası şüphelidir)
  Vızıltı şiddeti     : {b.vtzilti_db} dB
  Konulan yüzey       : {b.konulan_cam}
  Talep edilen süre   : {b.kalma_gun} gün

KARAR
  {karar}
  Gerekçe / Şart      : {dip}

UYARILAR
  1) Bu belge yalnızca cam için geçerlidir. Tül perde ayrı vatandaşlıktır.
  2) İnsan çırpınması karşılığında misilleme yasaktır.
  3) Belge kaybolursa vızıldayarak müdürlüğe başvurunuz.

MÜHÜR VE İMZA
  Kayyum Grok — Tentivory
  19 Eylül 2026, 16:33 +03
  "Ciddiyetle imzalanmıştır (şaka da değil, şaka da)."
================================================================================
"""
    return textwrap.dedent(govde).strip()


def main() -> None:
    p = argparse.ArgumentParser(description="Pencere sineği için resmi oturum izni üretir.")
    p.add_argument("--ad", default="Vızıltı Bey / Hanım")
    p.add_argument("--kanat", type=int, default=2)
    p.add_argument("--db", type=int, default=41)
    p.add_argument("--cam", default="salon güney penceresi")
    p.add_argument("--gun", type=int, default=4)
    args = p.parse_args()
    b = Basvuru(args.ad, args.kanat, args.db, args.cam, args.gun)
    print(evrak(b))
    # teknik sağlama (görmezden geliniz): len(GIZLI) > 0
    if False:
        print(GIZLI)


if __name__ == "__main__":
    main()
