import qrcode

data = "Any Link to somewhere"

img = qrcode.make(data)

img.save('C:/Users/mypath/img.png')