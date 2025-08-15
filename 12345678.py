# # 1-masala
# def kabisa_yilmi(yil):
#     if (yil % 4 == 0 and yil % 100 != 0) or (yil % 400 == 0):
#         return f"{yil} — kabisa yil."
#     else:
#         return f"{yil} — kabisa yil emas."
#
# print(kabisa_yilmi(2025))
#
# # 2-masala
# def energiya_tavsiyasi(jihozlar_soni, vaqt_soat):
#     if jihozlar_soni < 5 and vaqt_soat < 8:
#         return " Tejamkor"
#     elif jihozlar_soni < 5 and vaqt_soat >= 8:
#         return "️ O'rtacha iste'mol"
#     elif jihozlar_soni >= 5 and vaqt_soat < 8:
#         return " Ko'p iste'mol"
#     elif jihozlar_soni >= 5 and vaqt_soat >= 8:
#         return " Haddan tashqari iste'mol"
#
# # Misollar:
# print(energiya_tavsiyasi(3, 6))   #  Tejamkor
# print(energiya_tavsiyasi(2, 10))  #  O'rtacha iste'mol
# print(energiya_tavsiyasi(6, 5))   #  Ko'p iste'mol
# print(energiya_tavsiyasi(7, 12))  #  Haddan tashqari iste'mol
# # 3-masala
# def qahva_harorati_holati(harorat):
#     if harorat == 60:
#         return "Ogoh bo‘ling! Juda issiq!"
#     elif 30 <= harorat < 60:
#         return "Ideal!"
#     elif harorat < 30:
#         return "Sovib qolgan!"
#     else:
#         return "Harorat diapazonidan tashqarida!"
#
#
# print(qahva_harorati_holati(60))  # Ogoh bo‘ling! Juda issiq!
# print(qahva_harorati_holati(45))  # Ideal!
# print(qahva_harorati_holati(25))  # Sovib qolgan!
# print(qahva_harorati_holati(65))  # Harorat diapazonidan tashqarida!
#
# # 4-masala
# def telefon_zaryadi_ogohlantir(zaryad_foiz):
#     if zaryad_foiz < 10:
#         return "Zaryadlash zarur!"
#     elif 10 <= zaryad_foiz < 50:
#         return "Yana biroz ishlatish mumkin."
#     elif zaryad_foiz == 85:
#         return "Zaryad yetarli."
#     else:
#         return "Zaryad holati normal."
#
#
# print(telefon_zaryadi_ogohlantir(5))   # Zaryadlash zarur!
# print(telefon_zaryadi_ogohlantir(30))  # Yana biroz ishlatish mumkin.
# print(telefon_zaryadi_ogohlantir(50))  # Zaryad yetarli.
# print(telefon_zaryadi_ogohlantir(75))  # Zaryad holati normal.
#
# # 5-masala
# def operatorni_aniqlash(raqam):
#     kod = raqam[:2]
#
#     if kod in ['90', '91']:
#         return "Beeline"
#     elif kod in ['93', '94']:
#         return "Ucell"
#     elif kod == '97':
#         return "Mobiuz"
#     else:
#         return "Noma’lum operator"
#
#
# # Misollar:
# print(operatorni_aniqlash("901234567"))  # Beeline
# print(operatorni_aniqlash("931234567"))  # Ucell
# print(operatorni_aniqlash("971234567"))  # Mobiuz
# print(operatorni_aniqlash("881234567"))  # Noma’lum operator
#
# # 6-masala
# def email_togri_mi(email):
#     if '@' in email:
#         return "Email to‘g‘ri."
#     else:
#         return "Email noto‘g‘ri: @ belgisi yo‘q."
#
# # Misollar
# print(email_togri_mi("user@example.com"))  # Email to‘g‘ri.
# print(email_togri_mi("userexample.com"))   # Email noto‘g‘ri: @ belgisi yo‘q.
#
# # 7-masala
# def baho_fikri(baho):
#     if baho < 56:
#         return "Qoniqarsiz"
#     elif 56 <= baho <= 70:
#         return "Qoniqarli"
#     elif 71 <= baho < 85:
#         return "Yaxshi"
#     elif baho == 85:
#         return "A’lo"
#     else:
#         return "Baho diapazonidan tashqarida"
#
# # Misollar
# print(baho_fikri(50))  # Qoniqarsiz
# print(baho_fikri(60))  # Qoniqarli
# print(baho_fikri(80))  # Yaxshi
# print(baho_fikri(85))  # A’lo
# print(baho_fikri(90))  # Baho diapazonidan tashqarida
#
# # 8-masala
# def kino_chiptasi_narxi(yosh):
#     if yosh < 7:
#         return "Bepul"
#     elif 7 <= yosh <= 18:
#         return "5000 so‘m"
#     elif 19 <= yosh < 59:
#         return "10000 so‘m"
#     elif yosh == 59:
#         return "7000 so‘m"
#     else:
#         return "Yosh diapazonidan tashqarida"
#
# # Misollar
# print(kino_chiptasi_narxi(5))   # Bepul
# print(kino_chiptasi_narxi(15))  # 5000 so‘m
# print(kino_chiptasi_narxi(30))  # 10000 so‘m
# print(kino_chiptasi_narxi(59))  # 7000 so‘m
# print(kino_chiptasi_narxi(60))  # Yosh diapazonidan tashqarida
#
# # 9-masala
# def oxirida_bosh_joy_bormi(satr):
#     if satr.endswith(' '):
#         return True
#     else:
#         return False
#
# # Misollar
# print(oxirida_bosh_joy_bormi("Salom "))  # True
# print(oxirida_bosh_joy_bormi("Salom"))   # False
# print(oxirida_bosh_joy_bormi(" "))       # True
# print(oxirida_bosh_joy_bormi(""))        # False
#
# # 10-masala
# def karta_raqami_togri_mi(raqam):
#     if raqam.isdigit() and len(raqam) == 16:
#         return True
#     else:
#         return False
#
# # Misollar
# print(karta_raqami_togri_mi("1234567890123456"))  # True
# print(karta_raqami_togri_mi("12345678901234"))    # False (uzunligi kam)
# print(karta_raqami_togri_mi("1234abcd90123456"))  # False (raqam emas belgilar bor)
#
# # 11-masala
# def chegirma_hisobla(narx):
#     if narx < 50000:
#         chegirma = 0
#     elif 50000 <= narx < 100000:
#         chegirma = narx * 0.05
#     elif 100000 <= narx < 200000:
#         chegirma = narx * 0.10
#     else:  # narx ≥ 200000
#         chegirma = narx * 0.15
#
#     return f"Chegirma: {int(chegirma)} so‘m"
#
#
# # Misollar
# print(chegirma_hisobla(40000))  # Chegirma: 0 so‘m
# print(chegirma_hisobla(75000))  # Chegirma: 3750 so‘m
# print(chegirma_hisobla(150000))  # Chegirma: 15000 so‘m
# print(chegirma_hisobla(250000))  # Chegirma: 37500 so‘m
#
# # 12-masala
# def yolkira_hisobla(km):
#     if km <= 5:
#         return 7000
#     elif 6 <= km <= 15:
#         ortiqcha_km = km - 5
#         return 7000 + ortiqcha_km * 1000
#     else:  # km > 15
#         ortiqcha_10_km = 10  # 6–15 km oralig'i
#         undan_ortiq_km = km - 15
#         return 7000 + ortiqcha_10_km * 1000 + undan_ortiq_km * 2000
#
# # Misollar
# print(yolkira_hisobla(3))   # 7000
# print(yolkira_hisobla(10))  # 7000 + 5*1000 = 12000
# print(yolkira_hisobla(16))  # 7000 + 10000 + 1*2000 = 19000
# print(yolkira_hisobla(20))  # 7000 + 10000 + 5*2000 = 27000
#
# # 13-masala
# def aqliy_test_bahosi(togri, notogri):
#     jami_javob = togri + notogri
#     if jami_javob == 0:
#         return "Baholanmadi"
#     else:
#         ball = togri * 2 - notogri * 1
#         return f"Umumiy ball: {ball}"
#
# # Misollar
# print(aqliy_test_bahosi(50, 5))   # Umumiy ball: 15
# print(aqliy_test_bahosi(85, 0))    # Baholandi
# print(aqliy_test_bahosi(3, 2))    # Umumiy ball: 4
# print(aqliy_test_bahosi(95, 4))    # Umumiy ball: 99
#
# # 14-masala
# def vaqt_holatini_aniqlash(soat, minut):
#     vaqt = soat * 60 + minut  # minutlarga aylantiramiz
#
#     if 9 * 60 <= vaqt <= 18 * 60:
#         return "Ish vaqti"
#     elif 18 * 60 < vaqt <= 23 * 60 + 59:
#         return "Dam olish vaqti"
#     else:
#         return "Uyqu vaqti"
#
# # Misollar
# print(vaqt_holatini_aniqlash(8, 00))  # Ish vaqti
# print(vaqt_holatini_aniqlash(20, 15))  # Dam olish vaqti
# print(vaqt_holatini_aniqlash(7, 45))   # Uyqu vaqti
# print(vaqt_holatini_aniqlash(18, 0))   # Ish vaqti
# print(vaqt_holatini_aniqlash(0, 0))    # Uyqu vaqti
#
# # 15-masala
# def rezyume_bahola(tajriba_yil, loyiha_soni):
#     if tajriba_yil < 3:
#         return "Boshlovchi"
#     elif 3 <= tajriba_yil < 5:
#         return "O‘rta daraja"
#     elif tajriba_yil >= 5 and loyiha_soni >= 1:
#         return "Tajribalilar"
#     else:
#         return "Tajriba yetarli emas"
# print(rezyume_bahola(2, 0))   # Boshlovchi
# print(rezyume_bahola(4, 0))   # O‘rta daraja
# print(rezyume_bahola(5, 2))   # Tajribalilar
# print(rezyume_bahola(6, 0))   # Tajriba yetarli emas
#
# # 16-masala
# def sogliq_bahosi(harorat):
#     if harorat < 36:
#         return "Past harorat"
#     elif 36 <= harorat <= 37:
#         return "Normal"
#     elif 37 < harorat < 38:
#         return "Yengil isitma"
#     elif harorat == 38:
#         return "Yuqumli kasallik ehtimoli bor"
#     else:
#         return "Og'ir isitma yoki boshqa holat"
# print(sogliq_bahosi(35.5))  # Past harorat
# print(sogliq_bahosi(36.7))  # Normal
# print(sogliq_bahosi(37.5))  # Yengil isitma
# print(sogliq_bahosi(38.0))  # Yuqumli kasallik ehtimoli bor
# print(sogliq_bahosi(39.2))  # Og'ir isitma yoki boshqa holat
#
#  # 17-masala
# def buyurtma_tekshir(buyurtmalar):
#     buyurtmalar = [taom.lower() for taom in buyurtmalar]  # kichik harflarga o'tkazamiz
#
#     if "lavash" in buyurtmalar and "cola" in buyurtmalar:
#         return "Combo: chegirma!"
#     elif "lavash" in buyurtmalar or "cola" in buyurtmalar:
#         return "Yaxshi tanlov!"
#     else:
#         return "Oddiy buyurtma."
# print(buyurtma_tekshir(["lavash", "cola"]))       # Combo: chegirma!
# print(buyurtma_tekshir(["Lavash"]))               # Yaxshi tanlov!
# print(buyurtma_tekshir(["cola"]))                 # Yaxshi tanlov!
# print(buyurtma_tekshir(["pizza", "choy"]))        # Oddiy buyurtma.
#
# # 18-masala
# def karta_turi_aniqlash(raqam):
#     if raqam.startswith("8600"):
#         return "UzCard"
#     elif raqam.startswith("9860"):
#         return "Humo"
#     elif raqam.startswith("4000"):
#         return "Visa"
#     else:
#         return "Noma’lum karta"
# print(karta_turi_aniqlash("8600123456789012"))  # UzCard
# print(karta_turi_aniqlash("9860123412341234"))  # Humo
# print(karta_turi_aniqlash("4000123456789012"))  # Visa
# print(karta_turi_aniqlash("1234567890123456"))  # Noma’lum karta
#
# # 19-masala
# def maqom_aniqlash(yosh):
#     if yosh < 6:
#         return "Go‘dak"
#     elif 6 <= yosh <= 12:
#         return "Bola"
#     elif 13 <= yosh <= 17:
#         return "O‘smir"
#     elif 18 <= yosh <= 25:
#         return "Yosh"
#     elif 26 <= yosh <= 59:
#         return "Katta yoshli"
#     elif yosh >= 60:
#         return "Qariya"
#     else:
#         return "Noto‘g‘ri yosh"
#
# # Misollar
# print(maqom_aniqlash(4))    # Go‘dak
# print(maqom_aniqlash(10))   # Bola
# print(maqom_aniqlash(15))   # O‘smir
# print(maqom_aniqlash(22))   # Yosh
# print(maqom_aniqlash(45))   # Katta yoshli
# print(maqom_aniqlash(70))   # Qariya
#
#
# # 20-masala
# def depozit_foizi(muddat_oy):
#     if muddat_oy == 3:
#         return "5%"
#     elif muddat_oy == 6:
#         return "10%"
#     elif muddat_oy == 12:
#         return "20%"
#     else:
#         return "Noto‘g‘ri tanlov"
#
# # Misollar
# print(depozit_foizi(3))   # 5%
# print(depozit_foizi(6))   # 10%
# print(depozit_foizi(12))  # 20%
# print(depozit_foizi(9))   # Noto‘g‘ri tanlov
#
# # 21-masala
# def yetkazib_berish_narxi(ogirlik):
#     if ogirlik < 1:
#         return 5000
#     elif 1 <= ogirlik < 3:
#         return 8000
#     elif 3 <= ogirlik < 5:
#         return 12000
#     else:  # 5 kg va undan katta
#         return 20000
#
# # Misollar
# print(yetkazib_berish_narxi(0.5))  # 5000
# print(yetkazib_berish_narxi(2))    # 8000
# print(yetkazib_berish_narxi(4))    # 12000
# print(yetkazib_berish_narxi(5))    # 20000
#
# # 22-masala
# def yetkazib_berish_narxi(ogirlik):
#     if ogirlik < 1:
#         return 5000
#     elif 1 <= ogirlik <= 3:
#         return 8000
#     elif 3 < ogirlik <= 5:
#         return 12000
#     elif ogirlik > 5:
#         return 20000
#     else:
#         return "Noto‘g‘ri og‘irlik"
#
# # Misollar
# print(yetkazib_berish_narxi(0.5))  # 5000
# print(yetkazib_berish_narxi(1))    # 8000
# print(yetkazib_berish_narxi(3))    # 8000
# print(yetkazib_berish_narxi(4))    # 12000
# print(yetkazib_berish_narxi(5))    # 12000
# print(yetkazib_berish_narxi(6))    # 20000
#
# # 23-masala
# # # Baholar ro'yxatini qabul qilish
# # baholar = input("Baholarni kiriting (masalan: 5 5 4 5): ").split()
# # baholar = list(map(int, baholar))
# #
# # # Baholarni sanaymiz
# # beshlik_soni = baholar.count(5)
# # tortlik_soni = baholar.count(4)
# #
# # # Stipendiyani aniqlaymiz
# # if beshlik_soni == len(baholar):
# #     print("1 000 000 so'm")
# # elif tortlik_soni == 1:
# #     print("800 000 so'm")
# # elif tortlik_soni == 2:
# #     print("600 000 so'm")
# # else:
# #     print("Stipendiya yo'q")
#
# # 24-masala
# # Telefon raqamini kiritish
# raqam = input("Telefon raqamini kiriting (masalan: +998901234567): ")
#
# # Raqamdagi kodni ajratib olish
# if raqam.startswith("+998") and len(raqam) >= 6:
#     kod = raqam[4:6]
# else:
#     print("Noto'g'ri raqam formati!")
#     exit()
#
# # Operatorni aniqlash
# if kod in ['90', '91']:
#     print("Beeline")
# elif kod in ['93', '94']:
#     print("Ucell")
# elif kod in ['88', '97']:
#     print("MobiUz")
# elif kod in ['77', '95', '99']:
#     print("Uzmobile")
# elif kod == '33':
#     print("Humans")
# elif kod == '98':
#     print("Perfectum mobile")
# else:
#     print("Noma'lum operator")
#
# # 25-masala
# # Pitsa narxlari
# pitsa_narxlari = {
#     "kichik": 30000,
#     "o‘rta": 45000,
#     "katta": 60000
# }
#
# # Foydalanuvchidan ma'lumotlarni olish
# turi = input("Pitsa turi (kichik / o‘rta / katta): ").lower()
# pishloq = input("Qo‘shimcha pishloq qo‘shilsinmi? (ha / yo‘q): ").lower()
# ichimlik = input("Ichimlik qo‘shilsinmi? (ha / yo‘q): ").lower()
#
# # Asosiy narxni olish
# narx = pitsa_narxlari.get(turi, 0)
#
# # Qo‘shimchalarni qo‘shish
# if pishloq == "ha":
#     narx += 5000
# if ichimlik == "ha":
#     narx += 10000
#
# # Natijani chiqarish
# if narx == 0:
#     print("Noto‘g‘ri pitsa turi kiritildi!")
# else:
#     print(f"Jami narx: {narx} so‘m")
#
# # 26-masala
# # Mahsulot narxini kiritish
# narx = float(input("Mahsulot narxini kiriting (so‘m): "))
#
# # To‘lov turini kiritish
# tolov_turi = input("To‘lov turi (naqd / plastik / onlayn): ").lower()
#
# # Chegirmani hisoblash
# if tolov_turi == "naqd":
#     chegirma = 0
# elif tolov_turi == "plastik":
#     chegirma = 0.05 * narx
# elif tolov_turi == "onlayn":
#     chegirma = 0.10 * narx
# else:
#     print("Noto‘g‘ri to‘lov turi kiritildi!")
#     exit()
#
# # Yakuniy summa
# yakuniy_narx = narx - chegirma
#
# # Natijani chiqarish
# print(f"Chegirma: {int(chegirma)} so‘m")
# print(f"To‘lanadigan summa: {int(yakuniy_narx)} so‘m")
#
# # 27-masala
# # Foydalanuvchidan ma'lumotlarni olish
# sistolik = int(input("Sistolik bosimni kiriting (masalan, 120): "))
# diastolik = int(input("Diastolik bosimni kiriting (masalan, 80): "))
# yurak_urishi = int(input("Yurak urishini kiriting (urinish/minut): "))
#
# # Belgilar
# qon_bosimi_normal = 90 <= sistolik <= 120 and 60 <= diastolik <= 80
# yurak_urishi_normal = 60 <= yurak_urishi <= 100
#
# # Tahlil
# if not qon_bosimi_normal:
#     print("Qon bosimi muammosi")
# elif not yurak_urishi_normal:
#     print("Tachikardiya")
# else:
#     print("Sog‘lom")
#
# # 28-masala
# # Foydalanuvchidan faslni olish
# fasl = input("Yil faslini kiriting (bahor / yoz / kuz / qish): ").lower()
#
# # Tavsiya etiladigan joy
# if fasl == "bahor":
#     print("Tavsiya: Samarqand")
# elif fasl == "yoz":
#     print("Tavsiya: Chorvoq")
# elif fasl == "kuz":
#     print("Tavsiya: Xiva")
# elif fasl == "qish":
#     print("Tavsiya: Beldersoy")
# else:
#     print("Noto‘g‘ri fasl kiritildi!")
#
# # 29-masala
# # Avtomobil turi va yo‘l sharoitini kiritish
# turi = input("Avtomobil turi (yengil / yuk): ").lower()
# sharoit = input("Yo‘l sharoiti (shahar / trassa): ").lower()
#
# # Sarfni aniqlash
# if turi == "yengil" and sharoit == "shahar":
#     sarf = 10
# elif turi == "yengil" and sharoit == "trassa":
#     sarf = 7
# elif turi == "yuk" and sharoit == "shahar":
#     sarf = 20
# elif turi == "yuk" and sharoit == "trassa":
#     sarf = 15
# else:
#     print("Noto‘g‘ri ma'lumot kiritildi!")
#     exit()
#
# # Natijani chiqarish
# print(f"Yoqilg‘i sarfi: {sarf} litr / 100 km")
#
# # 30-masala
# # Funksiya: eng katta va eng kichik to‘lovni topadi
# def tolov_solishtir(son1, son2, son3):
#     eng_katta = max(son1, son2, son3)
#     eng_kichik = min(son1, son2, son3)
#     print(f"Eng katta to‘lov: {eng_katta} so‘m")
#     print(f"Eng kichik to‘lov: {eng_kichik} so‘m")
#
# # Foydalanuvchidan 3 ta xizmat to‘lovini olish
# x1 = float(input("1-xizmat to‘lovi (so‘m): "))
# x2 = float(input("2-xizmat to‘lovi (so‘m): "))
# x3 = float(input("3-xizmat to‘lovi (so‘m): "))
#
# # Funksiyani chaqirish
# tolov_solishtir(x1, x2, x3)
#
# # 31-masala
# def elektr_tolovi(istemol):
#     if istemol <= 100:
#         tolov = istemol * 350
#     elif istemol <= 200:
#         tolov = (100 * 350) + (istemol - 100) * 450
#     else:
#         tolov = (100 * 350) + (100 * 450) + (istemol - 200) * 600
#     return tolov
#
# # Foydalanuvchidan ma'lumot olish
# try:
#     kv_soat = int(input("Iste'mol qilingan elektr (kVt/soat): "))
#     if kv_soat < 0:
#         print("Iste'mol manfiy bo'lishi mumkin emas!")
#     else:
#         print(f"Umumiy to‘lov: {elektr_tolovi(kv_soat)} so‘m")
# except ValueError:
#     print("Iltimos, faqat butun son kiriting!")
#
# # 32-masala
# # Foydalanuvchidan bo'y va vaznni olish
# boy = int(input("Bolaning bo'yi (sm): "))
# vazn = float(input("Bolaning vazni (kg): "))
#
# # Tekshiruv
# if 100 <= boy <= 130 and 20 <= vazn <= 40:
#     print("Sog‘lom")
# else:
#     print("Tekshiruv kerak")
#
# # 33-masala
# # Internet paket narxlari lug'ati
# narxlar = {
#     1: 9000,
#     5: 25000,
#     10: 45000,
#     30: 90000
# }
#
# # Foydalanuvchidan paket hajmini so'rash
# hajm = int(input("Internet paket hajmini tanlang (GB): "))
#
# # Narxni aniqlash va chiqarish
# if hajm in narxlar:
#     print(f"{hajm} GB uchun narx: {narxlar[hajm]} so'm")
# else:
#     print("Kechirasiz, tanlangan paket mavjud emas.")
#
# # 34-masala
# # Sportchilarning ballarini kiritish
# ball1 = float(input("1-sportchi balli: "))
# ball2 = float(input("2-sportchi balli: "))
# ball3 = float(input("3-sportchi balli: "))
#
# ballar = [ball1, ball2, ball3]
# eng_yuqori = max(ballar)
# nechta = ballar.count(eng_yuqori)
#
# if nechta > 1:
#     print("Durrang")
# else:
#     g_raqam = ballar.index(eng_yuqori) + 1
#     print(f"G'olib: {g_raqam}-sportchi")
#
# # 35-masala
# # Foydalanuvchidan ma'lumotlarni olish
# ishlaydi = input("Ishlaydiganmisiz? (ha/yo'q): ").strip().lower()
# oylik = float(input("Oylik maoshingiz (so'mda): "))
#
# # Qaror chiqarish
# if ishlaydi == "ha" and oylik > 5_000_000:
#     print("Yaroqli")
# else:
#     print("Yaroqsiz")
#
# # 36-masala
# # Foydalanuvchidan RAM va video karta borligini so'rash
# ram = float(input("Kompyuter RAM hajmi (GB): "))
# video_karta = input("Video karta mavjudmi? (ha/yo'q): ").strip().lower()
#
# # Shartni tekshirish
# if ram >= 8 and video_karta == "ha":
#     print("O‘yin ishlaydi")
# else:
#     print("Tizim talabiga javob bermaydi")
#
# # 37-masala
# # Baholarni kiritish
# baho1 = int(input("1-fan bahosi: "))
# baho2 = int(input("2-fan bahosi: "))
# baho3 = int(input("3-fan bahosi: "))
#
# baholar = [baho1, baho2, baho3]
#
# if all(b == 5 for b in baholar):
#     print("A’lochi")
# elif baholar.count(4) == 1:
#     print("Yaxshi")
# else:
#     print("O‘rtacha")
#
# # 38-masala
# def chegirma_hisobla(summasi):
#     if summasi < 100_000:
#         chegirma = 0
#     elif 100_000 <= summasi <= 200_000:
#         chegirma = 0.05
#     else:
#         chegirma = 0.10
#
#     chegirma_miqdori = summasi * chegirma
#     to_langan = summasi - chegirma_miqdori
#     return chegirma_miqdori, to_langan
#
# # Foydalanuvchidan summani olish
# xarid_sum = float(input("Xarid summasini kiriting (so'mda): "))
#
# # Chegirma va to'lovni hisoblash
# chegirma_sum, umumiy_tolash = chegirma_hisobla(xarid_sum)
#
# print(f"Chegirma: {chegirma_sum:.0f} so'm")
# print(f"To'lanadigan summa: {umumiy_tolash:.0f} so'm")
#
# # 39-masala
# # Masofani va dam olish kunini so'rash
# masofa = float(input("Masofani kiriting (km): "))
# dam_olish = input("Bugun dam olish kuni (ha/yo'q): ").strip().lower()
#
# # Asosiy narxni hisoblash
# asosiy_narx = masofa * 3000
#
# # Dam olish kuni bo'lsa, 20% qo'shish
# if dam_olish == "ha":
#     narx = asosiy_narx * 1.20
# else:
#     narx = asosiy_narx
#
# print(f"Taksi narxi: {narx:.0f} so'm")
#
# # 40-masala
# hisob_raqami = input("Hisob raqamingizni kiriting: ")
#
# if len(hisob_raqami) == 16 and hisob_raqami.isdigit():
#     print("Yaroqli")
# else:
#     print("Xato")
#
# # 41-masala
# lavozim = input("Lavozimni kiriting: ").strip().capitalize()
#
# if lavozim == "Direktor":
#     daraja = "A"
# elif lavozim == "Menejer":
#     daraja = "B"
# elif lavozim == "Ishchi":
#     daraja = "C"
# else:
#     daraja = "Noma’lum"
#
# print(f"Daraja: {daraja}")
#
# # 42-masala
# hudud = input("Hududni kiriting (Shahar/Qishloq): ").strip().capitalize()
# xonalar = int(input("Xonalar sonini kiriting: "))
#
# if hudud == "Shahar":
#     if xonalar == 3:
#         narx = 450_000_000
#     elif xonalar == 2:
#         narx = 300_000_000
#     else:
#         narx = None
# elif hudud == "Qishloq":
#     narx = 150_000_000
# else:
#     narx = None
#
# if narx:
#     print(f"Uy narxi: {narx} so'm")
# else:
#     print("Bunday hudud yoki xona soni uchun narx mavjud emas.")
#
# # 43-masala
# def kir_yuvish_rejimi(matot_turi, ifloslik_darajasi):
#     if matot_turi == "Paxta" and ifloslik_darajasi == "Yengil":
#         return "Rejim 1"
#     elif matot_turi == "Sintetik" and ifloslik_darajasi == "Og‘ir":
#         return "Rejim 3"
#     else:
#         return "Rejim 2"
#
#
# # Misol uchun:
# print(kir_yuvish_rejimi("Paxta", "Yengil"))   # Rejim 1
# print(kir_yuvish_rejimi("Sintetik", "Og‘ir")) # Rejim 3
# print(kir_yuvish_rejimi("Paxta", "Og‘ir"))    # Rejim 2
# print(kir_yuvish_rejimi("Sintetik", "Yengil"))# Rejim 2
# print(kir_yuvish_rejimi("Jun", "O‘rta"))      # Rejim 2
#
# # 44-masala
# def kitob_janri(nom):
#     nom_past = nom.lower()
#
#     if "sir" in nom_past or "jinoyat" in nom_past:
#         return "Detektiv"
#     elif "sevgi" in nom_past or "romantika" in nom_past:
#         return "Romantik"
#     elif "kosmos" in nom_past or "kelajak" in nom_past:
#         return "Fantastik"
#     else:
#         return "Boshqa"
#
#
# # Misollar:
# print(kitob_janri("Sirli jinoyat"))  # Detektiv
# print(kitob_janri("Sevgi va romantika"))  # Romantik
# print(kitob_janri("Kelajakdagi kosmos sarguzashtlari"))  # Fantastik
# print(kitob_janri("Tarixiy roman"))  # Boshqa
#
# # 45-masala
# def chipta_narxi(turi, yosh):
#     if turi == "VIP" and yosh > 60:
#         return 50000
#     elif turi == "Oddiy" and yosh < 18:
#         return 20000
#     else:
#         return 30000
#
# # Misollar:
# print(chipta_narxi("VIP", 65))    # 50000
# print(chipta_narxi("Oddiy", 15))  # 20000
# print(chipta_narxi("VIP", 40))    # 30000
# print(chipta_narxi("Oddiy", 25))  # 30000
#
# # 46-masala
# def do_kon_ish_vaqti(hafta_kuni, soat):
#     hafta_kuni = hafta_kuni.lower()
#
#     # Dushanba-Juma (Monday-Friday)
#     dushanba_juma = ["dushanba", "seshanba", "chorshanba", "payshanba", "juma"]
#     # Shanba-Yakshanba (Saturday-Sunday)
#     shanba_yakshanba = ["shanba", "yakshanba"]
#
#     if hafta_kuni in dushanba_juma and 9 <= soat <= 18:
#         return "Ochiq"
#     elif hafta_kuni in shanba_yakshanba and 10 <= soat <= 16:
#         return "Ochiq"
#     else:
#         return "Yopiq"
#
#
# # Misollar:
# print(do_kon_ish_vaqti("Dushanba", 10))  # Ochiq
# print(do_kon_ish_vaqti("Juma", 19))  # Yopiq
# print(do_kon_ish_vaqti("Shanba", 12))  # Ochiq
# print(do_kon_ish_vaqti("Yakshanba", 9))  # Yopiq
# print(do_kon_ish_vaqti("Chorshanba", 8))  # Yopiq
#
# # 47-masala
# def osimlik_parvarishi(osimlik_turi, fasl):
#     if osimlik_turi == "Gul" and fasl == "Bahor":
#         return "Haftada 3 marta sug'oring"
#     elif osimlik_turi == "Daraxt" and fasl == "Yoz":
#         return "Har kuni sug'oring"
#     elif osimlik_turi == "Gul" and fasl == "Qish":
#         return "Haftada 1 marta sug'oring"
#     else:
#         return "Haftada 2 marta sug'oring"
#
# # Misol uchun:
# print(osimlik_parvarishi("Gul", "Bahor"))  # Haftada 3 marta sug'oring
# print(osimlik_parvarishi("Daraxt", "Yoz"))  # Har kuni sug'oring
# print(osimlik_parvarishi("Gul", "Qish"))  # Haftada 1 marta sug'oring
# print(osimlik_parvarishi("Daraxt", "Qish"))  # Haftada 2 marta sug'oring
#
# # 48-masala
# def kredit_imkoniyati(yosh, oylik_daromad, kredit_tarixi):
#     if 21 <= yosh <= 65 and oylik_daromad > 3_000_000:
#         if kredit_tarixi == "Yaxshi":
#             return "Kredit beriladi"
#         elif kredit_tarixi == "Qoniqarli":
#             return "Qo'shimcha hujjat kerak"
#     return "Kredit berilmaydi"
#
# # Misollar
# print(kredit_imkoniyati(30, 4_000_000, "Yaxshi"))       # Kredit beriladi
# print(kredit_imkoniyati(40, 3_500_000, "Qoniqarli"))    # Qo'shimcha hujjat kerak
# print(kredit_imkoniyati(20, 4_000_000, "Yaxshi"))       # Kredit berilmaydi
# print(kredit_imkoniyati(50, 2_500_000, "Yaxshi"))       # Kredit berilmaydi
# print(kredit_imkoniyati(60, 3_200_000, "Yomon"))        # Kredit berilmaydi
#
# # 49-masala
# def joy_tavsiyasi(budjet, vip_kerak, yaxshi_korish):
#     if budjet > 100_000:
#         if vip_kerak:
#             return "Birinchi qator VIP"
#         else:
#             return "Birinchi qator oddiy"
#     else:
#         if yaxshi_korish:
#             return "O'rta qatorlar"
#         else:
#             return "Orqa qatorlar"
#
# # Misollar:
# print(joy_tavsiyasi(150_000, True, False))    # Birinchi qator VIP
# print(joy_tavsiyasi(120_000, False, True))    # Birinchi qator oddiy
# print(joy_tavsiyasi(90_000, False, True))     # O'rta qatorlar
# print(joy_tavsiyasi(80_000, False, False))    # Orqa qatorlar
#
# # 50-masala
# def xotira_tekshiruvi(xotira_foiz):
#     if xotira_foiz >= 95:
#         return "Xotira to'la! Tozalash kerak"
#     elif 80 <= xotira_foiz < 95:
#         return "Xotira kam qoldi"
#     elif 50 <= xotira_foiz < 80:
#         return "Xotira yetarli"
#     else:
#         return "Xotira bo'sh"
#
# # Misollar:
# print(xotira_tekshiruvi(96))  # Xotira to'la! Tozalash kerak
# print(xotira_tekshiruvi(85))  # Xotira kam qoldi
# print(xotira_tekshiruvi(70))  # Xotira yetarli
# print(xotira_tekshiruvi(45))  # Xotira bo'sh
#
# # 51-masala
# def kiyim_tavsiyasi(harorat, yomgir_ehtimoli):
#     if harorat < 0:
#         return "Qish kiyimi"
#     elif 0 <= harorat < 15 and yomgir_ehtimoli > 50:
#         return "Kuz kiyimi va soyabon"
#     elif 15 <= harorat < 25:
#         return "Bahor kiyimi"
#     elif harorat >= 25:
#         return "Yoz kiyimi"
#     else:
#         return "Ma'lumot yetarli emas"
#
# # Misollar:
# print(kiyim_tavsiyasi(-5, 30))    # Qish kiyimi
# print(kiyim_tavsiyasi(10, 60))    # Kuz kiyimi va soyabon
# print(kiyim_tavsiyasi(20, 40))    # Bahor kiyimi
# print(kiyim_tavsiyasi(30, 20))    # Yoz kiyimi
#
# # 52-masala
# def daraja_baholash(ball1, ball2, ball3):
#     umumiy_ball = ball1 + ball2 + ball3
#
#     if umumiy_ball >= 90:
#         return "Ustoz"
#     elif 70 <= umumiy_ball < 90:
#         return "Malakali"
#     elif 50 <= umumiy_ball < 70:
#         return "O'rta"
#     else:
#         return "Boshlang'ich"
#
#
# # Misollar:
# print(daraja_baholash(30, 30, 35))  # Ustoz (95)
# print(daraja_baholash(20, 25, 25))  # Malakali (70)
# print(daraja_baholash(15, 20, 10))  # O'rta (45)
# print(daraja_baholash(10, 15, 20))  # Boshlang'ich (45)
#
# # 53-masala
# def harorat_baholagich(harorat):
#     if harorat < 0:
#         return "Juda sovuq "
#     elif 0 <= harorat < 15:
#         return "Salqin "
#     elif 15 <= harorat < 30:
#         return "Iliq "
#     else:  # harorat >= 30
#         return "Issiq "
#
# # Misollar:
# print(harorat_baholagich(-5))   # Juda sovuq
# print(harorat_baholagich(10))   # Salqin
# print(harorat_baholagich(20))   # Iliq
# print(harorat_baholagich(35))   # Issiq
#
# # 54-masala
# def talaba_baho(umumiy_ball):
#     if 90 <= umumiy_ball <= 100:
#         return "5 baxo a"
#     elif 71 <= umumiy_ball <= 89:
#         return "4 baxo b"
#     elif 60 <= umumiy_ball < 71:
#         return "3 baxo o"
#     else:
#         return "Ball yetarli emas! x"
#
# # Misollar:
# print(talaba_baho(95))  # 5 baxo a
# print(talaba_baho(75))  # 4 baxo b
# print(talaba_baho(65))  # 3 baxo o
# print(talaba_baho(50))  # Ball yetarli emas! x
#
# # 55-masala
# def chipta_narxi(yosh, talaba):
#     if yosh < 7:
#         return "Bepul "
#     elif talaba:
#         return "5000 so‘m "
#     elif yosh >= 60:
#         return "Chegirma: 3000 so‘m "
#     else:
#         return "7000 so‘m "
#
# # Misollar:
# print(chipta_narxi(5, False))   # Bepul
# print(chipta_narxi(20, True))   # 5000 so‘m
# print(chipta_narxi(65, False))  # Chegirma: 3000 so‘m
# print(chipta_narxi(30, False))  # 7000 so‘m
#
# # 56-masala
# def yil_fasli(oy):
#     if oy in [12, 1, 2]:
#         return "Qish "
#     elif oy in [3, 4, 5]:
#         return "Bahor "
#     elif oy in [6, 7, 8]:
#         return "Yoz ️"
#     elif oy in [9, 10, 11]:
#         return "Kuz "
#     else:
#         return "Noto'g'ri oy raqami"
#
# # Misollar:
# print(yil_fasli(1))   # Qish
# print(yil_fasli(4))   # Bahor
# print(yil_fasli(7))   # Yoz
# print(yil_fasli(10))  # Kuz
# print(yil_fasli(13))  # Noto'g'ri oy raqami
#
# # 57-masala
# def telefon_narxi(model, holat):
#     if model == "iPhone":
#         if holat == "yangi":
#             return "1200$ "
#         elif holat == "ishlatilgan":
#             return "800$ "
#     elif model == "Samsung":
#         if holat == "yangi":
#             return "900$ "
#         elif holat == "ishlatilgan":
#             return "600$ "
#     return "Noto'g'ri ma'lumot"
#
# # Misollar:
# print(telefon_narxi("iPhone", "yangi"))       # 1200$
# print(telefon_narxi("iPhone", "ishlatilgan")) # 800$
# print(telefon_narxi("Samsung", "yangi"))      # 900$
# print(telefon_narxi("Samsung", "ishlatilgan"))# 600$
# print(telefon_narxi("Nokia", "yangi"))        # Noto'g'ri ma'lumot
#
# # 58-masala
# def maktabga_qabul(yosh, ball):
#     if yosh >= 6 and ball >= 70:
#         return "Qabul qilindi "
#     else:
#         return "Qabul qilinmadi "
#
# # Misollar:
# print(maktabga_qabul(7, 75))  # Qabul qilindi
# print(maktabga_qabul(5, 80))  # Qabul qilinmadi
# print(maktabga_qabul(6, 65))  # Qabul qilinmadi
#
# # 59-masala
# def bahola_internet_tezligi(tezlik):
#     if tezlik < 5:
#         return "toshbaqa Juda sekin yuryabdi"
#     elif 5 <= tezlik < 20:
#         return "odam O‘rtacha yuryabdi"
#     elif 20 <= tezlik <= 100:
#         return "odam Tez yuguryapdi"
#     else:
#         return "raketa Juda tez uchyabdi"
# print(bahola_internet_tezligi(3))    # toshbaqa Juda sekin yuryabdi
# print(bahola_internet_tezligi(10))   # odam O‘rtacha yuryabdi
# print(bahola_internet_tezligi(50))   # odam Tez yuguryapdi
# print(bahola_internet_tezligi(150))  # raketa Juda tez uchyabdi
#
# # 60-masala
# def uy_hayvoni_tavsiyasi(vaqt, joy, sabr):
#     if vaqt == "kam" and joy == "kam":
#         return " Baliq"
#     elif vaqt == "ko‘p" and sabr == "ha":
#         return " It"
#     else:
#         return " Mushuk"
# print(uy_hayvoni_tavsiyasi("kam", "kam", "yo‘q"))     #  Baliq
# print(uy_hayvoni_tavsiyasi("ko‘p", "ko‘p", "ha"))     #  It
# print(uy_hayvoni_tavsiyasi("o‘rtacha", "o‘rtacha", "yo‘q"))  #  Mushuk
#
# # 61-masala
# def ishga_qabul_sharti(yosh, tajriba, ingliz_tili):
#     if yosh >= 22 and tajriba >= 2 and ingliz_tili in ["o‘rta", "yaxshi"]:
#         return " Qabul qilindi"
#     else:
#         return " Qabul qilinmadi"
# print(ishga_qabul_sharti(25, 3, "yaxshi"))    #  Qabul qilindi
# print(ishga_qabul_sharti(21, 3, "o‘rta"))     #  Qabul qilinmadi
# print(ishga_qabul_sharti(24, 1, "yaxshi"))    #  Qabul qilinmadi
# print(ishga_qabul_sharti(26, 4, "past"))      #  Qabul qilinmadi
#
# # 62-masala
# def kabisa_yilmi(yil):
#     if (yil % 4 == 0 and yil % 100 != 0) or (yil % 400 == 0):
#         return " Kabisa yili"
#     else:
#         return " Kabisa yili emas"
# print(kabisa_yilmi(2020))  #  Kabisa yili
# print(kabisa_yilmi(1900))  #  Kabisa yili emas
# print(kabisa_yilmi(2000))  #  Kabisa yili
# print(kabisa_yilmi(2023))  #  Kabisa yili emas
#
# # 63-masala
# def soliq_foizi(daromad):
#     if daromad <= 1_000_000:
#         return " Soliq: 0%"
#     elif daromad <= 3_000_000:
#         return " Soliq: 10%"
#     else:
#         return " Soliq: 20%"
# print(soliq_foizi(800_000))     #  Soliq: 0%
# print(soliq_foizi(2_500_000))   #  Soliq: 10%
# print(soliq_foizi(4_200_000))   #  Soliq: 20%
#
# # 64-masala
# def imtihon_natijasi(fan, ball):
#     if ball >= 100:
#         natija = "Zo‘r natija!"
#     elif 100 <= ball <= 100:
#         natija = "Zo‘r natija!"
#     elif 100 <= ball <= 100:
#         natija = "Zo‘r natija!"
#     else:
#         natija = "Zo‘r natija!"
#
#     return f"{fan} fanidan baho: {ball} → {natija}"
# print(imtihon_natijasi("Matematika", 100))   # Matematika fanidan baho: 100 →  Zo‘r natija!
# print(imtihon_natijasi("Fizika", 100))       # Fizika fanidan baho: 100 →  Zo‘r natija!
# print(imtihon_natijasi("Kimyo", 100))        # Kimyo fanidan baho: 100 →  Zo‘r natija!
# print(imtihon_natijasi("Biologiya", 100))    # Biologiya fanidan baho: 100 →  Zo‘r natija!
#
# # 65-masala
# def chegirma_aniqlash(mahsulot_turi, yosh):
#     # Agar mahsulot oziq-ovqat bo‘lsa, hech qanday chegirma qo‘llanilmaydi
#     if mahsulot_turi.lower() == "oziq-ovqat":
#         return "Chegirma yo‘q"
#
#     # Yoshga qarab chegirma
#     if yosh < 12:
#         return "20% chegirma"
#     elif yosh > 60:
#         return "15% chegirma"
#     else:
#         return "Chegirma yo‘q"
#
# # Misol uchun sinov:
# print(chegirma_aniqlash("kiyim", 10))    # 20% chegirma
# print(chegirma_aniqlash("oziq-ovqat", 70))  # Chegirma yo‘q
# print(chegirma_aniqlash("kitob", 65))    # 15% chegirma
# print(chegirma_aniqlash("kiyim", 30))    # Chegirma yo‘q
#
# # 66-masala
# def velosiped_tavsiyasi(yosh):
#     if 5 <= yosh <= 10:
#         return "Bolalar velosipedi"
#     elif 11 <= yosh <= 17:
#         return "Sport velosipedi"
#     elif yosh >= 18:
#         return "Shahar velosipedi"
#     else:
#         return "Yosh mos kelmaydi (5 yoshdan kichik)"
# print(velosiped_tavsiyasi(7))   # ➤ Bolalar velosipedi
# print(velosiped_tavsiyasi(15))  # ➤ Sport velosipedi
# print(velosiped_tavsiyasi(22))  # ➤ Shahar velosipedi
# print(velosiped_tavsiyasi(3))   # ➤ Yosh mos kelmaydi (5 yoshdan kichik)
#
# # 67-masala
# def muzqaymoq_maslahati(ob_havo, vaqt):
#     if ob_havo.lower() == "issiq" and vaqt.lower() == "tush":
#         return "Tavsiya qilinadi"
#     else:
#         return "Keyinroq"
# print(muzqaymoq_maslahati("issiq", "tush"))     # ➤ Tavsiya qilinadi
# print(muzqaymoq_maslahati("salqin", "tush"))    # ➤ Keyinroq
# print(muzqaymoq_maslahati("issiq", "kechqurun"))# ➤ Keyinroq
#
# # 68-masala
# def toy_mehmoni(yosh, munosabat):
#     if munosabat.lower() == "yaqin" and yosh >= 18:
#         return "Chaqirilgan"
#     elif munosabat.lower() == "do‘st" and yosh >= 25:
#         return "Chaqirilgan"
#     else:
#         return "Chaqirilmagan"
# print(toy_mehmoni(20, "yaqin"))   # ➤ Chaqirilgan
# print(toy_mehmoni(30, "do‘st"))   # ➤ Chaqirilgan
# print(toy_mehmoni(22, "do‘st"))   # ➤ Chaqirilmagan
# print(toy_mehmoni(17, "yaqin"))   # ➤ Chaqirilmagan
#
# # 69-masala
# def tatil_joyi_tanlovi(byudjet, ob_havo, uzoqlik):
#     if byudjet.lower() == "kam":
#         return "Mahalliy"
#     elif ob_havo.lower() == "yaxshi" and uzoqlik.lower() == "yaqin":
#         return "Tog‘"
#     else:
#         return "Plyaj"
# print(tatil_joyi_tanlovi("kam", "yaxshi", "yaqin"))   # ➤ Mahalliy
# print(tatil_joyi_tanlovi("kop", "yaxshi", "yaqin"))   # ➤ Tog‘
# print(tatil_joyi_tanlovi("kop", "yomon", "uzoqqa"))   # ➤ Plyaj
#
# # 70-masala
# def tandir_harorati(tandir_turi, vaqt):
#     if tandir_turi.lower() == "elektr" and vaqt < 30:
#         return "180°C"
#     elif tandir_turi.lower() == "gaz" and vaqt >= 30:
#         return "200°C"
#     else:
#         return "160°C"
# print(tandir_harorati("elektr", 25))   # ➤ 180°C
# print(tandir_harorati("gaz", 30))      # ➤ 200°C
# print(tandir_harorati("gaz", 20))      # ➤ 160°C
#
# # 71-masala
# def stipendiya_beriladimi(daraja, ortacha_baho):
#     daraja = daraja.lower()  # kichik harflarga o'tkazamiz
#
#     if daraja == "bakalavr" and ortacha_baho >= 85:
#         return "to'ri Stipendiya beriladi"
#     elif daraja == "magistr" and ortacha_baho >= 90:
#         return "to'ri Stipendiya beriladi"
#     else:
#         return "noto'g'ri Stipendiya berilmaydi"
#
# # Misollar:
# print(stipendiya_beriladimi("bakalavr", 87))   # to'ri
# print(stipendiya_beriladimi("magistr", 88))    # noto'g'ri
# print(stipendiya_beriladimi("magistr", 92))    # to'ri
# print(stipendiya_beriladimi("bakalavr", 80))   # noto'g'ri
#
# # 72-masala
# import re
#
# def parol_xavfsizligi(parol):
#     uzun = len(parol) >= 8
#     raqam_bor = any(char.isdigit() for char in parol)
#     maxsus_belgi_bor = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", parol))
#
#     if uzun and raqam_bor and maxsus_belgi_bor:
#         return " Xavfsiz"
#     elif raqam_bor or uzun:
#         return " O‘rtacha"
#     else:
#         return " Xavfli"
#
# # Misollar:
# print(parol_xavfsizligi("parol123!"))   #  Xavfsiz
# print(parol_xavfsizligi("1234567"))     # ️ O‘rtacha
# print(parol_xavfsizligi("parol"))       #  Xavfli
# print(parol_xavfsizligi("parol123"))    #  O‘rtacha
#
# # 73-masala
# def ijarani_hisobla(tur, soat):
#     if tur.lower() == "shahar":
#         narx_soat = 10000
#     elif tur.lower() == "sport":
#         narx_soat = 15000
#     else:
#         return " Noto‘g‘ri velosiped turi"
#
#     umumiy_narx = narx_soat * soat
#
#     # Chegirma
#     if soat > 5:
#         chegirma = 0.20
#     elif soat > 3:
#         chegirma = 0.10
#     else:
#         chegirma = 0.0
#
#     chegirmali_narx = umumiy_narx * (1 - chegirma)
#     return f" To‘lov: {int(chegirmali_narx):,} so‘m"
#
# # Misollar:
# print(ijarani_hisobla("shahar", 2))   #  20,000
# print(ijarani_hisobla("sport", 4))    #  54,000 (10% chegirma)
# print(ijarani_hisobla("shahar", 6))   #  48,000 (20% chegirma)
# print(ijarani_hisobla("tog'", 2))     #  Noto‘g‘ri velosiped turi
#
# # 74-masala
# def meva_sifati(ogirlik, korinish):
#     korinish = korinish.lower()
#
#     if korinish == "yomon":
#         return " Past sifat"
#     elif ogirlik < 100:
#         return " Rad etiladi"
#     elif ogirlik > 200 and korinish == "yaxshi":
#         return " Premium"
#     elif 100 <= ogirlik <= 200 and korinish == "yaxshi":
#         return " Standart"
#     else:
#         return " Nomaʼlum holat"
#
# # Misollar:
# print(meva_sifati(250, "yaxshi"))   #  Premium
# print(meva_sifati(150, "yaxshi"))   #  Standart
# print(meva_sifati(180, "yomon"))    #  Past sifat
# print(meva_sifati(90, "yaxshi"))    #  Rad etiladi
#
# # 75-masala
# def chegirma_hisobla(summa, soat):
#     if summa > 100000 and 18 <= soat < 22:
#         chegirma = 0.15
#     elif 50000 <= summa <= 100000 and 10 <= soat < 18:
#         chegirma = 0.10
#     else:
#         chegirma = 0.0
#
#     yakuniy_summa = summa * (1 - chegirma)
#     return f" To‘lov: {int(yakuniy_summa):,} so‘m |  Chegirma: {int(chegirma * 100)}%"
#
# # Misollar:
# print(chegirma_hisobla(120000, 19))  #  To‘lov: 102,000 |  Chegirma: 15%
# print(chegirma_hisobla(75000, 15))   #  To‘lov: 67,500 |  Chegirma: 10%
# print(chegirma_hisobla(40000, 12))   #  To‘lov: 40,000 |  Chegirma: 0%
# print(chegirma_hisobla(105000, 10))  #  To‘lov: 105,000 |  Chegirma: 0%
#
# # 76-masala
# def harakat_maslahati(chiroq_rangi, yol_holati=None):
#     chiroq_rangi = chiroq_rangi.lower()
#
#     if chiroq_rangi == "qizil":
#         return " To‘xtang"
#     elif chiroq_rangi == "sariq":
#         return "️ Tayyorlaning"
#     elif chiroq_rangi == "yashil":
#         if yol_holati is None:
#             return "ℹ Yo‘l holati aniqlanmagan"
#         elif yol_holati.lower() == "bo‘sh":
#             return " Yuring"
#         elif yol_holati.lower() == "band":
#             return " Kuting"
#         else:
#             return " Nomaʼlum yo‘l holati"
#     else:
#         return " Nomaʼlum signal"
#
#
# # Misollar:
# print(harakat_maslahati("qizil"))  #  To‘xtang
# print(harakat_maslahati("yashil", "bo‘sh"))  #  Yuring
# print(harakat_maslahati("yashil", "band"))  #  Kuting
# print(harakat_maslahati("sariq"))  #  Tayyorlaning
# print(harakat_maslahati("yashil"))  # ℹ Yo‘l holati aniqlanmagan
#
# # 77-masala
# def ijara_narxi(kitob_turi, kunlar):
#     kitob_turi = kitob_turi.lower()
#
#     if kitob_turi == "ilmiy":
#         narx_kun = 2000
#     elif kitob_turi == "badiiy":
#         narx_kun = 1000
#     else:
#         return " Noto‘g‘ri kitob turi"
#
#     jami = narx_kun * kunlar
#
#     if kunlar > 14:
#         chegirma = 0.30
#     elif kunlar > 7:
#         chegirma = 0.20
#     else:
#         chegirma = 0.0
#
#     yakuniy_narx = jami * (1 - chegirma)
#     return f" To‘lov: {int(yakuniy_narx):,} so‘m | 🏷 Chegirma: {int(chegirma * 100)}%"
#
#
# # Misollar:
# print(ijara_narxi("ilmiy", 5))  # 10,000 so‘m (chegirma yo‘q)
# print(ijara_narxi("badiiy", 10))  # 8,000 so‘m (20% chegirma)
# print(ijara_narxi("ilmiy", 15))  # 21,000 so‘m (30% chegirma)
# print(ijara_narxi("detektiv", 5))  #  xatolik
#
# # 78-masala
# def navbat_belgilash(yosh, holat):
#     holat = holat.lower()
#
#     if yosh < 10 or yosh > 70:
#         return " Zudlik bilan"
#     elif holat == "og‘ir":
#         return " Navbat 1-soat ichida"
#     elif holat == "oddiy":
#         return " Navbat 3-soat ichida"
#     else:
#         return " Nomaʼlum holat"
#
#
# # Misollar:
# print(navbat_belgilash(5, "oddiy"))  #  Zudlik bilan
# print(navbat_belgilash(75, "og‘ir"))  #  Zudlik bilan
# print(navbat_belgilash(35, "og‘ir"))  #  Navbat 1-soat ichida
# print(navbat_belgilash(40, "oddiy"))  #  Navbat 3-soat ichida
# print(navbat_belgilash(25, "nomaʼlum"))  #  Nomaʼlum holat
#
# # 79-masala
# def sugorish_maslahati(osimlik, tuproq):
#     osimlik = osimlik.lower()
#     tuproq = tuproq.lower()
#
#     if osimlik == "gul" and tuproq == "qumloq":
#         return " Har 2 kunda sug‘oring"
#     elif osimlik == "daraxt" and tuproq == "loy":
#         return " Haftada 1 marta sug‘oring"
#     else:
#         return " Har 3 kunda sug‘oring"
#
#
# # Misollar:
# print(sugorish_maslahati("gul", "qumloq"))  #  Har 2 kunda sug‘oring
# print(sugorish_maslahati("daraxt", "loy"))  #  Haftada 1 marta sug‘oring
# print(sugorish_maslahati("gul", "loy"))  #  Har 3 kunda sug‘oring
# print(sugorish_maslahati("bargdor", "qor"))  #  Har 3 kunda sug‘oring
#
# # 80-masala
# def usta_narxi(xizmat_turi, ish_vaqti_soat):
#     xizmat_turi = xizmat_turi.lower()
#
#     if xizmat_turi == "ta’mirlash":
#         narx_soat = 50000
#     elif xizmat_turi == "o‘rnatish":
#         narx_soat = 30000
#     else:
#         return " Noto‘g‘ri xizmat turi"
#
#     jami_narx = narx_soat * ish_vaqti_soat
#
#     if ish_vaqti_soat > 5:
#         jami_narx *= 0.9  # 10% chegirma
#
#     return f" To‘lov: {int(jami_narx):,} so‘m"
#
# # Misollar:
# print(usta_narxi("ta’mirlash", 3))    # 150,000 so‘m
# print(usta_narxi("o‘rnatish", 6))     # 162,000 so‘m (10% chegirma bilan)
# print(usta_narxi("bo‘yash", 4))       #  Noto‘g‘ri xizmat turi
#
# # 81-masala
# def sumka_tavsiyasi(sinf, ogirlik_kg):
#     if 1 <= sinf <= 4 and ogirlik_kg > 2:
#         return "️ Og‘ir, kamaytiring"
#     elif 5 <= sinf <= 9 and ogirlik_kg > 4:
#         return "️ Og‘ir, kamaytiring"
#     else:
#         return " Normal"
#
# # Misollar:
# print(sumka_tavsiyasi(3, 2.5))  # ️ Og‘ir, kamaytiring
# print(sumka_tavsiyasi(7, 3.5))  #  Normal
# print(sumka_tavsiyasi(8, 4.5))  #  Og‘ir, kamaytiring
# print(sumka_tavsiyasi(10, 5))   #  Normal
#
# # 82-masala
# def kafe_narxi(turi, miqdor):
#     turi = turi.lower()
#
#     if turi == "kofe":
#         narx_dona = 15000
#     elif turi == "choy":
#         narx_dona = 5000
#     else:
#         return " Noto‘g‘ri buyurtma turi"
#
#     jami = narx_dona * miqdor
#
#     if miqdor > 5:
#         jami *= 0.9  # 10% chegirma
#
#     return f" To‘lov: {int(jami):,} so‘m"
#
# # Misollar:
# print(kafe_narxi("kofe", 3))    # 45,000 so‘m
# print(kafe_narxi("choy", 6))    # 27,000 so‘m (10% chegirma bilan)
# print(kafe_narxi("suv", 2))     #  Noto‘g‘ri buyurtma turi
#
# # 83-masala
# def marshrut_vaqti(masofa_km, transport):
#     transport = transport.lower()
#
#     if transport == "piyoda":
#         vaqt_km = 12
#     elif transport == "velosiped":
#         vaqt_km = 4
#     elif transport == "avtobus":
#         vaqt_km = 2
#     else:
#         return " Noto‘g‘ri transport turi"
#
#     jami_vaqt = masofa_km * vaqt_km
#     return f" Sayohat vaqti: {jami_vaqt} daqiqa"
#
# # Misollar:
# print(marshrut_vaqti(5, "piyoda"))     # 60 daqiqa
# print(marshrut_vaqti(10, "velosiped")) # 40 daqiqa
# print(marshrut_vaqti(7, "avtobus"))    # 14 daqiqa
# print(marshrut_vaqti(3, "mashina"))    #  Noto‘g‘ri transport turi
#
# # 84-masala
# def batareya_holati(foiz, vaqt_soat):
#     if foiz < 20 and vaqt_soat > 1:
#         return "️ Zudlik bilan zaryadlang"
#     elif 20 <= foiz <= 50 and vaqt_soat < 1:
#         return " Tezroq zaryadlang"
#     elif foiz == 50:
#         return " Yaxshi holat"
#     else:
#         return "️ Holat normal yoki qo‘shimcha ma'lumot kerak"
#
# # Misollar:
# print(batareya_holati(15, 2))    # ️ Zudlik bilan zaryadlang
# print(batareya_holati(30, 0.5))  #  Tezroq zaryadlang
# print(batareya_holati(50, 5))    #  Yaxshi holat
# print(batareya_holati(60, 0.2))  #  Holat normal yoki qo‘shimcha ma'lumot kerak
#
# # 85-masala
# def bonus_berish(xarid_summasi, mijoz_turi):
#     mijoz_turi = mijoz_turi.lower()
#
#     if mijoz_turi == "doimiy" and xarid_summasi > 50000:
#         return " 5000 so‘m bonus beriladi"
#     elif mijoz_turi == "yangi" and xarid_summasi > 100000:
#         return " 3000 so‘m bonus beriladi"
#     else:
#         return " Bonus yo‘q"
#
# # Misollar:
# print(bonus_berish(60000, "doimiy"))  # 5000 so‘m bonus beriladi
# print(bonus_berish(120000, "yangi"))  # 3000 so‘m bonus beriladi
# print(bonus_berish(40000, "doimiy"))  # Bonus yo‘q
#
# # 86-masala
# def obhavo_maslahati(harorat, yomgir_ehtimoli):
#     if harorat < 5:
#         return " Issiq kiyining"
#     elif yomgir_ehtimoli > 70:
#         return "️ Soyabon oling"
#     elif 5 <= harorat <= 25 and yomgir_ehtimoli < 30:
#         return " Yengil kiyining"
#     else:
#         return "️ Holat uchun qo‘shimcha maslahat yo‘q"
#
# # Misollar:
# print(obhavo_maslahati(3, 20))   # Issiq kiyining
# print(obhavo_maslahati(10, 80))  # Soyabon oling
# print(obhavo_maslahati(20, 10))  # Yengil kiyining
# print(obhavo_maslahati(30, 40))  # Holat uchun qo‘shimcha maslahat yo‘q
#
# # 87-masala
# def universitet_qabul(bal, kvota):
#     if bal >= 90 and kvota:
#         return " Qabul qilindi"
#     elif 70 <= bal <= 89 and not kvota:
#         return " Navbat kuting"
#     elif bal < 70:
#         return " Qabul qilinmadi"
#     else:
#         return " Qo‘shimcha ma'lumot kerak"
#
# # Misollar:
# print(universitet_qabul(92, True))   # Qabul qilindi
# print(universitet_qabul(75, False))  # Navbat kuting
# print(universitet_qabul(65, True))   # Qabul qilinmadi
#
# # 88-masala
# def sport_dasturi(mashq_turi, tajriba_yil):
#     mashq_turi = mashq_turi.lower()
#
#     if mashq_turi == "kardio" and tajriba_yil < 1:
#         return "️ 20 daqiqa yengil"
#     elif mashq_turi == "og‘irlik" and tajriba_yil >= 2:
#         return "️ 60 daqiqa intensiv"
#     else:
#         return " 30 daqiqa o‘rtacha"
#
# # Misollar:
# print(sport_dasturi("kardio", 0.5))  # 20 daqiqa yengil
# print(sport_dasturi("og‘irlik", 3))  # 60 daqiqa intensiv
# print(sport_dasturi("kardio", 2))    # 30 daqiqa o‘rtacha
#
# # 89-masala
# def tv_tavsiya(korsatuv_turi, vaqt_soat):
#     # vaqt_soat format: "HH:MM" misol: "18:30"
#     hour = int(vaqt_soat.split(":")[0])
#     minute = int(vaqt_soat.split(":")[1])
#     total_minutes = hour * 60 + minute
#
#     if korsatuv_turi.lower() == "yangiliklar" and 18*60 <= total_minutes <= 20*60:
#         return " Tomosha qiling"
#     elif korsatuv_turi.lower() == "serial" and 20*60 <= total_minutes <= 22*60:
#         return " Qayta ko‘ring"
#     else:
#         return " Boshqa ko‘rsatuv tanlang"
#
# # Misollar:
# print(tv_tavsiya("Yangiliklar", "18:30"))  # Tomosha qiling
# print(tv_tavsiya("Serial", "21:15"))       # Qayta ko‘ring
# print(tv_tavsiya("Yangiliklar", "21:00"))  # Boshqa ko‘rsatuv tanlang
#
# # 90-masala
# def skuter_narxi(turi, masofa_km):
#     turi = turi.lower()
#
#     if turi == "elektr":
#         narx = 2000
#     elif turi == "oddiy":
#         narx = 1000
#     else:
#         return " Noto‘g‘ri skuter turi"
#
#     jami = narx * masofa_km
#
#     if masofa_km > 10:
#         jami *= 0.85  # 15% chegirma
#
#     return f" To‘lov: {int(jami):,} so‘m"
#
# # Misollar:
# print(skuter_narxi("elektr", 8))    # 16,000 so‘m
# print(skuter_narxi("oddiy", 12))    # 10,200 so‘m (15% chegirma bilan)
# print(skuter_narxi("gibrid", 5))    #  Noto‘g‘ri skuter turi
#
# # 91-masala
# def repair_cost(problem_type, part_price=0):
#     if problem_type == "dasturiy":
#         return 50000
#     elif problem_type == "uskunaviy":
#         if part_price > 100000:
#             return 150000
#         else:
#             return 80000
#     else:
#         return "Notogri muammo turi"
#
#         # Misollar:
# print(repair_cost("dasturiy"))  # 50000
# print(repair_cost("uskunaviy", 120000))  # 150000
# print(repair_cost("uskunaviy", 90000))  # 80000
#
# # 92-masala
# def ekologik_holat(ibloslanish, shamol_kms):
#     if ibloslanish > 50 and shamol_kms < 5:
#         return " Maska kiying"
#     elif ibloslanish <= 50 and shamol_kms > 10:
#         return "️ Sof havo"
#     else:
#         return " Oddiy holat"
#
# # Misollar:
# print(ekologik_holat(60, 3))   # Maska kiying
# print(ekologik_holat(40, 15))  # Sof havo
# print(ekologik_holat(30, 7))   # Oddiy holat
#
# # 93-masala
# def kurs_narxi(turi, davomiylik_oy):
#     turi = turi.lower()
#
#     if turi == "akvarel":
#         narx = 200000 * davomiylik_oy
#     elif turi == "yog‘li bo‘yoq":
#         narx = 300000 * davomiylik_oy
#     else:
#         return " Noto‘g‘ri kurs turi"
#
#     if davomiylik_oy > 3:
#         narx *= 0.9  # 10% chegirma
#
#     return f" To‘lov: {int(narx):,} so‘m"
#
# # Misollar:
# print(kurs_narxi("akvarel", 1))      # 200,000 so‘m
# print(kurs_narxi("yog‘li bo‘yoq", 4)) # 1,080,000 so‘m (chegirma bilan)
# print(kurs_narxi("pastel", 2))       # Noto‘g‘ri kurs turi
#
# # 94-masala
# def qulflash_xavfsizligi(turi, yoshi):
#     turi = turi.lower()
#
#     if turi == "elektron" and yoshi < 2:
#         return " Yuqori xavfsizlik"
#     elif turi == "mexanik" and yoshi < 5:
#         return " O‘rtacha xavfsizlik"
#     else:
#         return "️ Past xavfsizlik"
#
# # Misollar:
# print(qulflash_xavfsizligi("elektron", 1))  # Yuqori xavfsizlik
# print(qulflash_xavfsizligi("mexanik", 3))   # O‘rtacha xavfsizlik
# print(qulflash_xavfsizligi("elektron", 3))  # Past xavfsizlik
#
# # 95-masala
# def uy_ijarasi_narxi(joylashuv, xonalar_soni):
#     joylashuv = joylashuv.lower()
#
#     if joylashuv == "shahar markazi" and xonalar_soni == 3:
#         return " 5 000 000 so‘m"
#     elif joylashuv == "shahar cheti" and xonalar_soni == 2:
#         return " 3 000 000 so‘m"
#     else:
#         return " 2 000 000 so‘m"
#
# # Misollar:
# print(uy_ijarasi_narxi("shahar markazi", 3))  # 5 000 000 so‘m
# print(uy_ijarasi_narxi("shahar cheti", 2))    # 3 000 000 so‘m
# print(uy_ijarasi_narxi("qishloq", 4))         # 2 000 000 so‘m
#
# # 96-masala
# def skuter_quvvat_maslahat(quvvat_foiz, masofa_km):
#     if quvvat_foiz < 20 and masofa_km > 5:
#         return "️ Zaryadlang"
#     elif 20 <= quvvat_foiz <= 50 and masofa_km < 3:
#         return " Ehtiyot bo‘ling"
#     elif quvvat_foiz > 50:
#         return " Yaxshi holat"
#     else:
#         return "️ Holat noaniq"
#
# # Misollar:
# print(skuter_quvvat_maslahat(15, 6))   # Zaryadlang
# print(skuter_quvvat_maslahat(40, 2))   # Ehtiyot bo‘ling
# print(skuter_quvvat_maslahat(60, 10))  # Yaxshi holat
# print(skuter_quvvat_maslahat(45, 5))   # Holat noaniq
#
# # 97-masala
# def kamera_sifati(ruxsat_mp, yoruglik):
#     yoruglik = yoruglik.lower()
#
#     if ruxsat_mp >= 12 and yoruglik == "yaxshi":
#         return " Yuqori sifat"
#     elif 8 <= ruxsat_mp < 12 and yoruglik == "o‘rtacha":
#         return " O‘rtacha sifat"
#     else:
#         return " Past sifat"
#
# # Misollar:
# print(kamera_sifati(13, "yaxshi"))  # Yuqori sifat
# print(kamera_sifati(10, "o‘rtacha"))  # O‘rtacha sifat
# print(kamera_sifati(7, "yaxshi"))  # Past sifat
#
# # 98-masala
# def sayr_maslahati(masofa_km, ob_havo):
#     ob_havo = ob_havo.lower()
#
#     if masofa_km < 5 and ob_havo == "yaxshi":
#         return " Piyoda"
#     elif 5 <= masofa_km <= 20 and ob_havo == "o‘rtacha":
#         return " Velosiped"
#     else:
#         return " Avtobus"
#
# # Misollar:
# print(sayr_maslahati(3, "yaxshi"))  # Piyoda
# print(sayr_maslahati(10, "o‘rtacha"))  # Velosiped
# print(sayr_maslahati(25, "yomon"))  # Avtobus
#
# # 99-masala
# def email_holati(email):
#     uzunlik = len(email)
#     email = email.lower()
#
#     if uzunlik >= 10 and email.endswith("@gmail.com"):
#         return " Qabul qilindi"
#     elif uzunlik < 10 and email.endswith("@yahoo.com"):
#         return "️ Qisqa email"
#     else:
#         return " Noto‘g‘ri email"
#
# # Misollar:
# print(email_holati("user@gmail.com"))    # Qabul qilindi
# print(email_holati("abc@yahoo.com"))     # Qisqa email
# print(email_holati("test@outlook.com"))  # Noto‘g‘ri email
#
# # 100-masala
# def ovqat_kaloriya(turi, porsiya_g):
#     turi = turi.lower()
#     kaloriya_100g = 0
#
#     if turi == "salat":
#         kaloriya_100g = 50
#     elif turi == "go‘sht" or turi == "gosht":
#         kaloriya_100g = 200
#     else:
#         return "Noma'lum ovqat turi"
#
#     kaloriya = (porsiya_g / 100) * kaloriya_100g
#
#     if porsiya_g > 300:
#         kaloriya *= 1.10  # 10% qo‘shimcha
#
#     return f"{kaloriya:.2f} kkal"
#
# # Misollar:
# print(ovqat_kaloriya("Salat", 100))    # 50.00 kkal
# print(ovqat_kaloriya("Go‘sht", 350))   # 770.00 kkal (350 * 2 * 1.10)
# print(ovqat_kaloriya("Sho‘rva", 200))  # Noma'lum ovqat turi
#
# # 101-masala
# def kredit_foizi(summa, muddat_yil):
#     if summa < 10_000_000 and muddat_yil == 1:
#         return "12%"
#     elif summa >= 10_000_000 and muddat_yil == 2:
#         return "10%"
#     else:
#         return "15%"
#
# # Misollar:
# print(kredit_foizi(5_000_000, 1))    # 12%
# print(kredit_foizi(15_000_000, 2))   # 10%
# print(kredit_foizi(7_000_000, 3))    # 15%
#
# # 102-masala
# def parvoz_narxi(sinf, masofa):
#     if sinf.lower() == 'ekonom':
#         narx = 500_000
#     elif sinf.lower() == 'biznes':
#         narx = 1_000_000
#     else:
#         return "Noto‘g‘ri sinf kiritildi"
#
#     if masofa >= 1000:
#         narx *= 1.2  # 20% qo‘shamiz
#
#     return int(narx)
# print(parvoz_narxi('ekonom', 800))   # ➞ 500000 $
# print(parvoz_narxi('biznes', 800))   # ➞ 1000000 $
# print(parvoz_narxi('ekonom', 1200))  # ➞ 600000 $
# print(parvoz_narxi('biznes', 1500))  # ➞ 1200000 $
