# pylint: disable=C0413
from onir import util
registry = util.Registry(default='flex')
register = registry.register

from onir.datasets.base import Dataset
from onir.datasets.index_backed import IndexBackedDataset, LazyDataRecord
from onir.datasets.multilingual_dataset import MultilingualDataset
from onir.datasets import antique, base, car, index_backed, msmarco, random, robust, flex, wikir, nyt, covid
from onir.datasets import trec_arabic, trec_mandarin, trec_spanish

# Datasets for CLEF
# from onir.datasets.clef_dataset import ClefDataset
# from onir.datasets.clef_en import ClefEnglishDataset
from onir.datasets.scale_multilingual_dataset import ScaleMultilingualDataset
from onir.datasets.clef_ru import ClefRussianDataset
from onir.datasets.trec_9_chinese import Trec9ChineseDataset
from onir.datasets.hc3 import HC3Dataset
from onir.datasets.hc3_zh import HC3ChineseDataset
from onir.datasets.hc3_ru import HC3RussianDataset

# Default iteration functions over datasets
from onir.datasets.query_iter import QueryIter as query_iter
from onir.datasets.doc_iter import DocIter as doc_iter
from onir.datasets.pair_iter import pair_iter
from onir.datasets.record_iter import record_iter, run_iter, qrels_iter, pos_qrels_iter
