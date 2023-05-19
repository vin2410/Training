class TaiLieu:
    def __init__(self, ma_tai_lieu, ten_tai_lieu, ten_nha_xuat_ban, so_ban_phat_hanh):
        self.ma_tai_lieu = ma_tai_lieu
        self.ten_tai_lieu = ten_tai_lieu
        self.ten_nha_xuat_ban = ten_nha_xuat_ban
        self.so_ban_phat_hanh = so_ban_phat_hanh

    def in_tai_lieu(self):
        print("Mã tài liệu:", self.ma_tai_lieu)
        print("Tên tài liệu:", self.ten_tai_lieu)
        print("Tên nhà xuất bản:", self.ten_nha_xuat_ban)
        print("Số bản phát hành:", self.so_ban_phat_hanh)

class Sach(TaiLieu):
    def __init__(self, ma_tai_lieu, ten_tai_lieu, ten_nha_xuat_ban, so_ban_phat_hanh, ten_tac_gia, so_trang):
        TaiLieu.__init__(self, ma_tai_lieu, ten_tai_lieu, ten_nha_xuat_ban, so_ban_phat_hanh)
        self.ten_tac_gia = ten_tac_gia
        self.so_trang = so_trang

    def in_tai_lieu(self):
        TaiLieu.in_tai_lieu(self)
        print("Tên tác giả:", self.ten_tac_gia)
        print("Số trang:", self.so_trang)

class TapChi(TaiLieu):
    def __init__(self, ma_tai_lieu, ten_tai_lieu, ten_nha_xuat_ban, so_ban_phat_hanh, so_phat_hanh, thang_phat_hanh):
        TaiLieu.__init__(self, ma_tai_lieu, ten_tai_lieu, ten_nha_xuat_ban, so_ban_phat_hanh)
        self.so_phat_hanh = so_phat_hanh
        self.thang_phat_hanh = thang_phat_hanh

    def in_tai_lieu(self):
        TaiLieu.in_tai_lieu(self)
        print("Số phát hành:", self.so_phat_hanh)
        print("Tháng phát hành:", self.thang_phat_hanh)

class Bao(TaiLieu):
    def __init__(self, ma_tai_lieu, ten_tai_lieu, ten_nha_xuat_ban, so_ban_phat_hanh, ngay_phat_hanh):
        TaiLieu.__init__(self, ma_tai_lieu, ten_tai_lieu, ten_nha_xuat_ban, so_ban_phat_hanh)
        self.ngay_phat_hanh = ngay_phat_hanh

    def in_tai_lieu(self):
        TaiLieu.in_tai_lieu(self)
        print("Ngày phát hành:", self.ngay_phat_hanh)

class QuanLyTaiLieu:
    def __init__(self):
        self.danh_sach_tai_lieu = []

    def them_tai_lieu(self, tai_lieu):
        self.danh_sach_tai_lieu.append(tai_lieu)

    def xoa_tai_lieu(self, ma_tai_lieu):
        for tai_lieu in self.danh_sach_tai_lieu:
            if tai_lieu.ma_tai_lieu == ma_tai_lieu:
                self.danh_sach_tai_lieu.remove(tai_lieu)
                return True
        return False

    def tim_kiem_tai_lieu(self, ma_tai_lieu):
        for tai_lieu in self.danh_sach_tai_lieu:
            print(tai_lieu)
