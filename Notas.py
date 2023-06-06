import tabula
import pandas as pd

pdf_path = r"C:\Docs\Python\Notas\Documentos\1267290_NotaCorretagem - 2019.03.pdf"

dfs = tabula.read_pdf(pdf_path, pages="all", encoding="latin1")

selected_tables = [2, 3, 4, 5, 6, 7]

combined_table = pd.concat([dfs[table_num - 1] for table_num in selected_tables])

excel_path = r"C:\Docs\Python\Notas\Documentos\CombinedTable.xlsx"
combined_table.to_excel(excel_path, index=False)
