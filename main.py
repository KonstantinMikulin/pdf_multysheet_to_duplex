import os
from datetime import datetime
import pypdf

from config import INPUT_DIR, RESULT_DIR


def split_pdf(input_dir, output_dir):
    if not os.path.exists(RESULT_DIR):
        os.makedirs(RESULT_DIR)

    print(input_dir)
    print(output_dir)
    
    for file_name in os.listdir(input_dir):
        # Check if the file is an .pdf
        if file_name.endswith('.pdf'):
            # Construct the full path to the PDF file
            input_file = os.path.join(input_dir, file_name)

            with open(input_file, 'rb') as file:
                pdf_reader = pypdf.PdfReader(file)

                if len(pdf_reader.pages) % 2 != 0:
                    print("Error: The number of pages in the PDF must be even for duplex scanning.")
                    return

                for i in range(0, len(pdf_reader.pages), 2):
                    pdf_writer = pypdf.PdfWriter()
                    pdf_writer.add_page(pdf_reader.pages[i])
                    pdf_writer.add_page(pdf_reader.pages[i + 1])
                    time_stamp = str(datetime.now()).replace(':', '')

                    output_file = os.path.join(output_dir, f"result {time_stamp}.pdf")

                    with open(output_file, 'wb') as output:
                        pdf_writer.write(output)


if __name__ == "__main__":
    split_pdf(INPUT_DIR, RESULT_DIR)
