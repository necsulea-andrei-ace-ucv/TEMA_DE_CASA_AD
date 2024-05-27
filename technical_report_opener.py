import subprocess


def open_pdf_with_default_app(pdf_file_path):
    subprocess.run(["start", "", pdf_file_path], shell=True, check=True)

def open_technical_report():
    pdf_file_path = "experimental_data/technical_report.pdf"
    open_pdf_with_default_app(pdf_file_path)