from guizero import *

nhom = ["Kim loại kiềm", "Kim loại kiềm thổ", "Lanthan", "Actini", "Kim loại chuyển tiếp", "Kim loại yếu", "Á kim", "Phi kim", "Halogen", "Khí hiếm"]
app = App("guizero", width = 500, height = 500)

box = Box(app, layout = "grid")

window = None # cửa sổ hiển thị thông tin nguyên tố
ds_nguyen_tu = [] # danh sách chứa tất cả nguyên tố
tat_ca_button = []# ds chứa các nút nguyên tố

x= 0
y =0

with open(r'nguyento.txt') as file: # mở file txt để lấy thông tin
    lines = file.readlines()
    
    for line in lines: # chia thông tin
        split_data = line.split("|")

        # đặt biến cho từng thông tin
        stt = split_data[0].strip() # số thứ tự
        ki_hieu = split_data[1].strip() # kí hiệu hóa học
        ten = split_data[2].strip() # tên nguyên tố
        ntk = split_data[3].strip() # nguyên tử khối
        hoatri = split_data[4].strip() # hóa trị

        # lưu nguyên tố dưới dạng dictionary
        nguyen_tu = {
            "stt": stt,
            "ki_hieu" : ki_hieu,
            "ten": ten,
            "ntk": ntk,
            "hoatri": hoatri
        }
        ds_nguyen_tu.append(nguyen_tu) # bỏ vào 1 list

# lọc theo nhóm nguyên tố
def loc_nhom(ten_nhom):
    # Xác định xem có nên hiện chữ L và A không
    L.visible = (ten_nhom == "lanthan")
    A.visible = (ten_nhom == "actini")
    
    for button in tat_ca_button:
        if hasattr(button, 'nhom') and button.nhom != "chuthich_trangthai":
            # Nếu đúng nhóm thì hiện, sai thì ẩn
            if button.nhom == ten_nhom:
                button.visible = True
                L.visible = False
                A.visible = False
            if button.nhom == ten_nhom:
                L.visible = True
            else:
                button.visible = False
                L.visible = False
                A.visible = False

# hiện lại toàn bộ nguyên tố
def hien_tat_ca():
    for button in tat_ca_button:
        button.visible = True
        L.visible = True
        A.visible = True

# hàm hiển thị thông tin nguyên tố khi bấm nút
def hien_thi(stt, ki_hieu, ten, ntk, hoatri): # tạo một hàm với các thông tin đc cung cấp
    global window
    if window:
        window.destroy()
    window = Window(app) # tạo cửa sổ mới để hiển thị thông tin

    # thông tin cần hiển thị
    Text(window,f"STT: {stt}", size = 20)
    Text(window,f"Kí hiệu: {ki_hieu}", size = 20)
    Text(window,f"Tên: {ten}", size = 20)
    Text(window,f"Nguyên tử khối: {ntk}", size = 20)
    Text(window,f"Hóa trị: {hoatri}", size = 20)

# khu phân loại và chỗ chứa màu
# phân loại các nhóm nguyên tố + màu tương ứng
klk = [2, 10, 18, 36, 54, 86]
mau1 = "#F74420"
klkt = [3, 11, 19, 37, 55, 87]
mau2 = "#FFD580"
phikim = [0, 5, 6, 7, 14, 15, 33]
mau3 = "#AAFF00"
kimloaichuyentiep = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 56, 88, 71, 72, 73 ,74, 75, 76, 77, 78, 79, 103, 104, 105, 106, 107, 108, 109, 110, 111]
mau4 = "#FA8072"
Actini = ["**", 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102]
mau5 = "#FF69B4"
Lanthan = ["*", 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70]
mau6 = "#FF8AFF"
kimloaiyeu = [12, 30, 48, 49, 80, 81, 82, 112, 113, 114, 115]
mau7 = "#A9A9A9"
akim = [4, 13, 31, 32, 50, 51, 83]
mau8 = "#8A9A5B"
halogen = [8, 16, 34, 52, 84, 116]
mau9 = "#FFFF8F"
khihiem = [1, 9, 17, 35, 53, 85, 117]
mau10 = "#00FFFF"

