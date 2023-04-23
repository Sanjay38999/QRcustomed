import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1,
                   error_correction = qrcode.constants.ERROR_CORRECT_H,
                   box_size = 10, border = 2,)
qr.add_data("https://github.com")
qr.make(fit = True)
img = qr.make_image(fill_colour = "black", background_colour = "grey")
img.save("QRCustome.png")