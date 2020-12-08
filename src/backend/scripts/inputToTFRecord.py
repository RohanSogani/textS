import pandas as pd
import tensorflow as tf
import sys

input_dict = dict(
    inputs=[sys.argv[1]],
    targets=[""]
    )

save_path = "~/textS/src/pegasus/pegasus/data/testdata/test_pattern_1.tfrecord"
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
