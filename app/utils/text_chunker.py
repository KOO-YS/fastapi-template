from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

class TextChunker:
    def chunk_text(self, text: str):
        raise NotImplementedError("Subclasses should implement this method")

# 문서 단위 청킹
class DocumentChunker(TextChunker):
    def __init__(self, chunk_size=1000, chunk_overlap=100, delimiter=None):
        self.splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        self.delimiter = delimiter

    def chunk_text(self, text: str):
        # 텍스트를 구분자 기준으로 나눈 후 청킹
        if self.delimiter:
            text = text.replace(self.delimiter, '\n\n')  # 구분자를 문단 구분으로 변환
        return self.splitter.split_text(text)

# 문단 단위 청킹
class ParagraphChunker(TextChunker):
    def __init__(self, chunk_size=1000, chunk_overlap=100, delimiter=None):
        self.splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        self.delimiter = delimiter

    def chunk_text(self, text: str):
        paragraphs = text.split("\n\n")  # 기본적으로 문단을 구분
        chunks = []
        for paragraph in paragraphs:
            chunks.extend(self.splitter.split_text(paragraph))
        return chunks

# 문장 단위 청킹
class SentenceChunker(TextChunker):
    def __init__(self, chunk_size=1000, chunk_overlap=100, delimiter=None):
        self.splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        self.delimiter = delimiter

    def chunk_text(self, text: str):
        sentences = text.split("\n")  # 문장 단위로 텍스트를 분할
        chunks = []
        for sentence in sentences:
            chunks.extend(self.splitter.split_text(sentence))
        return chunks


# 청킹을 처리하는 함수
def chunk_text_based_on_conditions(text, chunk_size, chunk_overlap, chunk_type, delimiter=None):
    # 청킹 단위에 따라 처리하는 로직을 선택
    if chunk_type == "문서":
        chunker = DocumentChunker(chunk_size, chunk_overlap, delimiter)
    elif chunk_type == "문단":
        chunker = ParagraphChunker(chunk_size, chunk_overlap, delimiter)
    elif chunk_type == "문장":
        chunker = SentenceChunker(chunk_size, chunk_overlap, delimiter)
    else:
        raise ValueError("Invalid chunk type")

    # 텍스트 청킹
    chunks = chunker.chunk_text(text)

    # Document 객체로 변환
    documents = [Document(page_content=chunk) for chunk in chunks]

    return documents
