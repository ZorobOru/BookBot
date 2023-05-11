import re


def _get_part_text(text: str, start: int, page_size: int) -> tuple[str, int]:
    edit_text = re.sub(r'[,.?!;:]\.+$', '', text[start: start + page_size])
    edit_text = re.search(r'(?s).+[,.?!:;]', edit_text).group()
    return edit_text, len(edit_text)


def prepare_book(path: str) -> None:

    with open(path, 'r', encoding='UTF-8') as text:
        text_book = text.read()

    number_pages = start = 0
    while len(text_book) != start:
        number_pages += 1
        page, end = _get_part_text(text_book, start, PAGE_SIZE)
        book[number_pages] = page.lstrip()
        start += end


BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}

prepare_book(BOOK_PATH)
