
#CAPSTONE MODULE 1
#REYHAN NAUFALDY
#HYBE School of Idol

data_siswa = [ 
        {
        'SID': 2013001, 
        'Name': 'Kim Seokjin', 
        'Status': 'Inaktif',
        'Gender': 'Male', 
        'Singing': 95, 
        'Rapping': 80,
        'Dancing': 75
    },
    {
        'SID': 2013002, 
        'Name': 'Min Yoon-gi', 
        'Status': 'Inaktif',
        'Gender': 'Male', 
        'Singing': 85, 
        'Rapping': 95,
        'Dancing': 80
    },
    {
        'SID': 2013003, 
        'Name': 'Jung Hoseok', 
        'Status': 'Aktif',
        'Gender': 'Male', 
        'Singing': 80, 
        'Rapping': 90,
        'Dancing': 95
    },
    {
        'SID': 2013004, 
        'Name': 'Kim Namjoon', 
        'Status': 'Aktif',
        'Gender': 'Male', 
        'Singing': 85, 
        'Rapping': 95,
        'Dancing': 85
    },
    {
        'SID': 2013005, 
        'Name': 'Park Jimin', 
        'Status': 'Aktif',
        'Gender': 'Male', 
        'Singing': 90, 
        'Rapping': 85,
        'Dancing': 95
    },
    {
        'SID': 2013006, 
        'Name': 'Kim Taehyung', 
        'Status': 'Aktif',
        'Gender': 'Male', 
        'Singing': 95, 
        'Rapping': 80,
        'Dancing': 85
    },
    {
        'SID': 2013007, 
        'Name': 'Jeon Jungkook', 
        'Status': 'Inaktif',
        'Gender': 'Male', 
        'Singing': 90, 
        'Rapping': 85,
        'Dancing': 90
    },
    {
        'SID': 2022001, 
        'Name': 'Kim Garam', 
        'Status': 'Inaktif',
        'Gender': 'Female', 
        'Singing': 80, 
        'Rapping': 80,
        'Dancing': 90
    },
    {   
        'SID': 2022002, 
        'Name': 'Sakura Miyawaki', 
        'Status': 'Aktif',
        'Gender': 'Female', 
        'Singing': 50, 
        'Rapping': 65,
        'Dancing': 80
    },
    {
        'SID': 2022003, 
        'Name': 'Huh Yunjin', 
        'Status': 'Aktif',
        'Gender': 'Female', 
        'Singing': 95, 
        'Rapping': 90,
        'Dancing': 85
    },
    {   
        'SID': 2022004, 
        'Name': 'Hong Eunchae', 
        'Status': 'Aktif',
        'Gender': 'Female', 
        'Singing': 65, 
        'Rapping': 75,
        'Dancing': 80
    },
    {   
        'SID': 2022005, 
        'Name': 'Kim Chaewon', 
        'Status': 'Aktif',
        'Gender': 'Female', 
        'Singing': 85, 
        'Rapping': 85,
        'Dancing': 85
    },
    {   
        'SID': 2022006, 
        'Name': 'Kazuha Nakamura', 
        'Status': 'Aktif',
        'Gender': 'Female', 
        'Singing': 75, 
        'Rapping': 70,
        'Dancing': 90
    },
    {   
        'SID': 2022007, 
        'Name': 'Kim Minji', 
        'Status': 'Aktif',
        'Gender': 'Female', 
        'Singing': 85, 
        'Rapping': 85,
        'Dancing': 90
    },
    {   
        'SID': 2022008, 
        'Name': 'Hanni Pham', 
        'Status': 'Aktif',
        'Gender': 'Female', 
        'Singing': 90, 
        'Rapping': 90,
        'Dancing': 90
    },
    {   
        'SID': 2022009, 
        'Name': 'Danielle Marsh (Mo Ji-Hye)', 
        'Status': 'Aktif',
        'Gender': 'Female', 
        'Singing': 85, 
        'Rapping': 85,
        'Dancing': 90
    },
    {   
        'SID': 2022010, 
        'Name': 'Kang Haerin', 
        'Status': 'Aktif',
        'Gender': 'Female', 
        'Singing': 80, 
        'Rapping': 80,
        'Dancing': 85
    },
    {   
        'SID': 2022011, 
        'Name': 'Lee Hyein', 
        'Status': 'Inaktif',
        'Gender': 'Female', 
        'Singing': 88, 
        'Rapping': 90,
        'Dancing': 88
    }
     ]

data_siswa_update = data_siswa.copy()
SID = 0

#----------------------------------------------------------------------------------------------------------------------
#1: READ FUNCTION

