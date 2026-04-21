# This is a sample Python script.
import pandas as pd

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from fpdf import FPDF

def print_pdf():
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    df = pd.read_csv('topics.csv')
    for index, row in df.iterrows():
        # for _ in row
        pdf.add_page()
        pdf.set_text_color(100, 100, 100)
        pdf.set_font('Times', 'B', size=12)
        pdf.cell(0, 12, txt=row["Topic"], ln=1, align='L')

        pdf.line(10, 21, 200, 21)

    pdf.output('My_PDF_file.pdf')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_pdf()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
