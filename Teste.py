import pandas
import tabula
from IPython.display import display


pdf_path = r"C:\Docs\Python\Notas\Documentos\1267290_NotaCorretagem - 2019.03.pdf"


lista_tabelas = tabula.read_pdf(pdf_path, pages="1", guess=True)

for tabela in lista_tabelas:
    display(tabela)