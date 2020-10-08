import emoji

with open('emojitex.sty', mode='w') as fid:
    for emoji_glyph in emoji.unicode_codes.EMOJI_UNICODE.values():
        fid.write(f'{emoji_glyph}\n')
