#!/usr/bin/env python3
import re
import json
import sys
from typing import List

# Heuristic: detect Vietnamese characters
VIET_REGEX = re.compile(r"[\u00C0-\u1EF9]")

# Optional: try high‑quality translator if available
def get_translator():
    try:
        from deep_translator import GoogleTranslator  # pip install deep-translator
        return GoogleTranslator(source="vi", target="en")
    except Exception:
        return None

TRANSLATOR = get_translator()

# Fallback dictionary for common ML/dev terms (extend as needed)
FALLBACK_DICT = {
    "hàm": "function",
    "hàm số": "function",
    "biến": "variable",
    "lớp": "class",
    "mô hình": "model",
    "tham số": "parameter",
    "đối số": "argument",
    "ảnh": "image",
    "hình ảnh": "image",
    "chu thích": "caption",
    "chú thích": "caption",
    "tập huấn luyện": "training set",
    "huấn luyện": "training",
    "tập kiểm tra": "test set",
    "kiểm tra": "test",
    "xác thực": "validation",
    "đánh giá": "evaluation",
    "rò rỉ dữ liệu": "data leakage",
    "rò rỉ": "leakage",
    "tiền xử lý": "preprocessing",
    "tiền xử lí": "preprocessing",
    "hậu xử lý": "postprocessing",
    "tăng cường dữ liệu": "data augmentation",
    "tăng cường": "augmentation",
    "tách": "split",
    "tách tập": "split dataset",
    "từ vựng": "vocabulary",
    "mã hóa": "tokenization",
    "token hóa": "tokenization",
    "từ điển": "dictionary",
    "độ dài tối đa": "max length",
    "ngẫu nhiên": "random",
    "hạt giống": "seed",
    "đường dẫn": "path",
    "thư mục": "directory",
    "lưu": "save",
    "tải": "load",
    "mô tả": "description",
    "ví dụ": "example",
    "bước": "step",
    "và": "and",
    "của": "of",
    "một": "a",
    "vài": "few",
    "mẫu": "sample",
    "tính": "consistency",
    "nhất quán": "consistent",
    "với": "with",
    "có": "has",
    "thay vì": "instead of",
    "để": "to",
    "đảm bảo": "ensure",
    "sửa lại": "fix",
    "các": "the",
    "cho": "for",
    "này": "this",
    "đó": "that",
}

# Identifier mapping (safe renames). Only applies to whole identifiers.
IDENT_MAP = {
    "anh": "image",
    "hinh_anh": "image",
    "chu_thich": "caption",
    "du_lieu": "data",
    "tap_huan_luyen": "train_set",
    "tap_kiem_tra": "test_set",
    "tang_cuong_du_lieu": "data_augmentation",
    "ro_ri_du_lieu": "data_leakage",
    "tu_vung": "vocab",
    "do_dai_toi_da": "max_len",
    "ngau_nhien": "random_state",
}

IDENTIFIER_REGEX = re.compile(r"\b(" + "|".join(map(re.escape, IDENT_MAP.keys())) + r")\b")

def translate_text_vi_en(text: str) -> str:
    # Skip if no Vietnamese-looking characters to reduce no-op calls
    if not VIET_REGEX.search(text):
        return text
    
    # Preserve trailing newline if present
    has_newline = text.endswith('\n')
    text_to_translate = text.rstrip('\n')
    
    if TRANSLATOR:
        try:
            translated = TRANSLATOR.translate(text_to_translate)
            return translated + ('\n' if has_newline else '')
        except Exception:
            pass
    # Fallback word-level mapping (very naive)
    def replace_word(w: str) -> str:
        lw = w.lower()
        return FALLBACK_DICT.get(lw, w)
    # Preserve punctuation; replace tokens split by spaces
    tokens = re.split(r"(\s+)", text_to_translate)
    result = "".join(replace_word(tok) if tok.strip() else tok for tok in tokens)
    return result + ('\n' if has_newline else '')

def translate_markdown_lines(lines: List[str]) -> List[str]:
    return [translate_text_vi_en(line) for line in lines]

COMMENT_SPLIT = re.compile(r"^(?P<code>.*?)(?P<hash>\s*#\s*)(?P<comment>.*)$")

def translate_code_lines(lines: List[str]) -> List[str]:
    out = []
    in_triple = False
    triple_quote = None

    for line in lines:
        # Handle docstrings (translate content inside triple quotes)
        if not in_triple:
            m = re.search(r"([rubf]*)([\"']{3})", line, flags=re.IGNORECASE)
            if m:
                triple_quote = m.group(2)
                in_triple = True
                # Split at the first triple quote
                pre, quote, post = line.partition(triple_quote)
                # Translate the post part up to a closing triple quote if it exists on same line
                if triple_quote in post:
                    inner, q2, tail = post.partition(triple_quote)
                    inner_t = translate_text_vi_en(inner)
                    out.append(pre + quote + inner_t + q2 + tail)
                    in_triple = False
                    triple_quote = None
                else:
                    # Translate the rest as starting of docstring
                    post_t = translate_text_vi_en(post)
                    out.append(pre + quote + post_t)
                continue
        else:
            # We are inside a triple-quoted string
            if triple_quote in line:
                inner, q2, tail = line.partition(triple_quote)
                inner_t = translate_text_vi_en(inner)
                out.append(inner_t + q2 + tail)
                in_triple = False
                triple_quote = None
            else:
                out.append(translate_text_vi_en(line))
            continue

        # Translate full-line comments and inline comments
        if line.lstrip().startswith("#"):
            has_newline = line.endswith('\n')
            line_clean = line.rstrip('\n')
            prefix, comment = line_clean.split("#", 1)
            translated = prefix + "# " + translate_text_vi_en(comment.strip()).rstrip('\n')
            out.append(translated + ('\n' if has_newline else ''))
            continue

        m = COMMENT_SPLIT.match(line)
        if m:
            has_newline = line.endswith('\n')
            code = m.group("code")
            hashsym = m.group("hash")
            comment = m.group("comment").rstrip('\n')
            translated = f"{code}{hashsym}{translate_text_vi_en(comment).rstrip('\n')}"
            out.append(translated + ('\n' if has_newline else ''))
        else:
            out.append(line)
    return out

def rename_identifiers_in_code(lines: List[str]) -> List[str]:
    if not IDENT_MAP:
        return lines
    def repl(m: re.Match) -> str:
        return IDENT_MAP[m.group(1)]
    return [IDENTIFIER_REGEX.sub(repl, ln) for ln in lines]

def process_notebook(in_path: str, out_path: str):
    with open(in_path, "r", encoding="utf-8") as f:
        nb = json.load(f)

    for cell in nb.get("cells", []):
        src = cell.get("source", [])
        if isinstance(src, str):
            src = src.splitlines(keepends=False)

        if cell.get("cell_type") == "markdown":
            cell["source"] = translate_markdown_lines(src)
        elif cell.get("cell_type") == "code":
            translated = translate_code_lines(src)
            translated = rename_identifiers_in_code(translated)
            cell["source"] = translated

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)

def main():
    if len(sys.argv) < 3:
        print("Usage: python translate_vi_en_notebook.py <input.ipynb> <output.ipynb>")
        sys.exit(1)
    process_notebook(sys.argv[1], sys.argv[2])
    print(f"Translated notebook written to: {sys.argv[2]}")

if __name__ == "__main__":
    main()