# phân loại trạng thái
khi = [0, 1, 6, 7, 8, 9, 16, 17, 35, 53, 85]
chu1 = "#FF0000"
long = [34, 79, 111]
chu2 = "#008000"

pt = [0, 2, 10, 18, 36, 54, 86] # các nguyên tố nằm ở cột đầu tiên của bảng tuần hoàn
for i in pt: # cho biến i trong list để lấy từng thông tin 
    # lấy thông tin nguyên tố từ danh sách
    stt = ds_nguyen_tu[i]['stt']
    ki_hieu = ds_nguyen_tu[i]['ki_hieu']
    ten = ds_nguyen_tu[i]["ten"]
    ntk = ds_nguyen_tu[i]['ntk']
    hoatri = ds_nguyen_tu[i]['hoatri']
    # tạo button hiển thị nguyên tố
    button = PushButton(
        box, 
        text = ki_hieu, 
        command = hien_thi, # khi bấm sẽ hiện thông tin
        args = [stt, ki_hieu, ten, ntk, hoatri], 
        grid = [x,y], # cùng 1 cột, khác hàng
        width = 4, 
        height = 1)
    button.text_size = 15
    tat_ca_button.append(button) # lưu lại để lọc nhóm sau này
    y += 1 # xuống hàng tiếp theo
    # dùng điều kiện if - else để phân loại
    if i in klk:
        button.bg = mau1
        button.nhom = "kim_loai_kiem"
    elif i in phikim:
        button.bg = mau3
        button.nhom = "phi_kim"
    if i in khi:
        button.text_color = chu1

pt = [3, 11, 19, 37, 55, 87]
y = 1 # hàng 2
x = 1 # cột 2
for i in pt:
    stt = ds_nguyen_tu[i]['stt']
    ki_hieu = ds_nguyen_tu[i]['ki_hieu']
    ten = ds_nguyen_tu[i]["ten"]
    ntk = ds_nguyen_tu[i]['ntk']
    hoatri = ds_nguyen_tu[i]['hoatri']
    button = PushButton(
        box, 
        text = ki_hieu, 
        command = hien_thi, 
        args = [stt, ki_hieu, ten, ntk, hoatri], 
        grid = [x,y],
        width = 4, 
        height = 1)
    button.text_size = 15
    tat_ca_button.append(button)
    y += 1 # xuống hàng
    if i in klkt:
        button.bg = mau2
        button.nhom = "kiem_tho"

pt = [20, 38, "*", "**", 21, 39, 71, 103, 22, 40, 72, 104, 23, 41, 73, 105, 24, 42, 74, 106, 25,
43, 75, 107, 26, 44, 76, 108, 27, 45, 77, 109, 28, 46, 78, 110, 29, 47, 79, 111]
y = 3
x = 2
for i in pt:
    # dùng điều kiện if - else để phân loại trường hợp đặc biệt
    if i == "*":
        stt = "57~71"
        ki_hieu = "L"
        ten = "Lant"
        ntk = "không"
        hoatri = "không"
        button = PushButton(
            box, 
            text = ki_hieu, 
            command = hien_thi, 
            args = [stt, ki_hieu, ten, ntk, hoatri], 
            grid = [x,y],
            width = 4, 
            height = 1)
        tat_ca_button.append(button)
        button.nhom = "lanthan"
        button.text_size = 15
        y += 1
    elif i == "**":
        stt = "89~103"
        ki_hieu = "A"
        ten = "Actinit"
        ntk = "không"
        hoatri = "không"
        button = PushButton(
            box, 
            text = ki_hieu, 
            command = hien_thi,
            args = [stt, ki_hieu, ten, ntk, hoatri], 
            grid = [x,y],
            width = 4, 
            height = 1)
        tat_ca_button.append(button)
        button.nhom = "actini"
        button.text_size = 15
        y += 1
    else:
        stt = ds_nguyen_tu[i]['stt']
        ki_hieu = ds_nguyen_tu[i]['ki_hieu']
        ten = ds_nguyen_tu[i]["ten"]
        ntk = ds_nguyen_tu[i]['ntk']
        hoatri = ds_nguyen_tu[i]['hoatri']
        button = PushButton(
            box, 
            text = ki_hieu, 
            command = hien_thi, 
            args = [stt, ki_hieu, ten, ntk, hoatri],
            grid = [x,y],
            width = 4, height = 1)
        button.text_size = 15
        tat_ca_button.append(button)
        y+=1
    if y >= 7:
        y = 3
        x += 1
    if i in kimloaichuyentiep:
        button.bg = mau4
        button.nhom = "chuyen_tiep"
    elif i in Actini:
        button.bg = mau5
        button.nhom = "actini"
    elif i in Lanthan:
        button.bg = mau6
        button.nhom = "lanthan"
    if i in long:
        button.text_color = chu2

