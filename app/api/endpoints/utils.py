def chunk_text(text: str, max_words: int = 500, min_words: int = 100) -> list:
    import re
    paragraphs = [p.strip() for p in re.split(r'\n{2,}', text) if p.strip()]
    chunks = []
    current_chunk = ""
    current_word_count = 0

    for para in paragraphs:
        words = para.split()
        if len(words) > max_words:
            for i in range(0, len(words), max_words):
                split_chunk = " ".join(words[i:i + max_words])
                if current_chunk:
                    chunks.append(current_chunk)
                    current_chunk = ""
                    current_word_count = 0
                chunks.append(split_chunk)
        elif current_word_count + len(words) < min_words:
            current_chunk += ("\n\n" if current_chunk else "") + para
            current_word_count += len(words)
        else:
            if current_chunk:
                chunks.append(current_chunk)
            current_chunk = ""
            current_word_count = 0

    if current_chunk:
        chunks.append(current_chunk)

    return chunks