def read_data():
    print('''
    --------------MENAMPILKAN DAFTAR NILAI SISWA-----------------

    1. Tampilkan Seluruh Daftar Nilai Siswa
    2. Tampilkan Daftar Nilai Siswa sesuai Student ID
    3. Kembali ke Main Menu
    ----------------------------------------------------
    ''')
    
    option_sub = input('    Input sub-menu (1-3): ')
    
    if option_sub == '1':
        if len(data_siswa) == 0:
            print('\n    *****Mohon maaf, data tidak ditemukan!*****')
            read_data()
        else:
            print('\n    Daftar Nilai Siswa:')
            for i, siswa in enumerate(data_siswa):
                print(f"\t{i + 1}. SID: {siswa['SID']}, Nama: {siswa['Name']}, Gender: {siswa['Gender']}, Status: {siswa['Status']}, Singing: {siswa['Singing']}, Rapping: {siswa['Rapping']}, Dancing: {siswa['Dancing']}")
            read_data()
    elif option_sub == '2':
        if len(data_siswa) == 0:
            print('\n    *****Data tidak ditemukan!*****')
            read_data()
        else:
            input_sid()
            for siswa in data_siswa:
                if siswa['SID'] == sid:
                    print(f"\n    Data siswa dengan Student ID {sid}:")
                    print(f"\tSID: {siswa['SID']}, Nama: {siswa['Name']}, Gender: {siswa['Gender']}, Status: {siswa['Status']}, Singing: {siswa['Singing']}, Rapping: {siswa['Rapping']}, Dancing: {siswa['Dancing']}")
                    break
            if siswa['SID'] != sid:
                print('\n    *****Data tidak ditemukan!*****')
            read_data()
    elif option_sub == '3':
        main_menu()
    else:
        print('\n    *****Mohon maaf, opsi yang anda input salah!*****')
        read_data()

# ----------------------------------------------------------------------------------------------------------------------
#2: CREATE FUNCTION
def create_data():
    print('''
    --------------MENAMBAHKAN DAFTAR NILAI SISWA---------------

    1. Menambahkan Data Siswa
    2. Kembali ke Main Menu
    ----------------------------------------------------
    ''')
    
    option_sub = input('    Input sub-menu (1-2): ')
    
    if option_sub == '1':
        sid = input('    Input SID siswa (7 digit): ')
        while len(sid) != 7 or not sid.isdigit():
            print('    *****SID harus 7 digit angka!*****')
            sid = input('    Input SID siswa (7 digit): ')
        sid = int(sid)

        # Cek apakah SID sudah ada di data_siswa
        if any(siswa['SID'] == sid for siswa in data_siswa):
            print('\n    *****SID telah terdapat di Daftar Nilai Siswa*****')
        else:
            nama = input('    Input nama siswa: ')
            while not all(word.isalpha() for word in nama.split()):
                print("    *****Nama tidak boleh kosong & harus alfabet!*****")
                nama = input("    Input nama siswa: ")
            
            nama_baru_splitted = nama.split()
            cap_nama_baru = [word.capitalize() for word in nama_baru_splitted]
            nama = " ".join(cap_nama_baru)
            
            status = input('    Input status siswa (Aktif, Inaktif): ').capitalize()
            while status not in ["Aktif", "Inaktif"]:
                print('    *****Status harus "Aktif" atau "Inaktif"!*****')
                status = input('    Input status siswa (Aktif, Inaktif): ').capitalize()
            
            gender = input('    Input jenis kelamin siswa (Male/Female): ').capitalize()
            while gender not in ['Male', 'Female']:
                print('    *****Jenis kelamin harus Male/Female!*****')
                gender = input('    Input jenis kelamin siswa (Male/Female): ').capitalize()
            
            singing = input('    Input nilai Singing (0-100): ')
            while not singing.isdigit() or not (0 <= int(singing) <= 100):
                print('    *****Nilai harus dalam bentuk digit & antara 0-100!*****')
                singing = input('    Input nilai Singing (0-100): ')
            singing = int(singing)

            rapping = input('    Input nilai Rapping (0-100): ')
            while not rapping.isdigit() or not (0 <= int(rapping) <= 100):
                print('    *****Nilai harus dalam bentuk digit & antara 0-100!*****')
                rapping = input('    Input nilai Rapping (0-100): ')
            rapping = int(rapping)

            dancing = input('    Input nilai Dancing (0-100): ')
            while not dancing.isdigit() or not (0 <= int(dancing) <= 100):
                print('    *****Nilai harus dalam bentuk digit & antara 0-100!*****')
                dancing = input('    Input nilai Dancing (0-100): ')
            dancing = int(dancing)

            option_save = input('\n    Apakah Anda yakin data akan disimpan? (Y/N): ').upper()

            if option_save == 'Y':
                data_siswa.append(
                {
                    'SID': sid, 
                    'Name': nama, 
                    'Status': status, 
                    'Gender': gender, 
                    'Singing': singing, 
                    'Rapping': rapping,
                    'Dancing': dancing
                })
                print('\n    *****Data tersimpan*****')
        create_data()
    elif option_sub == '2':
        main_menu()
    else:
        print('\n    *****Mohon maaf, opsi yang anda input salah!*****')
        create_data()

