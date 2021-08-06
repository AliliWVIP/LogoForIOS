# 3.0 库变为Pillow
from PIL import Image

'''
filein: 输入图片
fileout: 输出图片
width: 输出图片宽度
height:输出图片高度
type:输出图片类型（png, gif, jpeg...）
'''


def ResizeImage(file_in, file_out, out_width, out_height, out_type):
    img = Image.open(file_in)
    out = img.resize((out_width, out_height), Image.ANTIALIAS)
    print(out)
    out.save(file_out, out_type)


if __name__ == "__main__":
    filein = r'./image/logo1024.png'
    file_type = 'png'

    fileouts = [r'./image/logo1024.png', r'./image/logo180.png',
                r'./image/logo167.png',
                r'./image/logo152.png', r'./image/logo76.png',
                r'./image/logo80.png', r'./image/logo40.png',
                r'./image/logo58.png', r'./image/logo29.png',
                r'./image/logo20.png', r'./image/logo120.png',
                r'./image/logo87.png', r'./image/logo60.png']
    widths = [1024, 180, 167, 152, 76, 80, 40, 58, 29, 20, 120, 87, 60]

    # fileout = r'./image/logo180.png'
    # width = 180
    # # height = 18
    for i in range(len(fileouts)):
        width = widths[i]
        fileout = fileouts[i]
        ResizeImage(filein, fileout, width, width, file_type)
