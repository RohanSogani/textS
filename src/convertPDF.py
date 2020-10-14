import sys
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

def convert_pdf_to_txt(path):
    """
    Converts the input pdf file to a plain text
    """
    rsrc_mgr = PDFResourceManager()
    ret_str = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrc_mgr, ret_str, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrc_mgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = ret_str.getvalue()
    fp.close()
    device.close()
    ret_str.close()
    return text

def main():
    if len(sys.argv) is not 2:
        print("Usage: convertPDF.py <path_to_PDF_File>")
        exit(0)

    pdf_path =  str(sys.argv[-1])
    print(pdf_path)

    text = convert_pdf_to_txt(pdf_path)
    no_references = text.split("References")
    no_references = no_references[0]
    print(len(no_references))

    print(no_references)
    sentences = no_references.split(".")
    print(f'''The length of sentences is {len(sentences)}''')
    final_sentences = []
    for s in sentences:
        remove_newline = s.split("\n")
        for r in remove_newline:
            if r == "":
                continue
            final_sentences.append(r)

    print(f'''The final number of sentences is {len(final_sentences)}''')
    print(final_sentences)

if __name__ == "__main__":
    main()
