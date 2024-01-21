import PyPDF2
import os

input_pdf = 'C:/Users/user/Desktop/pdf_multysheet/test_pdf.pdf'
store_folder = 'C:/Users/user/Desktop/pdf_multysheet/pdf_duplex'


def split_pdf(input_file, output_folder):
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
    if not os.path.exists(store_folder):
        os.makedirs(store_folder)

    split_pdf(input_pdf, store_folder)
