import os

def show_data():
    try:
        data_file = open('transaksi.txt', 'r')
        id = data_file.readline()
        while id != '':
            nomor = data_file.readline()
            nama = data_file.readline()
            quantity = data_file.readline()
            harga = data_file.readline()
            sub_tot = data_file.readline()

            id = id.rstrip('\n')
            nomor = nomor.rstrip('\n')
            nama = nama.rstrip('\n')
            quantity = quantity.rstrip('\n')
            harga = harga.rstrip('\n')
            sub_tot = sub_tot.rstrip('\n')

    
            print('ID : ', id)
            print('Nomor Transaksi : TRX-',id)
            print('Nama produk : ', nama)
            print('Qty : ', quantity)
            print('Harga : ', harga)
            print('Subtotal : ', sub_tot)

            total += int(sub_tot)

            id = data_file.readline()
        data_file.close()
        print()
        print('Total keseluruhan : ', total)
    except FileNotFoundError:
        print("File transaksi.txt tidak ditemukan.")

    except IOError as e:
        print(f"Terjadi kesalahan saat mengakses file: {e}")

    except Exception as e:
        print(f"Terjadi kesalahan yang tidak terduga: {e}")

def input_data():
    try:
        another = 'y'
        data_file = open('transaksi.txt', 'a')
        while another == 'y' or another == 'Y':
            print('Silahkan masukkan data transaksi!')
            id = input('ID Transaksi : ')
            nomor = input('Nomor Transaksi : ')
            nama = input("Nama produk : ")
            quantity = int(input("Quantity : "))
            harga = int(input("Harga : "))
            sub_tot = harga * quantity

            data_file.write(id + '\n')
            data_file.write(nomor + '\n')
            data_file.write(nama + '\n')
            data_file.write(str(quantity) + '\n')
            data_file.write(str(harga) + '\n')
            data_file.write(str(sub_tot) + '\n')
            print('Apakah anda ingin menambahkan data lain?')
            another = input('Y = ya, lainnya = tidak : ')
        data_file.close()
        print('Data berhasil ditambahkan!')

    except FileNotFoundError:
        print("File transaksi.txt tidak ditemukan.")

    except IOError as e:
        print(f"Terjadi kesalahan saat mengakses file: {e}")

    except Exception as e:
        print(f"Terjadi kesalahan yang tidak terduga: {e}")
            

def edit_data():
    try:
        found = False
        print("Silahkan edit Data Transaksi!")
        cari = input('Silahkan masukkan nomor transaksi : ')
        data_file = open('transaksi.txt', 'r')
        temp_file = open('temp.txt', 'w')
        id = data_file.readline()
        while id != '':
            nomor = data_file.readline()
            nama = data_file.readline()
            quantity = data_file.readline()
            harga = data_file.readline()
            sub_tot = data_file.readline()

            id = id.rstrip('\n')
            nomor = nomor.rstrip('\n')
            nama = nama.rstrip('\n')
            quantity = quantity.rstrip('\n')
            harga = harga.rstrip('\n')
            sub_tot = sub_tot.rstrip('\n')

            if nomor == cari:
                print('ID : ', id)
                print('Nomor Transaksi : TRX-',id)
                print('Nama produk : ', nama)
                print('Qty : ', quantity)
                print('Harga : ', harga)
                print('Subtotal : ', sub_tot)
                print("")

                new_product = input("Nama baru dari produk : ")
                new_quantity = int(input("Masukkan quantity baru : "))
                new_price = int(input("Masukkan harga terbaru : "))
                new_sub_tot = new_price * new_quantity

                temp_file.write(id + '\n')
                temp_file.write(nomor + '\n')
                temp_file.write(new_product + '\n')
                temp_file.write(str(new_quantity) + '\n')
                temp_file.write(str(new_price) + '\n')
                temp_file.write(str(new_sub_tot) + '\n')
                found = True
            else:
                temp_file.write(id + '\n')
                temp_file.write(nomor + '\n')
                temp_file.write(new_product + '\n')
                temp_file.write(str(new_quantity) + '\n')
                temp_file.write(str(new_price) + '\n')
                temp_file.write(str(new_sub_tot) + '\n')
            id = data_file.readline()
        data_file.close()
        temp_file.close()
        os.remove('transaksi.txt')
        os.rename('temp.txt', 'transaksi.txt')
        if found:
            print('File telah diperbaharui.')
        else:
            print('Karyawan tersebut tidak ditemukan dalam file.')
    except FileNotFoundError:
        print("File transaksi.txt tidak ditemukan.")
    except IOError as e:
        print(f"Terjadi kesalahan saat mengakses file: {e}")
    except Exception as e:
        print(f"Terjadi kesalahan yang tidak terduga: {e}")

def delete_data():
    try:
        found = False
        cari = input('Silahkan masukkan nomor transaksi : ')
        data_file = open('transaksi.txt', 'r')
        temp_file = open('temp.txt', 'w')
        id = data_file.readline()
        while id != '':
            nomor = data_file.readline()
            nama = data_file.readline()
            quantity = data_file.readline()
            harga = data_file.readline()
            sub_tot = data_file.readline()

            id = id.rstrip('\n')
            nomor = nomor.rstrip('\n')
            nama = nama.rstrip('\n')
            quantity = quantity.rstrip('\n')
            harga = harga.rstrip('\n')
            sub_tot = sub_tot.rstrip('\n')

            if nomor != cari:
                temp_file.write(id + '\n')
                temp_file.write(nomor + '\n')
                temp_file.write(nama + '\n')
                temp_file.write(str(quantity) + '\n')
                temp_file.write(str(harga) + '\n')
                temp_file.write(str(sub_tot) + '\n')
            else:
                print('ID : ', id)
                print('Nomor Transaksi : TRX-',id)
                print('Nama produk : ', nama)
                print('Qty : ', quantity)
                print('Harga : ', harga)
                print('Subtotal : ', sub_tot)
                print("")
                found = True
            id = data_file.readline()
        data_file.close()
        temp_file.close()
        os.remove('transaksi.txt')
        os.rename('temp.txt', 'transaksi.txt')
        if found:
            print("File telah ditemukan!")
        else:
            print("Produk yang anda cari tidak ada di dalam data!")
    except FileNotFoundError:
        print('File transaksi.txt tidak ditemukan.')
    except IOError as e:
        print(f"Terjadi kesalahan saat mengakses file: {e}")
    except Exception as e:
        print(f"Terjadi kesalahan yang tidak terduga: {e}")

def main():
    while True:
        print("=========================")
        print('Aplikasi Transaksi Kasir')
        print("=========================")
        print('1. Data Transaksi Penjualan')
        print('2. Input data baru')
        print('3. Edit Data Transaksi')
        print('4. Delete Data Transaksi')
        print('5. Keluar')
        choice = input('Masukkan pilihan Anda: ')
        try:
            if choice == '1':
                show_data()
            elif choice == '2':
                input_data()
            elif choice == '3':
                edit_data()
            elif choice == '4':
                delete_data()
            elif choice == '5':
                print("Anda telah keluar....")
                break
            else:
                print('Pilihan tidak valid. Silahkan coba lagi.')
        except Exception as e:
            print(f"Terjadi kesalahan yang tidak terduga: {e}")

main()