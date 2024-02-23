import PyPDF2
import os
#done

from config import SOURCE_DIR, RESULT_DIR


def split_pdf(input_folder, output_folder):
    if not os.path.exists(RESULT_DIR):
        os.makedirs(RESULT_DIR)

    for file_name in os.listdir(SOURCE_DIR):
        # Check if the file is an .pdf
        if file_name.endswith('.pdf'):
            # Construct the full path to the PDF file
            input_file = os.path.join(SOURCE_DIR, file_name)

            with open(input_file, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)

                if len(pdf_reader.pages) % 2 != 0:
                    print("Error: The number of pages in the PDF must be even for duplex scanning.")
                    return

                for i in range(0, len(pdf_reader.pages), 2):
                    pdf_writer = PyPDF2.PdfWriter()
                    pdf_writer.add_page(pdf_reader.pages[i])
                    pdf_writer.add_page(pdf_reader.pages[i + 1])

                    output_file = os.path.join(output_folder, f"result_{i//2 + 1}.pdf")

                    with open(output_file, 'wb') as output:
                        pdf_writer.write(output)


if __name__ == "__main__":
    split_pdf(SOURCE_DIR, RESULT_DIR)
