from pathlib import Path
from openpyxl import Workbook
from main import HEADERS
root=Path(__file__).resolve().parent/'sample_data'; root.mkdir(exist_ok=True)
for name,rows in {'country_a':[['Demo A',2027,120,130,250,12]],'country_b':[['Demo B',2027,90,100,190,10]],'country_c':[['Demo C',2027,50,60,999,5]],'country_d':[['Demo D',2027,None,60,110,5]]}.items():
    wb=Workbook(); ws=wb.active; ws.title='Survey'; ws.append(HEADERS)
    for row in rows: ws.append(row)
    wb.save(root/f'{name}.xlsx')
