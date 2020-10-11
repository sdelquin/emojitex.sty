import pathlib
import emoji

TEX_PACKAGE_FILENAME = 'emojitex.sty'
TEX_PACKAGE_PREAMBLE = 'preamble.tex'


def build_package(emoji_glyph_max_length=1):
    buffer = []
    preamble_contents = pathlib.Path(TEX_PACKAGE_PREAMBLE).read_text()
    buffer.append(preamble_contents)
    for emoji_name, emoji_glyph in emoji.unicode_codes.EMOJI_UNICODE.items():
        emoji_name = emoji_name.strip(':')
        # newunicodechar only admits single Unicode character
        # https://ctan.math.illinois.edu/macros/latex/contrib/newunicodechar/newunicodechar.pdf
        if len(emoji_glyph) <= emoji_glyph_max_length:
            buffer.append(
                r'\newunicodechar{'
                f'{emoji_glyph}'
                r'}{{\NotoEmoji '
                f'{emoji_glyph}'
                r'}}'
                f'  % {emoji_name}'
            )
    return '\n'.join(buffer)


if __name__ == '__main__':
    print('Creating TeX package... ', end='')
    package = build_package()
    pathlib.Path(TEX_PACKAGE_FILENAME).write_text(package)
    print(f'✅ Done! => {TEX_PACKAGE_FILENAME}')
