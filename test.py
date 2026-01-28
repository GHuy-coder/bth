# from guizero import *
# from PIL import Image
# import os

# app = App("guizero", width=500, height=500)

# box = Box(app, layout="grid")

# window = None
# ds_nguyen_tu = []
# all_button = {}
# nhom = ["Kim loại kiềm", "Kim loại kiềm thổ", "Lanthan", "Actini", "Kim loại chuyển tiếp", "Kim loại yếu", "Á kim", "Phi kim", "Halogen", "Khí hiếm"]
# pt1 = ['3', '11', '19', '37', '55', '87']
# pt2 = ['4', '12', '20', '38', '56', '88']
# pt3 = ['58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71']
# pt4 = ['90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103']
# pt5 = ['21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '72', '73', '74', '75', '76', '77', '78', '79', '80', '104', '105', '106', '107', '108', '109', '110', '111', '112', '57', '89']
# pt6 = ['13', '31', '49', '50', '81', '82', '83', '113', '114', '115', '116']
# pt7 = ['5', '14', '32', '33', '51', '52', '84']
# pt8 = ['1', '6', '7', '8', '15', '16', '34']
# pt9 = ['9', '17', '35', '53', '85', '117']
# pt10 = ['2', '10', '18', '36', '54', '86', '118']
# img = []

# count = 1

# x= 0
# y =0

# for f in os.listdir("bangtuanhoan_anh"):
#     img.append(f)

# with open(r'nguyento.txt') as file: # mở file txt để lấy thông tin
#     lines = file.readlines()
    
#     for line in lines: # chia thông tin
#         split_data = line.split("|")

#         # đặt biến cho từng thông tin
#         stt = split_data[0].strip()
#         ki_hieu = split_data[1].strip()
#         ten = split_data[2].strip()
#         ntk = split_data[3].strip()
#         hoatri = split_data[4].strip()

#         # lập một từ điển
#         nguyen_tu = {
#             "stt": stt,
#             "ki_hieu" : ki_hieu,
#             "ten": ten,
#             "ntk": ntk,
#             "hoatri": hoatri
#         }
#         ds_nguyen_tu.append(nguyen_tu) # bỏ vào 1 list

# def hien_thi(stt, ki_hieu, ten, ntk, hoatri): # tạo một hàm với các thông tin đc cung cấp
#     global window, current_img_path
#     if window:
#         window.destroy()
#     window = Window(app) # tạo cửa sổ mới để hiển thị thông tin

#     # thông tin cần hiển thị
#     Text(window,f"STT: {stt}", size= 20)
#     Text(window,f"Kí hiệu: {ki_hieu}", size= 20)
#     Text(window,f"Tên: {ten}", size= 20)
#     Text(window,f"Nguyên tử khối: {ntk}", size= 20)
#     Text(window,f"Hóa trị: {hoatri}", size= 20)
#     current_img_path =f"birds/{stt}."

#     image = Image.open(current_img_path)
#     size = (450, 450)
#     resized_image = image.resize(size)
#     resized_image.save(current_img_path)
#     draw.image(0,0,resized_image)
# def loc_nhom(pt:list):
#     global all_button, count
#     L.visible = False
#     A.visible = False
#     if count % 2 != 0 :
#         for i in all_button.keys():
#             if i in pt:
#                 all_button[i].visible = True
#             else:
#                 all_button[i].visible = False
#         count += 1
#     else:
#         for i in all_button.keys():
#             all_button[i].visible = True
#             L.visible = True
#             A.visible = True
#         count = 1

# def Lant(pt:list):
#     global all_button, count
#     A.visible = False
#     if count % 2 != 0 :
#         for i in all_button.keys():
#             if i in pt:
#                 all_button[i].visible = True
#                 L.visible = True
#             else:
#                 all_button[i].visible = False
#         count += 1
#     else:
#         for i in all_button.keys():
#             all_button[i].visible = True
#             L.visible = True
#             A.visible = True

