from pathlib import Path
from collections import Counter
from openpyxl import Workbook, load_workbook
import csv
ROOT=Path(__file__).resolve().parent
HEADERS=['country','year','female_students','male_students','total_students','teachers']

def run(root=ROOT):
    out=root/'outputs'; out.mkdir(exist_ok=True)
    updated=out/'updated_templates'; updated.mkdir(exist_ok=True)
    rows=[]; issues=[]
    for path in sorted((root/'sample_data').glob('*.xlsx')):
        wb=load_workbook(path)
        if 'Survey' not in wb.sheetnames or list(next(wb['Survey'].values,()))!=HEADERS:
            issues.append([path.name,0,'Invalid survey structure']); continue
        ws=wb['Survey']
        if 'Metadata' not in wb.sheetnames: wb.create_sheet('Metadata')
        wb['Metadata']['A1']='Template version'; wb['Metadata']['B1']='2027-demo-v1'
        wb.save(updated/path.name)
        for i,row in enumerate(list(ws.values)[1:],2):
            if all(v is None for v in row): continue
            rows.append((path.name,i,row))
    counts=Counter((r[0],r[1]) for _,_,r in rows)
    valid=[]
    for name,i,r in rows:
        country,year,f,m,total,t=r; errors=[]
        if not isinstance(country,str) or not country.strip(): errors.append('Missing country')
        if year!=2027: errors.append('Unexpected survey year')
        if any(type(v) is not int or v<0 for v in (f,m,total,t)): errors.append('Counts must be nonnegative integers')
        elif f+m!=total: errors.append('Enrolment totals inconsistent')
        if counts[(country,year)]>1: errors.append('Duplicate country/year')
        if errors: issues.extend([name,i,e] for e in errors)
        else: valid.append([*r,name,i])
    wb=Workbook(); ws=wb.active; ws.title='Validated'; ws.append(HEADERS+['source_file','source_row'])
    for r in valid: ws.append(r)
    ws.freeze_panes='A2'; ws.auto_filter.ref=ws.dimensions
    wb.save(out/'consolidated.xlsx')
    with (out/'validation_report.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f); w.writerow(['source_file','source_row','issue']); w.writerows(issues)
    print(f'Rows read: {len(rows)}; accepted: {len(valid)}; rejected: {len(rows)-len(valid)}; issues: {len(issues)}')
    return valid,issues
if __name__=='__main__': run()
