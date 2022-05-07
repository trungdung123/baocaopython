# Phạm Trung Dũng
# B19DCCN130
# phamtrungdungasao@gmail.com
# 26/08/1993
# 0346954929

import re
import random as rd
songs_name = ['Hà Nội mùa thu', 'Chân tình', 'Không thể và có thể', 'Không giờ rồi', 'Tiến quân ca',
              'Thôi đừng chiêm bao', 'Linh hồn tượng đá', 'Mang tiền về cho mẹ', 'Hai triệu năm', 'Gõ cửa trái tim']
categories = ['tiền chiến', 'nhạc trẻ', 'rap',
              'cách mạng', 'trữ tình', 'bolero', 'vpop']
singers = ['Trọng Tấn', 'Mỹ Linh', 'Đăng Dương', 'Việt Hoàn', 'Sơn Tùng',
           'Lệ Quyên', 'Đan Nguyên', 'Đen Vâu', 'Hồ Ngọc Hà', 'Mỹ Tâm', 'Quang Lê']


def chuan_hoa_xau_B19DCCN130(string: str) -> str:
    string = re.sub(r'\s\s+', ' ', string.strip()) #Thay thế tất cả khoang trắng thành 1 khoảng trắng duy nhất 
    return string


def Pham_Trung_Dung_chon_ngau_nhien(list: list, number: int = 1) -> list:
    return rd.sample(list, number)


class BaiHat:
    def __init__(self, maBH, tenBH, caSyTheHien, theLoai, danhGia) -> None:
        self.maBH = "BH%03d" % maBH
        self.tenBH = chuan_hoa_xau_B19DCCN130(tenBH)
        self.caSyTheHien = caSyTheHien
        self.theLoai = theLoai
        self.danhGia = danhGia
    # kiểm tra tên ca sĩ có trong danh sách không
    
    def DaDuocTheHien(self, tenCaSy: str) -> bool:
        tenCaSy = chuan_hoa_xau_B19DCCN130(tenCaSy)
        return (tenCaSy in self.caSyTheHien)



# câu a
list_BH = []
for maBH in range(10):
    baihat = BaiHat(maBH+1, rd.choice(songs_name), Pham_Trung_Dung_chon_ngau_nhien(singers, rd.randint(1, 5)),
                    Pham_Trung_Dung_chon_ngau_nhien(categories, rd.randint(1, 5)), rd.randint(1, 6))
    list_BH.append(baihat)
    # choice trọn 1 bài hát trong ds

# câu b
print("câu b")
for baihat in list_BH:
    list_CaSyTheHien = ",".join(baihat.caSyTheHien)
    list_TheLoai = ",".join(baihat.theLoai)# chuyển 1 danh sách hoặc 1 mảng thành chuỗi 
    print(f"{baihat.maBH} - {baihat.tenBH} - {list_CaSyTheHien} - {list_TheLoai}")

# câu c
print("câu c")
tenCaSy=input()
result=[]
for baihat in list_BH:
    if baihat.DaDuocTheHien(tenCaSy):
        result.append(baihat)
result.sort(key=lambda x:x.danhGia)# sort sắp xếp mảng theo đánh giá tăng dần 
for baihat in result:
    list_CaSyTheHien = ",".join(baihat.caSyTheHien)
    print(f"{baihat.tenBH} - {list_CaSyTheHien} - {baihat.danhGia}")