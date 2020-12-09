import pandas as pd
import tensorflow as tf
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
    print(sentences)
    return sentences

def main():
    if len(sys.argv) != 2:
            print("Usage: inputToTFRecord.py <path_to_PDF_File>")
            exit(0)

    pdf_path = str(sys.argv[-1])
    # print(pdf_path)
    nltk.download('punkt')
    text = convert_pdf_to_txt(pdf_path)
    # Remove references and further
    text = text.split("References")[0]
    sentences = create_sentences(text)

    sentences = str(sentences)
    sentences = sentences.replace("\'", "\"")

    input_dict = dict(
        inputs=[sentences],
        targets=[""]
        )

    save_path = "/home/ecs289gnlp/textS/src/pegasus/pegasus/data/testdata/input.tfrecord"
    data = pd.DataFrame(input_dict)
    with tf.io.TFRecordWriter(save_path) as writer:
        for row in data.values:
            inputs, targets = row[:-1], row[-1]
            example = tf.train.Example(
                features=tf.train.Features(
                    feature={
                        "inputs": tf.train.Feature(bytes_list=tf.train.BytesList(value=[inputs[0].encode('utf-8')])),
                        "targets": tf.train.Feature(bytes_list=tf.train.BytesList(value=[targets.encode('utf-8')])),
                    }
                )
            )
            writer.write(example.SerializeToString())

if __name__ == "__main__":
    main()