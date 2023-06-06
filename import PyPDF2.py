import tabula

pdf_path = r"C:\Docs\Python\Notas\Documentos\1267290_NotaCorretagem - 2019.03.pdf"

tables = tabula.read_pdf(pdf_path, pages="all", multiple_tables=True)

if len(tables) > 0:
    print("The PDF file contains tables.")
else:
    print("The PDF file does not contain tables.")
