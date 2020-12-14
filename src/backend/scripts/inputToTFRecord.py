import pandas as pd
import tensorflow as tf
import sys
import nltk
import json
import pdfbox
import re
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
    print("random**************************************************")
    p = pdfbox.PDFBox()
    p.extract_text(path)   # writes text to /path/to/my_file.txt

def create_sentences(text):
    """
    Converts the input text into sentences, also removes stop words 
    """
    print("random**************************************************")
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
        print("Usage: inputToTFRecord.py <path_to_PDF_File>")
        exit(0)

    pdf_path = str(sys.argv[-1])
    convert_pdf_to_txt(pdf_path)
    file_name = pdf_path.split(".")
    file_name = file_name[0] + ".txt"
    print(file_name)
    text = ""
    with open(file_name, 'r') as f:
        for line in f:
            line = line.rstrip("\n")
            if line[-1] == "-":
                line = line.rstrip("-")
            else:
                line = line + " "
            text += line
        print(len(line)) #
        # remove \n and create a list of strings
        #text = f.read().splitlines()

    # merge all strings in list to one big string for sentence tokenize
    one_text = ""
    one_text = "".join(text)
    # Split at before Introduction and after References
    one_text = one_text.split("Introduction")[1]
    one_text = one_text.split("References")[0]
    sentences = create_sentences(one_text)

    # Put \n before every sentence
    important_string = "\n".join(map(str, sentences))
    # Put spaces before and after punctuations
    important_string = re.sub('([.,!?()])', r' \1 ', important_string)
    important_string = re.sub('\s{2,}', ' ', important_string)
    # convert everything to lowercase
    important_string = important_string.lower()

    input_dict = dict(
        inputs=[important_string],
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
