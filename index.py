def SemestersToIPK():
  # menginstall semua variable yang dibutuhkan aplikasi
  nama = input('Masukkan nama: ')
  total_semester_yang_diikuti = int(input('Jumlah semester yang diikuti: '))
  penampung_semua_nilai_semester = []
  total_nilai_semester = 0
  grade = ""
  ipk = 0

  # function ini berguna mengisi penampung semua nilai semester, 
  # contoh: yang tadinya hanya [] => [3.95, 3.21, 3.10, 3.5]. jumlah nilai didalam array ada 4, 4 diambil dari total semester yang diikuti
  def masukan_nilai_per_semester_ke_penampung_nilai_semester():
    for i in range(total_semester_yang_diikuti): 
      nilai_per_semester = input('Jumlah Nilai Semester - ' + str(i + 1) + ': ')
      penampung_semua_nilai_semester.append(float(nilai_per_semester))
      
    # di uncomment saja jika penasaran apa yang berubah
    # print('ini adalah semua nilai per-semester yang kamu input: ', penampung_semua_nilai_semester)


  # function ini menjumlah semua yang ada didalam penampung
  # contoh: [3.95, 3.21, 3.10, 3.5] dijumlahkan => 13.76 
  # nilai 0 yang ada di total_nilai_semester akan berubah/ditambahkan

  def menjumlahkan_semua_yang_ada_didalam_penampung_semua_nilai_semester():
    nonlocal total_nilai_semester

    for i in penampung_semua_nilai_semester:
      total_nilai_semester += i

    # di uncomment saja jika penasaran apa yang berubah
    # print('total_nilai_semester', total_nilai_semester)

  def menghitung_ipk_dan_memberi_grade():
    nonlocal ipk
    nonlocal grade

    ipk = round(total_nilai_semester / total_semester_yang_diikuti, 2)
    
    if (ipk >= 3):
      grade = "A"

    elif (ipk >= 2 and ipk < 3):
      grade = "B"

    elif (ipk >= 1 and ipk < 2):
      grade = "C"

    elif (ipk < 1):
      grade = "D"

    else: 
      print('ada kesalahan di input')

  def hasil_akhir():
    print('Nama:', nama)
    print('IPK:', ipk)
    print('Grade:', grade)
    print('Total Semester yang diikuti:', total_semester_yang_diikuti)
    print('Total Nilai Semester:', total_nilai_semester)

  # urutan berjalannya aplikasi
  masukan_nilai_per_semester_ke_penampung_nilai_semester()
  menjumlahkan_semua_yang_ada_didalam_penampung_semua_nilai_semester()
  menghitung_ipk_dan_memberi_grade()
  hasil_akhir()

# run application
SemestersToIPK()
