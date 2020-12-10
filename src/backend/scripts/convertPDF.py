import sys
import nltk
import pdfbox
import json
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
    ''' rsrc_mgr = PDFResourceManager()
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
    ret_str.close() '''

    p = pdfbox.PDFBox()
    p.extract_text(path)   # writes text to /path/to/my_file.txt
    

def create_sentences(text):
    """
    Converts the input text into sentences, also removes stop words 
    """
    from nltk.corpus import stopwords
    nltk.download('stopwords')
    from nltk.tokenize import sent_tokenize
    from nltk.tokenize import word_tokenize
    sentences = sent_tokenize(text)
    # print(sentences)
    # print("There are ", len(sentences), "sentences in this paper")
    final_sentences = []
    ''' for i in range(0, len(sentences)):
        text_tokens = word_tokenize(sentences[i])
        tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]
        final_sentences.append((" ").join(tokens_without_sw))
    print(final_sentences) '''
    return sentences


def main():
    if len(sys.argv) != 2:
        print("Usage: convertPDF.py <path_to_PDF_File>")
        exit(0)

    pdf_path = str(sys.argv[-1])
    # print(pdf_path)
    nltk.download('punkt')
    convert_pdf_to_txt(pdf_path)
    # Remove references and further
    #text = text.split("References")[0]
    
    path_prefix = ""
    file_name = pdf_path.split("/")
    file_name = file_name[-1]
    file_name = file_name.split('.')
    file_name = file_name[0] + ".txt"
    file_name = path_prefix + file_name
    print(file_name)
    text = ""
    with open(file_name, 'r') as f:
        # remove \n and create a list of strings
        text = f.read().splitlines()

    # merge all strings in list to one big string for sentence tokenize
    one_text = ""
    one_text = "".join(text)
    
    # Split at before Introduction and after References
    one_text = one_text.split("Introduction")[1]
    one_text = one_text.split("References")[0]
    sentences = create_sentences(one_text)
    # Convert single quotes to double quotes
    sentences = json.dumps(sentences)
    # print(sentences[-1])

if __name__ == "__main__":
    main()
