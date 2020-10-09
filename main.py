import pathlib
import emoji

TEX_PACKAGE_FILENAME = 'emojitex.sty'
TEX_PACKAGE_PREAMBLE = 'preamble.tex'


preamble_contents = pathlib.Path(TEX_PACKAGE_PREAMBLE).read_text()

print('Creating TeX package... ', end='')

with open(TEX_PACKAGE_FILENAME, mode='w') as fid:
    fid.write(f'{preamble_contents}\n')
    for emoji_name, emoji_glyph in emoji.unicode_codes.EMOJI_UNICODE.items():
        emoji_name = emoji_name.strip(':')
        # newunicodechar only admits single Unicode character
        # https://ctan.math.illinois.edu/macros/latex/contrib/newunicodechar/newunicodechar.pdf
        if len(emoji_glyph) == 1:
            fid.write(
                r'\newunicodechar{'
                f'{emoji_glyph}'
                r'}{{\NotoEmoji '
                f'{emoji_glyph}'
                r'}}'
                f'  % {emoji_name}'
                '\n'
            )

print(f'✅ Done! => {TEX_PACKAGE_FILENAME}')