#----------------------------------------------------------------------------------------------------------------------
#3: UPDATE FUNCTION
def update_data():
    print('''
    --------------MENGUBAH DATA NILAI SISWA---------------

    1. Mengubah Nilai Siswa
    2. Kembali ke Main Menu
    ----------------------------------------------------
    ''')
    
    option_sub = input('    Input sub-menu (1-2): ')
    
    if option_sub == '1':
        input_sid()
        sid_initial = sid
        temp = ''
        for siswa in data_siswa:
            if siswa['SID'] == sid_initial:
                print(f"\tSID: {siswa['SID']}, Nama: {siswa['Name']}, Gender: {siswa['Gender']}, Status: {siswa['Status']}, Singing: {siswa['Singing']}, Rapping: {siswa['Rapping']}, Dancing: {siswa['Dancing']}")
                
                option_continue = input('\n    Apakah akan melanjutkan update data? (Y/N): ').upper()
                if option_continue == 'Y':
                    temp = input('    Input kolom yang akan diupdate [Student ID, Name, Gender, Status, Singing, Rapping, Dancing]: ').capitalize()
                    if temp in siswa:
                        nomor_baru = input(f'    Input {temp} yang baru: ')
                        if temp == 'Gender':
                            while nomor_baru.capitalize() not in ['Male', 'Female']:
                                print('    *****Jenis kelamin harus "Male" atau "Female"!*****')
                                nomor_baru = input(f'    Input {temp} yang baru: ').capitalize()
                        elif temp == 'Status':
                            while nomor_baru.capitalize() not in ['Aktif', 'Inaktif']:
                                print('    *****Status harus "Aktif" atau "Inaktif"!*****')
                                nomor_baru = input(f'    Input {temp} yang baru: ').capitalize()
                        elif temp in ['Singing', 'Rapping', 'Dancing']:
                            while not nomor_baru.isdigit() or not (0 <= int(nomor_baru) <= 100):
                                print('    *****Nilai harus dalam bentuk digit & antara 0-100!*****')
                                nomor_baru = input(f'    Input {temp} yang baru: ')
                            nomor_baru = int(nomor_baru)
                        siswa[temp] = nomor_baru
                        print('\n    *****Data berhasil diupdate*****')
                    else:
                        print('    *****Kolom yang Anda input tidak ada!*****')
                break
        else:
            print('\n    *****Data tidak ditemukan!*****')
        update_data()
    elif option_sub == '2':
        main_menu()
    else:
        print('\n    *****Mohon maaf, opsi yang anda input salah!*****')
        update_data()
# ----------------------------------------------------------------------------------------------------------------------
#4: DELETE FUNCTION

def delete_data():
    print('''
    --------------MENGHAPUS DATA SISWA---------------

    1. Menghapus Data Siswa
    2. Kembali ke Main Menu
    ----------------------------------------------------
    ''')
    
    option_sub = input('    Input sub-menu (1-2): ')
    
    if option_sub == '1':
        input_sid()
        for index, siswa in enumerate(data_siswa):
            if siswa['SID'] == sid:
                option_delete = input(f'\n    Apakah Anda yakin data dengan SID {sid} akan dihapus? (Y/N): ').upper()
                if option_delete == 'Y':
                    data_siswa.pop(index)
                    print('    *****Data Terhapus*****')
                break
        else:
            print('\n    *****Data tidak ditemukan!*****')
        delete_data()
    elif option_sub == '2':
        main_menu()
    else:
        print('\n    *****Mohon maaf, opsi yang anda input salah!*****')
        delete_data()

# ----------------------------------------------------------------------------------------------------------------------
#REPEAT GLOBAL FUNCTION
def input_sid():
    global sid
    sid = input('    Input Student ID (7 digit): ')
    while len(sid) != 7 or not sid.isdigit():
        print('    *****SID harus 7 digit angka!*****')
        sid = input('    Input Student ID (7 digit): ')
    sid = int(sid)

#6: MAIN MENU

def main_menu():
    print('''
    -------------------------WELCOME TO-----------------------
    -----------HYBE Entertainment School of Idols-------------   
    --------------SISTEM PENGELOLAAN DATA SISWA---------------

    1. Memperlihatkan Data Siswa
    2. Menambah Data Siswa
    3. Mengubah Data Siswa
    4. Menghapus Data Siswa
    5. Exit
    ----------------------------------------------------
    ''')
    
    option = input('    Input sub-menu (1-5): ')
    
    if option == '1':
        read_data()
    elif option == '2':
        create_data()
    elif option == '3':
        update_data()
    elif option == '4':
        delete_data()
    elif option == '5':
        print('\n    *****Terima kasih telah menggunakan sistem pengelolaan nilai siswa!*****')
    else:
        print('\n    *****Mohon maaf, opsi yang anda input salah!*****')
        main_menu()

# Mulai program
main_menu()
