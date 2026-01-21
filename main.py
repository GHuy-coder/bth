from guizero import *

app = App("guizero", width=500, height=500)

box = Box(app, layout="grid")

window = None
ds_nguyen_tu = []

x= 0
y =0

with open(r'nguyento.txt') as file:
    lines = file.readlines()
    
    for line in lines:
        split_data = line.split("|")

        stt = split_data[0].strip()
        ki_hieu = split_data[1].strip()
        ten = split_data[2].strip()
        ntk = split_data[3].strip()
     
        nguyen_tu = {
            "stt": stt,
            "ki_hieu" : ki_hieu,
            "ten": ten,
            "ntk": ntk
        }
        ds_nguyen_tu.append(nguyen_tu)

def hien_thi(stt, ki_hieu, ten, ntk):
    global window
    if window:
        window.destroy()
    window = Window(app)

    Text(window,f"STT: {stt}")
    Text(window,f"Kí hiệu: {ki_hieu}")
    Text(window,f"Tên: {ten}")
    Text(window,f"Nguyên tử khối {ntk}")

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

khi = [0, 1, 6, 7, 8, 9, 16, 17, 35, 53, 85]
chu1 = "#FF0000"
long = [34, 79, 111]
chu2 = "#008000"

pt = [0, 2, 10, 18, 36, 54, 86]
for i in pt:
    stt = ds_nguyen_tu[i]['stt']
    ki_hieu = ds_nguyen_tu[i]['ki_hieu']
    ten = ds_nguyen_tu[i]["ten"]
    ntk = ds_nguyen_tu[i]['ntk']
    button = PushButton(box, text=ki_hieu, command=hien_thi, args=[stt, ki_hieu, ten, ntk], grid=[x,y],width=4, height=1)
    button.text_size=15
    y+=1
    if i in klk:
        button.bg = mau1
    elif i in phikim:
        button.bg = mau3
    if i in khi:
        button.text_color = chu1

pt = [3, 11, 19, 37, 55, 87]
y=1
x= 1
for i in pt:
    stt = ds_nguyen_tu[i]['stt']
    ki_hieu = ds_nguyen_tu[i]['ki_hieu']
    ten = ds_nguyen_tu[i]["ten"]
    ntk = ds_nguyen_tu[i]['ntk']
    button = PushButton(box, text=ki_hieu, command=hien_thi, args=[stt, ki_hieu, ten, ntk], grid=[x,y],width=4, height=1)
    button.text_size=15
    y+=1
    if i in klkt:
        button.bg= mau2

pt = [20, 38, "*", "**", 21, 39, 71, 103, 22, 40, 72, 104, 23, 41, 73, 105, 24, 42, 74, 106, 25, 43, 75, 107, 26, 44, 76, 108, 27, 45, 77, 109, 28, 46, 78, 110, 29, 47, 79, 111]
y=3
x =2
for i in pt:
    if i == "*":
        stt = "57~71"
        ki_hieu = "L"
        ten = "Lant"
        ntk = "không"
        button = PushButton(box, text=ki_hieu, command=hien_thi, args=[stt, ki_hieu, ten, ntk], grid=[x,y],width=4, height=1)
        button.text_size=15
        y+=1
    elif i == "**":
        stt = "89~103"
        ki_hieu = "A"
        ten = "Actinit"
        ntk = "không"
        button = PushButton(box, text=ki_hieu, command=hien_thi, args=[stt, ki_hieu, ten, ntk], grid=[x,y],width=4, height=1)
        button.text_size=15
        y+=1
    else:
        stt = ds_nguyen_tu[i]['stt']
        ki_hieu = ds_nguyen_tu[i]['ki_hieu']
        ten = ds_nguyen_tu[i]["ten"]
        ntk = ds_nguyen_tu[i]['ntk']
        button = PushButton(box, text=ki_hieu, command=hien_thi, args=[stt, ki_hieu, ten, ntk], grid=[x,y],width=4, height=1)
        button.text_size=15
        y+=1
    if y >= 7:
        y = 3
        x+= 1
    if i in kimloaichuyentiep:
        button.bg = mau4
    elif i in Actini:
        button.bg = mau5
    elif i in Lanthan:
        button.bg = mau6
    if i in long:
        button.text_color = chu2