pt = [4, 12, 30, 48, 80, 112, 5, 13, 31, 49, 81, 113, 6, 14, 32, 50, 82, 114, 7, 15, 33, 51, 83, 
115, 8, 16, 34, 52, 84, 116]
y = 1
for i in pt:
    stt = ds_nguyen_tu[i]['stt']
    ki_hieu = ds_nguyen_tu[i]['ki_hieu']
    ten = ds_nguyen_tu[i]["ten"]
    ntk = ds_nguyen_tu[i]['ntk']
    hoatri = ds_nguyen_tu[i]['hoatri']
    button = PushButton(
        box, 
        text = ki_hieu, command = hien_thi, 
        args = [stt, ki_hieu, ten, ntk, hoatri],
        grid = [x,y],
        width = 4, 
        height = 1)
    button.text_size = 15
    tat_ca_button.append(button)
    y += 1 
    if y >= 7:
        y = 1
        x += 1
    if i in phikim:
        button.bg = mau3
        button.nhom = "phi_kim"
    elif i in kimloaiyeu:
        button.bg = mau7
        button.nhom = "kim_loai_yeu"
    elif i in akim:
        button.bg = mau8
        button.nhom = "a_kim"
    elif i in halogen:
        button.bg = mau9
        button.nhom = "halogen"
    if i in khi:
        button.text_color = chu1
    elif i in long:
        button.text_color = chu2

pt = [1, 9, 17, 35, 53, 85, 117]
y = 0
for i in pt:
    stt = ds_nguyen_tu[i]['stt']
    ki_hieu = ds_nguyen_tu[i]['ki_hieu']
    ten = ds_nguyen_tu[i]["ten"]
    ntk = ds_nguyen_tu[i]['ntk']
    hoatri = ds_nguyen_tu[i]['hoatri']
    button = PushButton(
        box, 
        text = ki_hieu, 
        command = hien_thi, 
        args = [stt, ki_hieu, ten, ntk, hoatri], 
        grid = [x,y],
        width = 4, 
        height = 1)
    button.text_size = 15
    tat_ca_button.append(button)
    y += 1
    if i in khihiem:
        button.bg = mau10
        button.nhom = "khi_hiem"
    if i in khi:
        button.text_color = chu1

# tạo 1 box trống nhằm tạo khoảng trống
space = Box(box, layout = "grid", grid = [1,7], width = 1, height = 50)
pt = [56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 88, 89, 90, 91, 92, 93, 94, 95,
    96, 97, 98, 99, 100, 101, 102]
y = 8
x = 3
# tạo chữ để chú thích
L = Text(box, text = "L", grid = [2,8], size = 15)
A = Text(box, text = "A", grid = [2,9], size = 15)

