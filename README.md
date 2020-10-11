# emojitex.sty

$\TeX$ package to display color emojis.

Inspired by:

- [coloremoji.sty](https://github.com/alecjacobson/coloremoji.sty)
- [How to use Noto Color Emoji with lualatex?](https://tex.stackexchange.com/questions/497403/how-to-use-noto-color-emoji-with-lualatex)
- [How to get certain Unicode characters appearing in LaTeX/PDF output?](https://groups.google.com/g/sphinx-users/c/XnJnQ2N1ACU)

## Installation

```console
$ mkdir -p ~/Library/texmf/tex/latex/local
$ cd ~/Library/texmf/tex/latex/local
$ git clone git@github.com:sdelquin/emojitex.sty.git
$ texhash emojitex.sty
```

## Requirements

- [LuaTeX](http://www.luatex.org/) as the engine to produce PDF output: `lualatex` (_included in last TeX distributions_).
- [Noto Emoji](https://github.com/googlefonts/noto-emoji) font to produce emojis (_included in last TeX distributions_).

## Examples

This `input.tex`:

```tex
\documentclass{article}
\usepackage{emojitex}
\begin{document}
Here I am using great color emojis 🎉.

You can have this 🍉 or that 🍋.
\end{document}
```

through `lualatex input.tex` produces the following output:

![TeX Output](tex_output.png)

## Development

The following snippet will produce (update) [emojitex.sty](emojitex.sty).

```console
$ git clone git@github.com:sdelquin/emojitex.sty.git
$ cd emojitex.sty
$ # create & activate a virtualenv
$ pip install -r requirements.txt
$ ./build.sh
```

### Update `emojitex.sty`

This package relies on [emoji](https://pypi.org/project/emoji/) Python package. From time to time it would be fine to update the file [emojitex.sty](emojitex.sty) file (_possible new emojis_):

```console
$ git clone git@github.com:sdelquin/emojitex.sty.git
$ cd emojitex.sty
$ # create & activate a virtualenv
$ pip install -U emoji # ensure update package
$ ./build.sh
```

## Disclaimer

I've only tested this package on [MacTeX 2020](https://tug.org/mactex/).
