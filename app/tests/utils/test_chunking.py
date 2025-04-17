from app.utils.text_chunker import chunk_text_based_on_conditions


def test_chunking():
    filename = "../dummy_data/sample.txt"
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()

    # 사용자로부터 입력 받은 값 (예시)
    chunk_size = 1000
    chunk_overlap = 100
    chunk_type = "문장"  # 선택 가능: 문서, 문단, 문장
    delimiter = None  # 구분자 (필요에 따라 사용)

    print("")
    print("문장")
    # 청킹 작업 수행
    documents = chunk_text_based_on_conditions(text, chunk_size, chunk_overlap, "문장", delimiter)

    # 결과 출력
    for i, doc in enumerate(documents):
        print(f"Document {i+1} content: {doc.page_content[:100]}...\n")
    print(documents)

    print("문단")
    # 청킹 작업 수행
    documents = chunk_text_based_on_conditions(text, chunk_size, chunk_overlap, "문단", delimiter)

    # 결과 출력
    for i, doc in enumerate(documents):
        print(f"Document {i+1} content: {doc.page_content[:100]}...\n")
    print(documents)


    print("문서")
    # 청킹 작업 수행
    documents = chunk_text_based_on_conditions(text, chunk_size, chunk_overlap, "문서", delimiter)

    # 결과 출력
    for i, doc in enumerate(documents):
        print(f"Document {i+1} content: {doc.page_content[100]}...\n")
    print(documents)