import os
import PyPDF2

def combine_pdfs(folder_path, output_file):
    pdf_files = [file for file in os.listdir(folder_path) if file.endswith('.pdf')]
    
    writer = PyPDF2.PdfWriter()
    
    for file in pdf_files:
        pdf_path = os.path.join(folder_path, file)
        with open(pdf_path, 'rb') as pdf:
            reader = PyPDF2.PdfReader(pdf)
            for page in range(len(reader.pages)):
                writer.add_page(reader.pages[page])
    
    with open(output_file, 'wb') as output:
        writer.write(output)

# Example usage
folder_path = 'input_files/ENGL306A_Module_3'
output_file = 'output_files/ENGL306A_Module_3.pdf'
combine_pdfs(folder_path, output_file)