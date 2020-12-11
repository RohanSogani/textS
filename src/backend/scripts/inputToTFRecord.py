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

def main():
    if len(sys.argv) != 2:
        print("Usage: inputToTFRecord.py <path_to_PDF_File>")
        exit(0)

    pdf_path = str(sys.argv[-1])
   
    text = convert.convert_pdf_to_txt(pdf_path)

    sentences = convert.create_sentences(text)
    input = str(sentences)
    input = input.replace("\'", "\"")

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