pt = [4, 12, 30, 48, 80, 112, 5, 13, 31, 49, 81, 113, 6, 14, 32, 50, 82, 114, 7, 15, 33, 51, 83, 115, 8, 16, 34, 52, 84, 116]
y=1
for i in pt:
    stt = ds_nguyen_tu[i]['stt']
    ki_hieu = ds_nguyen_tu[i]['ki_hieu']
    ten = ds_nguyen_tu[i]["ten"]
    ntk = ds_nguyen_tu[i]['ntk']
    button = PushButton(box, text=ki_hieu, command=hien_thi, args=[stt, ki_hieu, ten, ntk], grid=[x,y],width=4, height=1)
    button.text_size=15
    y+=1
    if y >= 7:
        y = 1
        x+= 1
    if i in phikim:
        button.bg = mau3
    elif i in kimloaiyeu:
        button.bg = mau7
    elif i in akim:
        button.bg = mau8
    elif i in halogen:
        button.bg = mau9
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
    button = PushButton(box, text=ki_hieu, command=hien_thi, args=[stt, ki_hieu, ten, ntk], grid=[x,y],width=4, height=1)
    button.text_size=15
    y+=1
    if i in khihiem:
        button.bg = mau10
    if i in khi:
        button.text_color = chu1

space = Box(box, layout="grid", grid=[1,7], width=1, height=50)

pt = [56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102]
y = 8
x= 3
Text(box, text="L", grid=[2,8], size= 15)
Text(box, text="A", grid=[2,9], size= 15)

for i in pt:
    stt = ds_nguyen_tu[i]['stt']
    ki_hieu = ds_nguyen_tu[i]['ki_hieu']
    ten = ds_nguyen_tu[i]["ten"]
    ntk = ds_nguyen_tu[i]['ntk']
    button = PushButton(box, text=ki_hieu, command=hien_thi, args=[stt, ki_hieu, ten, ntk], grid=[x,y],width=4, height=1)
    button.text_size=15
    x+=1
    if x >= 18:
        x = 3
        y += 1
    if i in kimloaichuyentiep:
        button.bg= mau4
    elif i in Actini:
        button.bg = mau5
    elif i in Lanthan:
        button.bg = mau6

chuthich = Box(app, layout="grid")

Text(chuthich, text="Chú thích: ", size= 25, grid=[0,0])
Text(chuthich, text="Trạng thái vật chất: ", size= 20, grid=[0,1])
the = ["Đen = Rắn", "Đỏ = Khí", "Lục = Lỏng"]
x = 1
for i in the:
    button = PushButton(chuthich, text=i, grid=[x, 1], width=10, height=1)
    button.text_size = 15
    if i == "Đỏ = Khí":
        button.text_color = chu1
    elif i == "Lục = Lỏng":
        button.text_color = chu2
    x += 1

Text(chuthich, text="Các nhóm cùng gốc trong bảng tuần hoàn: ", size= 20, grid=[0,2])
nhom = ["Kim loại kiềm", "Kim loại kiềm thổ", "Lanthan", "Actini", "Kim loại chuyển tiếp", "Kim loại yếu", "Á kim", "Phi kim", "Halogen", "Khí hiếm"]
x = 1
y = 2
for i in nhom:
    button = PushButton(chuthich, text= i, grid=[x, y], width=15, height=1)
    button.text_size = 15
    if i == "Kim loại kiềm":
        button.bg = mau1
    elif i == "Kim loại kiềm thổ":
        button.bg = mau2
    elif i == "Lanthan":
        button.bg = mau6
    elif i == "Actini":
        button.bg = mau5
    elif i == "Kim loại chuyển tiếp":
        button.bg = mau4
    elif i == "Kim loại yếu":
        button.bg = mau7
    elif i == "Á kim":
        button.bg = mau8
    elif i == "Phi kim":
        button.bg = mau3
    elif i == "Halogen":
        button.bg = mau9
    elif i == "Khí hiếm":
        button.bg = mau10
    x += 1
    if x >= 6:
        x = 1
        y += 1

app.display()