for i in pt:
    stt = ds_nguyen_tu[i]['stt']
    ki_hieu = ds_nguyen_tu[i]['ki_hieu']
    ten = ds_nguyen_tu[i]["ten"]
    ntk = ds_nguyen_tu[i]['ntk']
    hoatri = ds_nguyen_tu[i]['hoatri']
    button = PushButton(
        box, 
        text = ki_hieu, 
        command = hien_thi, 
        args = [stt, ki_hieu, ten, ntk, hoatri], 
        grid = [x,y], 
        width = 4,
        height = 1)
    button.text_size = 15
    tat_ca_button.append(button)
    x += 1 # sang phải
    if x >= 18: # đủ hàng thì xuống dòng
        x = 3
        y += 1
    if i in kimloaichuyentiep:
        button.bg = mau4
        button.nhom = "chuyen_tiep"
    elif i in Actini:
        button.bg = mau5
        button.nhom = "actini"
    elif i in Lanthan:
        button.bg = mau6
        button.nhom = "lanthan"

# Tạo chú thích cho dễ hiểu
chuthich = Box(app, layout="grid")

Text(chuthich, text = "Chú thích: ", size = 20, grid = [0,0])
Text(chuthich, text = "Trạng thái: ", size = 18, grid = [0,1])

the_chat = ["Đen = Rắn", "Đỏ = Khí", "Lục = Lỏng"]
for idx, item in enumerate(the_chat):
    btn = PushButton(chuthich, text = item, grid = [idx + 1, 1], width = 10)
    btn.text_size = 14
    btn.nhom = "chuthich_trangthai" 
    tat_ca_button.append(btn)
    if item == "Đỏ = Khí": btn.text_color = chu1
    elif item == "Lục = Lỏng": btn.text_color = chu2

# Đưa từ điển ra ngoài vòng lặp để tối ưu
nhom_lookup = {
    "Kim loại kiềm": "kim_loai_kiem",
    "Kim loại kiềm thổ": "kiem_tho",
    "Lanthan": "lanthan",
    "Actini": "actini",
    "Kim loại chuyển tiếp": "chuyen_tiep",
    "Kim loại yếu": "kim_loai_yeu",
    "Á kim": "a_kim",
    "Phi kim": "phi_kim",
    "Halogen": "halogen",
    "Khí hiếm": "khi_hiem"
}

x_coord = 1
y_coord = 2
for ten_tieng_viet in nhom:
    ma_nhom = nhom_lookup[ten_tieng_viet]
    btn_nhom = PushButton(
        chuthich,
        text = ten_tieng_viet,
        grid = [x_coord, y_coord],
        width = 15,
        command = loc_nhom,
        args = [ma_nhom]
    )
    btn_nhom.text_size = 13
    btn_nhom.nhom = "nut_chuc_nang" # Tránh bị ẩn khi lọc

    # Gán màu cho nút lọc (giống màu nguyên tố)
    if ten_tieng_viet == "Kim loại kiềm": btn_nhom.bg = mau1
    elif ten_tieng_viet == "Kim loại kiềm thổ": btn_nhom.bg = mau2
    elif ten_tieng_viet == "Lanthan": btn_nhom.bg = mau6
    elif ten_tieng_viet == "Actini": btn_nhom.bg = mau5
    elif ten_tieng_viet == "Kim loại chuyển tiếp": btn_nhom.bg = mau4
    elif ten_tieng_viet == "Kim loại yếu": btn_nhom.bg = mau7
    elif ten_tieng_viet == "Á kim": btn_nhom.bg = mau8
    elif ten_tieng_viet == "Phi kim": btn_nhom.bg = mau3
    elif ten_tieng_viet == "Halogen": btn_nhom.bg = mau9
    elif ten_tieng_viet == "Khí hiếm": btn_nhom.bg = mau10

    x_coord += 1
    if x_coord >= 6:
        x_coord = 1
        y_coord += 1

Text(chuthich, text = "Các nhóm cùng gốc trong bảng tuần hoàn: ", size = 20, grid = [0,2])

# Nút hiện tất cả
nut_reset = PushButton(chuthich, text="Hiện tất cả", grid=[0, 3], width=15, command=hien_tat_ca)
nut_reset.text_size = 14
nut_reset.bg = "white"



app.display()