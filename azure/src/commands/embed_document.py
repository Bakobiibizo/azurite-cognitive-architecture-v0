from data_ingestion.loaders.loader_selector import LoaderSelector
from data_ingestion.document import Document
from data_ingestion.splitters.splitter_selector import NLTKTextSplitter
from data_ingestion.vectorstore.vectorstore import Vectorstores
from data_ingestion.embeddings.embeddings_caller import EmbeddingsCaller

loader = LoaderSelector().pdf_loader()
