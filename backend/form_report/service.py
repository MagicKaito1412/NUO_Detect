from mailmerge import MailMerge
from backend.form_report import app
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

path = app.root_path.replace('\\', '/')
doc_template = f"{path}/templates/doc_report_template.docx"
patient_template = f"{path}/templates/patient_report_template.docx"


def doc_report(data):
    svg = data.get('svg')
    patient_data = data.get('patient')
    ekgs_data = data.get('ekgs')
    svg = '<svg' + svg.split('<svg')[-1]
    with open(f"{path}/templates/img.svg", 'w') as f:
        f.write(svg)
    drawing = svg2rlg("img.svg")
    sx, sy = 3
    drawing.width, drawing.height = drawing.minWidth() * sx, drawing.height * sy
    drawing.scale(sx, sy)
    renderPM.drawToFile(drawing, "img.jpg", fmt="JPG")

    for item in ekgs_data:
        for key, value in item.items():
            item[key] = str(value)

    document = MailMerge(doc_template)
    document.merge_pages([patient_data])
    document.merge_rows('ekg_id', ekgs_data)
    filename = f"Отчет_по_пациенту_{patient_data.get('patient_id')}_(для_врача).docx"
    document.write(f"{path}/templates/{filename}")
    return filename


def patient_report(data):
    patient_data = data.get('patient')
    ekgs_data = data.get('ekgs')
    for item in ekgs_data:
        for key, value in item.items():
            item[key] = str(value)

    document = MailMerge(patient_template)
    document.merge_pages([patient_data])
    document.merge_rows('ekg_id', ekgs_data)
    filename = f"Отчет_по_пациенту_{patient_data.get('patient_id')}.docx"
    document.write(f"{path}/templates/{filename}")
    return filename
