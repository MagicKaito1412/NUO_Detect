from mailmerge import MailMerge
from backend.form_report import app
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm
import jinja2
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM


path = app.root_path.replace('\\', '/')
doc_template = f"{path}/templates/doc_report_template.docx"
patient_template = f"{path}/templates/patient_report_template.docx"


def doc_report(data):
    patient_data = data.get('patient')
    ekgs_data = data.get('ekgs')

    svg = data.get('svg')

    svg = '<svg' + svg.split('<svg')[-1]
    svg = svg.split('<path')
    svg = svg[0] + ''.join(['<path ' + 'style="fill:none;"' + p for p in svg[1:]])

    with open(f"{path}/templates/img.svg", 'w') as f:
        f.write(svg)
    drawing = svg2rlg(f"{path}/templates/img.svg")
    sx = sy = 3
    drawing.width, drawing.height = drawing.minWidth() * sx, drawing.height * sy
    drawing.scale(sx, sy)
    image_path = f"{path}/templates/img.jpg"
    renderPM.drawToFile(drawing, image_path, fmt="JPG")

    for item in ekgs_data:
        for key, value in item.items():
            item[key] = str(value)

    document = MailMerge(doc_template)
    document.merge_pages([patient_data])
    document.merge_rows('ekg_id', ekgs_data)
    filename = f"Отчет_по_пациенту_{patient_data.get('patient_id')}_(для_врача).docx"
    new_file_path = f"{path}/templates/{filename}"
    document.write(new_file_path)

    tpl = DocxTemplate(new_file_path)
    context = {
        'Image': InlineImage(tpl, image_path, width=Mm(190))
    }
    jinja_env = jinja2.Environment(autoescape=True)
    tpl.render(context, jinja_env)
    tpl.save(new_file_path)

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
    new_file_path = f"{path}/templates/{filename}"
    document.write(new_file_path)

    return filename
