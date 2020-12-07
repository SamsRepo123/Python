## MODULES REQUIRED ##
# pypdf2

from PyPDF2 import PdfFileWriter, PdfFileReader


def locker(file, password):
    parser = PdfFileWriter()
    pdf = PdfFileReader(file)
    for page in range(pdf.numPages):
        parser.addPage(pdf.getPage(page))
    parser.encrypt(password)
    with open(f"encrypted_{file}", "wb") as f:
        parser.write(f)
        f.close()
    print(f"encrypted_{file} file is Created...")


if __name__ == "__main__":
    file = input("Enter your pdf file name with extension .pdf: ")
    password = input("Enter Password: ")
    locker(file, password)
