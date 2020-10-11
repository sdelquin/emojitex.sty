from main import build_package


def test_build_package():
    package = build_package()
    package.count('newunicodechar') >= 1298