# def Acti(pt:list):
#     global all_button, count
#     L.visible = False
#     if count % 2 != 0 :
#         for i in all_button.keys():
#             if i in pt:
#                 all_button[i].visible = True
#                 A.visible = True
#             else:
#                 all_button[i].visible = False
#         count += 1
#     else:
#         for i in all_button.keys():
#             all_button[i].visible = True
#             L.visible = True
#             A.visible = True

# # khu phân loại và chỗ chứa màu
# # phân loại các nhóm 
# klk = [2, 10, 18, 36, 54, 86]
# mau1 = "#F74420"
# klkt = [3, 11, 19, 37, 55, 87]
# mau2 = "#FFD580"
# phikim = [0, 5, 6, 7, 14, 15, 33]
# mau3 = "#AAFF00"
# kimloaichuyentiep = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 56, 88, 71, 72, 73 ,74, 75, 76, 77, 78, 79, 103, 104, 105, 106, 107, 108, 109, 110, 111]
# mau4 = "#FA8072"
# Actini = ["**", 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102]
# mau5 = "#FF69B4"
# Lanthan = ["*", 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70]
# mau6 = "#FF8AFF"
# kimloaiyeu = [12, 30, 48, 49, 80, 81, 82, 112, 113, 114, 115]
# mau7 = "#A9A9A9"
# akim = [4, 13, 31, 32, 50, 51, 83]
# mau8 = "#8A9A5B"
# halogen = [8, 16, 34, 52, 84, 116]
# mau9 = "#FFFF8F"
# khihiem = [1, 9, 17, 35, 53, 85, 117]
# mau10 = "#00FFFF"

# # phân loại trạng thái
# khi = [0, 1, 6, 7, 8, 9, 16, 17, 35, 53, 85]
# chu1 = "#FF0000"
# long = [34, 79, 111]
# chu2 = "#008000"

# pt = [0, 2, 10, 18, 36, 54, 86] # list chứa thông tin cần sắp xếp bảng tuần hoàn
# for i in pt: # cho biến i trong list để lấy từng thông tin 
#     # đặt từng biến cho từng thông tin
#     stt = ds_nguyen_tu[i]['stt']
#     ki_hieu = ds_nguyen_tu[i]['ki_hieu']
#     ten = ds_nguyen_tu[i]["ten"]
#     ntk = ds_nguyen_tu[i]['ntk']
#     hoatri = ds_nguyen_tu[i]['hoatri']
#     # tạo một nút với các thông tin đã lấy đc
#     button = PushButton(box, text=ki_hieu, command=hien_thi, args=[stt, ki_hieu, ten, ntk, hoatri], grid=[x,y],width=4, height=1)
#     button.text_size=15
#     all_button[stt] = all_button.get(stt, button)
#     y+=1
#     # dùng điều kiện if - else để phân loại
#     if i in klk:
#         button.bg = mau1
#     elif i in phikim:
#         button.bg = mau3
#     if i in khi:
#         button.text_color = chu1

# pt = [3, 11, 19, 37, 55, 87]
# y=1
# x= 1
# for i in pt:
#     stt = ds_nguyen_tu[i]['stt']
#     ki_hieu = ds_nguyen_tu[i]['ki_hieu']
#     ten = ds_nguyen_tu[i]["ten"]
#     ntk = ds_nguyen_tu[i]['ntk']
#     hoatri = ds_nguyen_tu[i]['hoatri']
#     button = PushButton(box, text=ki_hieu, command=hien_thi, args=[stt, ki_hieu, ten, ntk, hoatri], grid=[x,y],width=4, height=1)
#     button.text_size=15
#     all_button[stt] = all_button.get(stt, button)
#     y+=1
#     if i in klkt:
#         button.bg= mau2

