"""arxiv dataset."""
import tensorflow.compat.v2 as tf
import tensorflow_datasets as tfds
import os
import json

_DESCRIPTION = """
Research Papers from Arxiv.
Subset contains papers only from CS.CR, CS.DB, & CS.DC.
"""

_CITATION = """
"""

_DOCUMENT = "input"
_SUMMARY = "targets"

class Arxiv(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for arxiv dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            # These are the features of your dataset like images, labels ...
            _DOCUMENT: tfds.features.Text(),
            _SUMMARY: tfds.features.Text()
            # "section_names": tfds.features.Text(),
        }),
        # If there's a common (input, target) tuple from the
        # features, specify them here. They'll be used if
        # `as_supervised=True` in `builder.as_dataset`.
        supervised_keys=(_DOCUMENT, _SUMMARY),  # Set to `None` to disable
        homepage="https://github.com/armancohan/long-summarization",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    # path = dl_manager.download_and_extract('https://todo-data-url')
    path = os.path.join('dummy_data')
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={"path": os.path.join(path, "train.txt")},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={"path": os.path.join(path, "val.txt")},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={"path": os.path.join(path, "test.txt")},
        ),
    ]

  def _generate_examples(self, path):
    """Yields examples."""
    with tf.io.gfile.GFile(path) as f:
      for line in f:
          d = json.loads(line)
          summary = "\n".join(d["abstract_text"])
          summary = summary.replace("<S>", "").replace("</S", "")
          yield d["article_id"], {
            _DOCUMENT: "\n".join(d["article_text"]),
            _SUMMARY: summary
            # "section_names": "\n".join(d["section_names"])
          }
