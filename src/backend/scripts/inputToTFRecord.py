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
import backend.scripts.convertPDF as convert
import json

def main():
    if len(sys.argv) != 2:
        print("Usage: inputToTFRecord.py <path_to_PDF_File>")
        exit(0)

    pdf_path = str(sys.argv[-1])
   
    convert.convert_pdf_to_txt(pdf_path)

    path_prefix = ""
    file_name = pdf_path.split("/")
    file_name = file_name[-1]
    file_name = file_name.split('.')
    file_name = file_name[0] + ".txt"
    file_name = path_prefix + file_name
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
    sentences = convert.create_sentences(one_text)
    # Convert single quotes to double quotes
    sentences = json.dumps(sentences)
    print(type(sentences))


    ''' input = str(sentences)
    input = input.replace("\'", "\"") '''

    input_dict = dict(
        inputs=sentences,
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
