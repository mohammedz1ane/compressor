import argparse
import os
import zipfile
from PIL import Image
from PyPDF2 import PdfReader, PdfWriter
from docx2pdf import convert
from comtypes import client

def compress_pdf(file_path, power=0):
    output_path = os.path.splitext(file_path)[0] + '_compressed.pdf'
    reader = PdfReader(file_path)
    writer = PdfWriter()

    for page in reader.pages:
        page.compress_content_streams() 
        writer.add_page(page)

    for i in range(power):
        writer.add_metadata({
            "/Compress": "/FlateDecode",
            "/CompressFlate": "/FlateDecode",
            "/CompressObject": f"/CompressLevel{i+1}"
        })

    with open(output_path, "wb") as f:
        writer.write(f)

    print(f"Compressed PDF: {output_path}")
    print(f"Original size: {os.path.getsize(file_path) / 1024:.2f} KB")
    print(f"Compressed size: {os.path.getsize(output_path) / 1024:.2f} KB")
""""""
def compress_image(file_path):
    img = Image.open(file_path)
    output_path = os.path.splitext(file_path)[0] + '_compressed' + os.path.splitext(file_path)[1]
    img.save(output_path, optimize=True, quality=85)
    print(f"Compressed image: {output_path}")

def convert_to_pdf(file_path):
    if file_path.endswith('.docx'):
        output_path = os.path.splitext(file_path)[0] + '.pdf'
        convert(file_path, output_path)
        print(f"Converted DOCX to PDF: {output_path}")
    elif file_path.endswith('.pptx'):
        powerpoint = client.CreateObject('Powerpoint.Application')
        powerpoint.Visible = 1
        deck = powerpoint.Presentations.Open(file_path)
        output_path = os.path.splitext(file_path)[0] + '.pdf'
        deck.SaveAs(output_path, 32)  # 32 is the PDF format code
        deck.Close()
        powerpoint.Quit()
        print(f"Converted PPTX to PDF: {output_path}")
    else:
        print(f"Unsupported file format for conversion: {file_path}")

def compress_or_extract(name):
    if os.path.isfile(name):
        if name.endswith('.zip'):
            with zipfile.ZipFile(name, 'r') as zip_ref:
                zip_ref.extractall()
            print(f"Extracted ZIP: {name}")
        elif name.endswith('.rar'):
            print("RAR extraction not implemented")
        else:
            output_path = f"{name}.zip"
            with zipfile.ZipFile(output_path, 'w') as zip_ref:
                zip_ref.write(name)
            print(f"Compressed to ZIP: {output_path}")
    elif os.path.isdir(name):
        output_path = f"{name}.zip"
        with zipfile.ZipFile(output_path, 'w') as zip_ref:
            for root, _, files in os.walk(name):
                for file in files:
                    zip_ref.write(os.path.join(root, file))
        print(f"Compressed folder to ZIP: {output_path}")
    else:
        print(f"File or folder not found: {name}")

def compress_all_files():
    for file in os.listdir():
        if file.endswith(('.pdf', '.jpg', '.jpeg', '.png', '.gif')):
            if file.endswith('.pdf'):
                compress_pdf(file)
            else:
                compress_image(file)

def main():
    parser = argparse.ArgumentParser(description="Project Compressor")
    parser.add_argument('-a', action='store_true', help="Compress all PDF and image files in the current directory")
    parser.add_argument('-f', metavar='file_name', help="Compress the specified PDF or image file")
    parser.add_argument('-c', metavar='file_name', help="Convert the specified DOCX or PPTX file to PDF")
    parser.add_argument('-e', metavar='name', nargs='?', const='.', help="Compress or extract the specified file/folder, or compress the current directory if no argument is provided")

    args = parser.parse_args()

    if args.a:
        compress_all_files()
    elif args.f:
        if args.f.endswith('.pdf'):
            compress_pdf(args.f)
        elif args.f.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            compress_image(args.f)
        else:
            print(f"Unsupported file format: {args.f}")
    elif args.c:
        convert_to_pdf(args.c)
    elif args.e is not None:
        if args.e == '.':
            compress_all_files()
        else:
            compress_or_extract(args.e)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()