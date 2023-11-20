Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 08:06:12) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print("Program raport SMP Bangun Insan Mandiri")
nama_siswa = input("Masukkan nama siswa: ")
kelas=input("Masukkan kelas siswa :")
tahun=input("Masukkan Tahun Ajaran :")
print("1. Raport Kurikulum Merdeka")
print("2. Raport Kurikulum Edexcel")
pilihan = int(input("Masukan pilihan: "))
def Raport_Merdeka(MP1,MP2,MP3,MP4,MP5,MP6,MP7,MP8):
    M = (MP1+MP2+MP3+MP4+MP5+MP6+MP7+MP8)/8
    return M
def Raport_Edexcel(S1,S2,S3):
    E=(S1+S2+S3)/3
    return E
if pilihan == 1:
    MP1 = int(input("masukan nilai Agama: "))
    MP2 = int(input("masukan nilai Bahasa Indonesia: "))
    MP3 = int(input("masukan nilai Bahasa Inggris: "))
    MP4 = int(input("masukan nilai Matematika: "))
    MP5 = int(input("masukan nilai Informatika: "))
    MP6 = int(input("masukan nilai IPA: "))
    MP7 = int(input("masukan nilai IPS: "))
    MP8 = int(input("masukan nilai Art: "))
    print("====================================================")
    print("Laporan Hasil Belajar SMP Bangun Insan Mandiri")
    print("Nama Siswa :",nama_siswa)
    print("Kelas :", kelas)
    print("Tahun Ajaran : ",tahun)
    print("Nilai Mata Pelajaran : \n1.Pendidikan Agama:{} \n2.Bahasa Indonesia:{} \n3.Bahasa Inggris:{}\n4.Matematika:{}\n5.Informatika:{}\n6.IPA:{}\n7.IPS:{}\n8.Art:{},\nNilai Raport:{}".format(MP1,MP2,MP3,MP4,MP5,MP6,MP7,MP8, Raport_Merdeka (MP1,MP2,MP3,MP4,MP5,MP6,MP7,MP8)))
    if Raport_Merdeka (MP1,MP2,MP3,MP4,MP5,MP6,MP7,MP8)>=70:
        print("KETERANGAN : LULUS")
    else :
        print("KETERANGAN : TIDAK LULUS")
    print("====================================================")
elif pilihan == 2:
      S1 = int(input("Input English Score : "))
      S2 = int(input("Input Science Score: "))
      S3 = int(input("Input Math Score: "))
      print("====================================================")
      print("SMP Bangun Insan Mandiri Student's Academic")
      print("Studet Name :",nama_siswa)
      print("Class :", kelas)
      print("Academic : ",tahun)
      print("Subjects score:\n1.English:{},\n2. Science:{},\n3.Math:{},\nReport Score:{}".format(S1,S2,S3, Raport_Edexcel (S1,S2,S3)))
      if Raport_Edexcel (S1,S2,S3)>=70:
        print("CATEGORY : GRADUATED")
      else :
        print("CATEGORY : NOT GRADUATED")
      print("====================================================")
else:
    print("pilihan anda salah, silahkan ulangi dengan pilihan yang tersedia")
