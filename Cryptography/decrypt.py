# Decryption

file_name = input('Enter Filename with extension like .txt .jpg .png .pdf: ')
file_type = input('Enter file extension like txt jpg png pdf: ')

if file_type == 'text' or file_type == 'txt':
    fo = open(file_name, "rb")
    file = fo.read()
    fo.close()
    file = bytearray(file)
    key = 48
    for index , value in enumerate(file):
        file[index] = value^key
    fo = open("decrypted.txt", "wb")
    fo.write(file)
    fo.close()
    print("The file is successfully decrypted")

elif file_type == 'image' or file_type == 'jpg' or file_type == 'png':
    fo = open(file_name, "rb")
    image = fo.read()
    fo.close()
    image = bytearray(image)
    key = 48
    for index, value in enumerate(image):
        image[index] = value^key
    if file_type == 'jpg':
        fo = open("decrypted.jpg " , "wb")
        fo.write(image)
        fo.close()
        print("The file is successfully decrypted")
    elif file_type == 'png':
        fo = open("decrypted.png ", "wb")
        fo.write(image)
        fo.close()
        print("The file is successfully decrypted")
    else:
        fo = open("decrypted.jpg ", "wb")
        fo.write(image)
        fo.close()
        print("The file is successfully decrypted")

elif file_type == 'pdf' or file_type == 'doc' or file_type == 'docx':
    fo = open(file_name, "rb")
    pdf = fo.read()
    fo.close()
    pdf = bytearray(pdf)
    key = 48
    for index , value in enumerate(pdf):
        pdf[index] = value^key
    if file_type == 'pdf':
        fo = open("decrypted.pdf", "wb")
        fo.write(pdf)
        fo.close()
        print("The file is successfully decrypted")
    elif file_type == 'doc':
        fo = open("decrypted.doc", "wb")
        fo.write(pdf)
        fo.close()
        print("The file is successfully decrypted")
    elif file_type == 'docx':
        fo = open("decrypted.doc", "wb")
        fo.write(pdf)
        fo.close()
        print("The file is successfully decrypted")
    else:
        fo = open(file_name, "wb")
        fo.write(pdf)
        fo.close()
else:
  print('try again')

