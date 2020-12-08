import sys
import nltk
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from nltk import sent_tokenize
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

def create_sentences(text):
    """
    Converts the input text into sentences, also removes stop words 
    """
    from nltk.corpus import stopwords
    nltk.download('stopwords')
    from nltk.tokenize import word_tokenize
    sentences = sent_tokenize(text)
    # print("There are ", len(sentences), "sentences in this paper")
    for i in range(0, 1):
        text_tokens = word_tokenize(sentences[50])
        tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]
        sentences[i] = (" ").join(tokens_without_sw)
    return sentences

def main():
    if len(sys.argv) != 2:
        print("Usage: convertPDF.py <path_to_PDF_File>")
        exit(0)

    pdf_path = str(sys.argv[-1])
    # print(pdf_path)
    nltk.download('punkt')
    text = convert_pdf_to_txt(pdf_path)
    # Remove references and further
    text = text.split("References")[0]
    sentences = create_sentences(text)
    path_prefix = "/home/ecs289gnlp/textS/src/backend/src/media/post_pdfs/"
    file_name = pdf_path.split("/")
    file_name = file_name[-1]
    file_name = file_name.split('.')
    file_name = file_name[0] + ".txt"
    file_name = path_prefix + file_name
    # print(file_name)
    with open(file_name, 'w') as f:
        for item in sentences:
            f.write("%s\n" % item)

if __name__ == "__main__":
    main()
