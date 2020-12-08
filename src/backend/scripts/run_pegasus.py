python3 ~/textS/src/backend/scripts/inputToTFRecord.py random

cd ~/textS/src/pegasus/

python3 ./pegasus/bin/evaluate.py \
--params=arxiv_transformer \
--param_overrides=vocab_filename=ckpt/pegasus_ckpt/c4.unigram.newline.10pct.96000.model,batch_size=1,beam_size=2,beam_alpha=0.6 \
--model_dir=ckpt/pegasus_ckpt/arxiv/model.ckpt-340000
