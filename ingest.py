from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
import shutil
import box
import yaml
import warnings

from io import BytesIO
from pypdf import PdfReader


warnings.filterwarnings("ignore", category=DeprecationWarning)


def run_ingest(file_loc):
    # Import config vars
    with open('config.yml', 'r', encoding='utf8') as ymlfile:
        cfg = box.Box(yaml.safe_load(ymlfile))
    
    with open(file_loc,"rb") as fh:
        bytes_stream = BytesIO(fh.read())

    reader = PdfReader(bytes_stream)

    documents = reader.pages[0].extract_text()
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=cfg.CHUNK_SIZE,
                                              chunk_overlap=cfg.CHUNK_OVERLAP)
    documents = text_splitter.create_documents([documents])
    
    #texts = text_splitter.split_documents(documents)
    #print(f"Loaded {len(texts)} splits")

    embeddings = HuggingFaceEmbeddings(model_name=cfg.EMBEDDINGS,
                                       model_kwargs={'device': cfg.DEVICE},
                                       encode_kwargs={'normalize_embeddings': cfg.NORMALIZE_EMBEDDINGS})

    shutil.rmtree(cfg.VECTOR_DB, ignore_errors=True)

    vector_store = Chroma.from_documents(documents,
                                         embeddings,
                                         collection_name=cfg.COLLECTION_NAME,
                                         collection_metadata={"hnsw:space": cfg.VECTOR_SPACE},
                                         persist_directory=cfg.VECTOR_DB)

    print(f"Vector store created at {cfg.VECTOR_DB}")


if __name__ == "__main__":
    run_ingest()