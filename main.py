import pathlib
import emoji

TEX_PACKAGE_FILENAME = 'emojitex.sty'
TEX_PACKAGE_PREAMBLE = 'preamble.tex'


preamble_contents = pathlib.Path(TEX_PACKAGE_PREAMBLE).read_text()

print('Creating TeX package... ', end='')

with open(TEX_PACKAGE_FILENAME, mode='w') as fid:
    fid.write(f'{preamble_contents}\n')
    for emoji_glyph in emoji.unicode_codes.EMOJI_UNICODE.values():
        fid.write(
            r'\newunicodechar{'
            f'{emoji_glyph}'
            r'}{{\NotoEmoji '
            f'{emoji_glyph}'
            r'}}'
            '\n'
        )

print(f'✅ Done! => {TEX_PACKAGE_FILENAME}')
