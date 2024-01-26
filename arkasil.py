import pyqrcode
url=input("enter you url")

qr_cod=pyqrcode.create(url)
qr_cod.svg("qrcode.svg",scale=8)