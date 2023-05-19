from Opp_library import TaiLieu

ds_tailieu = []

while True:
    print(f'''\n
    0. Thoát Chương trình
    1. Thêm Tài liệu
    2. Cập nhật thông tin tài liệu
    3. Xóa tài liệu
    4. Xem thông tin tất cả tài liệu
    5. Xem Thông tin tài liệu
    6. Tìm tài liệu theo tên
    7. Số lượng tài liệu
    ''')
    select = input("Mời chọn chức năng:  ")

    if str(select).isdigit():
        select = int(select)
        if select == 0:
            break
        elif select == 1:
            ma_tai_lieu = input("Nhập mã tài liệu:  ")
            ten_tai_lieu = input("Nhập Tên tài liệu:  ")
            tl = TaiLieu(ma_tai_lieu , ten_tai_lieu)
            ds_tailieu.append(tl)

        elif select == 2:
            ma_tai_lieu = input("Nhập mã tài liệu bạn cần sửa :  ")
            for i in ds_tailieu:
                if i.get_id() == ma_tai_lieu:
                    i.set_Name( input("Nhập vào tên mới:  ") )
                    i.show_info()

        elif select == 4:
            if len(ds_tailieu) == 0:
                print("\n Thư viện hiện đang trống . Bạn vui lòng thêm sinh viên mói vào danh sách !")
            else:
                print(f"\nHiện có {len(ds_tailieu)} Tài liệu ")
                for i in ds_tailieu:
                    i.show_info()

        elif select == 3:
            ma_tai_lieu = input("Nhập mã tài liệu cần xóa :  ")
            for i in ds_tailieu:
                if i.get_id() == ma_tai_lieu:
                    ds_tailieu.remove(i)
                    print("Bạn đã xóa 1 tài liệu thành công ")
                    continue

        elif select == 5:
            ma_tai_lieu = input("Nhập mã tài liệu cần xem thông tin :  ")
            for i in ds_tailieu:
                if i.get_id() == ma_tai_lieu:
                    i.show_info()
                    continue

        elif select == 6:
            ten_tai_lieu = input("Nhập Tên Tài liệu cần tìm :  ")
            for i in ds_tailieu:
                if i.get_Name() == ten_tai_lieu:
                    i.show_info()

        elif select == 7:
            print(f"\nHiện có { len(ds_tailieu) } Tài liệu \n")
    else:
        print("\nBạn phải nhập số. Vui Lòng nhập lại !")