# pt = [20, 38, "*", "**", 21, 39, 71, 103, 22, 40, 72, 104, 23, 41, 73, 105, 24, 42, 74, 106, 25, 43, 75, 107, 26, 44, 76, 108, 27, 45, 77, 109, 28, 46, 78, 110, 29, 47, 79, 111]
# y=3
# x =2
# for i in pt:
#     # dùng điều kiện if - else để phân loại trường hợp đặc biệt
#     if i == "*":
#         stt = "57~71"
#         ki_hieu = "L"
#         ten = "Lant"
#         ntk = "không"
#         button = PushButton(box, text=ki_hieu, command=hien_thi, args=[stt, ki_hieu, ten, ntk], grid=[x,y],width=4, height=1)
#         button.text_size=15
#         all_button[stt] = all_button.get(stt, button)
#         y+=1
#     elif i == "**":
#         stt = "89~103"
#         ki_hieu = "A"
#         ten = "Actinit"
#         ntk = "không"
#         button = PushButton(box, text=ki_hieu, command=hien_thi, args=[stt, ki_hieu, ten, ntk], grid=[x,y],width=4, height=1)
#         button.text_size=15
#         all_button[stt] = all_button.get(stt, button)
#         y+=1
#     else:
#         stt = ds_nguyen_tu[i]['stt']
#         ki_hieu = ds_nguyen_tu[i]['ki_hieu']
#         ten = ds_nguyen_tu[i]["ten"]
#         ntk = ds_nguyen_tu[i]['ntk']
#         hoatri = ds_nguyen_tu[i]['hoatri']
#         button = PushButton(box, text=ki_hieu, command=hien_thi, args=[stt, ki_hieu, ten, ntk, hoatri], grid=[x,y],width=4, height=1)
#         button.text_size=15
#         all_button[stt] = all_button.get(stt, button)
#         y+=1
#     if y >= 7:
#         y = 3
#         x+= 1
#     if i in kimloaichuyentiep:
#         button.bg = mau4
#     elif i in Actini:
#         button.bg = mau5
#     elif i in Lanthan:
#         button.bg = mau6
#     if i in long:
#         button.text_color = chu2

# pt = [4, 12, 30, 48, 80, 112, 5, 13, 31, 49, 81, 113, 6, 14, 32, 50, 82, 114, 7, 15, 33, 51, 83, 115, 8, 16, 34, 52, 84, 116]
# y=1
# for i in pt:
#     stt = ds_nguyen_tu[i]['stt']
#     ki_hieu = ds_nguyen_tu[i]['ki_hieu']
#     ten = ds_nguyen_tu[i]["ten"]
#     ntk = ds_nguyen_tu[i]['ntk']
#     hoatri = ds_nguyen_tu[i]['hoatri']
#     button = PushButton(box, text=ki_hieu, command=hien_thi, args=[stt, ki_hieu, ten, ntk, hoatri], grid=[x,y],width=4, height=1)
#     button.text_size=15
#     all_button[stt] = all_button.get(stt, button)
#     y+=1
#     if y >= 7:
#         y = 1
#         x+= 1
#     if i in phikim:
#         button.bg = mau3
#     elif i in kimloaiyeu:
#         button.bg = mau7
#     elif i in akim:
#         button.bg = mau8
#     elif i in halogen:
#         button.bg = mau9
#     if i in khi:
#         button.text_color = chu1
#     elif i in long:
#         button.text_color = chu2

# pt = [1, 9, 17, 35, 53, 85, 117]
# y = 0
# for i in pt:
#     stt = ds_nguyen_tu[i]['stt']
#     ki_hieu = ds_nguyen_tu[i]['ki_hieu']
#     ten = ds_nguyen_tu[i]["ten"]
#     ntk = ds_nguyen_tu[i]['ntk']
#     hoatri = ds_nguyen_tu[i]['hoatri']
#     button = PushButton(box, text=ki_hieu, command=hien_thi, args=[stt, ki_hieu, ten, ntk, hoatri], grid=[x,y],width=4, height=1)
#     button.text_size=15
#     all_button[stt] = all_button.get(stt, button)
#     y+=1
#     if i in khihiem:
#         button.bg = mau10
#     if i in khi:
#         button.text_color = chu1

# # tạo 1 box nhầm tạo khoảng trống
# space = Box(box, layout="grid", grid=[1,7], width=1, height=50)

# pt = [56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102]
# y = 8
# x= 3
# # tạo 2 dòng chữ cho 2 trường hợp đặc biệt
# L = Text(box, text="L", grid=[2,8], size= 15)
# A =Text(box, text="A", grid=[2,9], size= 15)

