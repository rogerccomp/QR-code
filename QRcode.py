import qrcode

# gerando um QRcode
link = "https://www.rogeriovaz-mat.com.br/"
imagem = qrcode.make(link)
imagem.save("link_sitePessoal.png")
print("Arquivo QRcode Criado com sucesso !!")
