#!/bin/bash

inputPDFFilePath=$1
echo "Input PDF file path: $inputPDFFilePath"

python3 /home/ecs289gnlp/textS/src/backend/scripts/inputToTFRecord.py "$inputPDFFilePath"

cd /home/ecs289gnlp/textS/src/pegasus/
export PYTHONPATH=.

python3 ./pegasus/bin/evaluate.py \
--params=arxiv_transformer \
--param_overrides=vocab_filename=ckpt/pegasus_ckpt/c4.unigram.newline.10pct.96000.model,batch_size=1,beam_size=1,beam_alpha=0.8 \
--model_dir=ckpt/pegasus_ckpt/arxiv/model.ckpt-340000