# for i in pt:
#     stt = ds_nguyen_tu[i]['stt']
#     ki_hieu = ds_nguyen_tu[i]['ki_hieu']
#     ten = ds_nguyen_tu[i]["ten"]
#     ntk = ds_nguyen_tu[i]['ntk']
#     hoatri = ds_nguyen_tu[i]['hoatri']
#     button = PushButton(box, text=ki_hieu, command=hien_thi, args=[stt, ki_hieu, ten, ntk, hoatri], grid=[x,y],width=4, height=1)
#     button.text_size=15
#     all_button[stt] = all_button.get(stt, button)
#     x+=1
#     if x >= 18:
#         x = 3
#         y += 1
#     if i in kimloaichuyentiep:
#         button.bg= mau4
#     elif i in Actini:
#         button.bg = mau5
#     elif i in Lanthan:
#         button.bg = mau6

# # tạo chú thích cho dễ hiểu
# chuthich = Box(app, layout="grid")

# Text(chuthich, text="Chú thích: ", size= 25, grid=[0,0])
# Text(chuthich, text="Trạng thái vật chất: ", size= 20, grid=[0,1])
# the = ["Đen = Rắn", "Đỏ = Khí", "Lục = Lỏng"]
# x = 1
# for i in the:
#     button = PushButton(chuthich, text=i, grid=[x, 1], width=10, height=1)
#     button.text_size = 15
#     if i == "Đỏ = Khí":
#         button.text_color = chu1
#     elif i == "Lục = Lỏng":
#         button.text_color = chu2
#     x += 1

# Text(chuthich, text="Các nhóm cùng gốc trong bảng tuần hoàn: ", size= 20, grid=[0,2])
# x = 1
# y = 2
# for i in nhom:
#     if i == "Kim loại kiềm":
#         button = PushButton(chuthich, text= i, grid=[x, y], width=15, height=1, command=loc_nhom, args=[pt1])
#         button.text_size = 15
#         button.bg = mau1
#     elif i == "Kim loại kiềm thổ":
#         button = PushButton(chuthich, text= i, grid=[x, y], width=15, height=1, command=loc_nhom, args=[pt2])
#         button.text_size = 15
#         button.bg = mau2
#     elif i == "Lanthan":
#         button = PushButton(chuthich, text= i, grid=[x, y], width=15, height=1, command=Lant, args=[pt3])
#         button.text_size = 15
#         button.bg = mau6
#     elif i == "Actini":
#         button = PushButton(chuthich, text= i, grid=[x, y], width=15, height=1, command=Acti, args=[pt4])
#         button.text_size = 15
#         button.bg = mau5
#     elif i == "Kim loại chuyển tiếp":
#         button = PushButton(chuthich, text= i, grid=[x, y], width=15, height=1, command=loc_nhom, args=[pt5])
#         button.text_size = 15
#         button.bg = mau4
#     elif i == "Kim loại yếu":
#         button = PushButton(chuthich, text= i, grid=[x, y], width=15, height=1, command=loc_nhom, args=[pt6])
#         button.text_size = 15
#         button.bg = mau7
#     elif i == "Á kim":
#         button = PushButton(chuthich, text= i, grid=[x, y], width=15, height=1, command=loc_nhom, args=[pt7])
#         button.text_size = 15
#         button.bg = mau8
#     elif i == "Phi kim":
#         button = PushButton(chuthich, text= i, grid=[x, y], width=15, height=1, command=loc_nhom, args=[pt8])
#         button.text_size = 15
#         button.bg = mau3
#     elif i == "Halogen":
#         button = PushButton(chuthich, text= i, grid=[x, y], width=15, height=1, command=loc_nhom, args=[pt9])
#         button.text_size = 15
#         button.bg = mau9
#     elif i == "Khí hiếm":
#         button = PushButton(chuthich, text= i, grid=[x, y], width=15, height=1, command=loc_nhom, args=[pt10])
#         button.text_size = 15
#         button.bg = mau10
#     x += 1
#     if x >= 6:
#         x = 1
#         y += 1

# app.display()