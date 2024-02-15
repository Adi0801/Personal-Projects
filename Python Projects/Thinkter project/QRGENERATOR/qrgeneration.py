# import qrcode as qr
# #make (give url or any string),save--some function of qrcode
# img=qr.make("https://www.youtube.com/watch?v=OKuiyX5k6zg&ab_channel=WsCubeTech")
# img.save("wscube_youtube.png")#name.format
# #it save were the python file is created 


#To format qr code img
import qrcode
from PIL import Image
#remover error such as overlapping of qr

qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=5)#here we correct high level error
qr.add_data("https://ncs.io/music")
qr.make(fit=True)#make only if date present in the url(fit=True)
img=qr.make_image(fill_color="red",back_color="white")#formating of the image
img.save("nscmusic_webpage.png")

