import ahk
import re

nimi = {
    'kijetesantakalu': 'U+F1980',  # 󱦀
    'misikeke': 'U+F1987',  # 󱦇
    'kokosila': 'U+F1984',  # 󱦄
    'kepeken': 'U+F1919',  # 󱤙
    'sitelen': 'U+F1960',  # 󱥠
    'monsuta': 'U+F197D',  # 󱥽
    'lanpan': 'U+F1985',  # 󱦅
    'kalama': 'U+F1915',  # 󱤕
    'kulupu': 'U+F191F',  # 󱤟
    'pakala': 'U+F1948',  # 󱥈
    'palisa': 'U+F194A',  # 󱥊
    'pimeja': 'U+F194F',  # 󱥏
    'sijelo': 'U+F195B',  # 󱥛
    'sinpin': 'U+F195F',  # 󱥟
    'soweli': 'U+F1962',  # 󱥢
    'majuna': 'U+F19A2',  # 󱦢
    'namako': 'U+F1978',  # 󱥸
    'kipisi': 'U+F197B',  # 󱥻
    'jasima': 'U+F197F',  # 󱥿
    'akesi': 'U+F1901',  # 󱤁
    'apeja': 'U+F19A1',  # 󱦡
    'kiwen': 'U+F191B',  # 󱤛
    'linja': 'U+F1929',  # 󱤩
    'lukin': 'U+F192E',  # 󱤮
    'monsi': 'U+F1938',  # 󱤸
    'nanpa': 'U+F193D',  # 󱤽
    'nasin': 'U+F193F',  # 󱤿
    'pilin': 'U+F194E',  # 󱥎
    'tenpo': 'U+F196B',  # 󱥫
    'utala': 'U+F1971',  # 󱥱
    'tonsi': 'U+F197E',  # 󱥾
    'epiku': 'U+F1983',  # 󱦃
    'alasa': 'U+F1903',  # 󱤃
    'insa': 'U+F190F',  # 󱤏
    'jaki': 'U+F1910',  # 󱤐
    'jelo': 'U+F1912',  # 󱤒
    'kala': 'U+F1914',  # 󱤔
    'kama': 'U+F1916',  # 󱤕
    'kasi': 'U+F1917',  # 󱤗
    'kili': 'U+F191A',  # 󱤚
    'kule': 'U+F191E',  # 󱤞
    'kute': 'U+F1920',  # 󱤠
    'lape': 'U+F1922',  # 󱤢
    'laso': 'U+F1923',  # 󱤣
    'lawa': 'U+F1924',  # 󱤤
    'lete': 'U+F1926',  # 󱤦
    'lili': 'U+F1928',  # 󱤨
    'lipu': 'U+F192A',  # 󱤪
    'loje': 'U+F192B',  # 󱤫
    'luka': 'U+F192D',  # 󱤭
    'lupa': 'U+F192F',  # 󱤯
    'mama': 'U+F1931',  # 󱤱
    'mani': 'U+F1932',  # 󱤲
    'mije': 'U+F1935',  # 󱤵
    'moku': 'U+F1936',  # 󱤶
    'moli': 'U+F1937',  # 󱤷
    'musi': 'U+F193B',  # 󱤻
    'mute': 'U+F193C',  # 󱤼
    'nasa': 'U+F193E',  # 󱤾
    'nena': 'U+F1940',  # 󱥀
    'nimi': 'U+F1942',  # 󱥂
    'noka': 'U+F1943',  # 󱥃
    'olin': 'U+F1945',  # 󱥅
    'open': 'U+F1947',  # 󱥇
    'pake': 'U+F19A0',  # 󱦠
    'pali': 'U+F1949',  # 󱥉
    'pana': 'U+F194C',  # 󱥌
    'pini': 'U+F1950',  # 󱥐
    'pipi': 'U+F1951',  # 󱥑
    'poka': 'U+F1952',  # 󱥒
    'poki': 'U+F1953',  # 󱥓
    'pona': 'U+F1954',  # 󱥔
    'powe': 'U+F19A3',  # 󱦣
    'sama': 'U+F1956',  # 󱥖
    'seli': 'U+F1957',  # 󱥗
    'selo': 'U+F1958',  # 󱥘
    'seme': 'U+F1959',  # 󱥙
    'sewi': 'U+F195A',  # 󱥚
    'sike': 'U+F195C',  # 󱥜
    'sina': 'U+F195E',  # 󱥞
    'sona': 'U+F1961',  # 󱥡
    'suli': 'U+F1963',  # 󱥣
    'suno': 'U+F1964',  # 󱥤
    'supa': 'U+F1965',  # 󱥥
    'suwi': 'U+F1966',  # 󱥦
    'taso': 'U+F1968',  # 󱥨
    'tawa': 'U+F1969',  # 󱥩
    'telo': 'U+F196A',  # 󱥪
    'toki': 'U+F196C',  # 󱥬
    'tomo': 'U+F196D',  # 󱥭
    'unpa': 'U+F196F',  # 󱥯
    'walo': 'U+F1972',  # 󱥲
    'waso': 'U+F1974',  # 󱥴
    'wawa': 'U+F1975',  # 󱥵
    'weka': 'U+F1976',  # 󱥶
    'wile': 'U+F1977',  # 󱥷
    'leko': 'U+F197C',  # 󱥼
    'soko': 'U+F1981',  # 󱦁
    'meso': 'U+F1982',  # 󱦂
    'meli': 'U+F1933',  # 󱤳
    'anpa': 'U+F1905',  # 󱤅
    'ante': 'U+F1906',  # 󱤆
    'awen': 'U+F1908',  # 󱤈
    'esun': 'U+F190B',  # 󱤋
    'ilo': 'U+F190E',  # 󱤎
    'jan': 'U+F1911',  # 󱤑
    'ken': 'U+F1918',  # 󱤘
    'kon': 'U+F191D',  # 󱤝
    'len': 'U+F1925',  # 󱤥
    'lon': 'U+F192C',  # 󱤬
    'mun': 'U+F193A',  # 󱤺
    'ona': 'U+F1946',  # 󱥆
    'pan': 'U+F194B',  # 󱥋
    'sin': 'U+F195D',  # 󱥝
    'tan': 'U+F1967',  # 󱥧
    'uta': 'U+F1970',  # 󱥰
    'wan': 'U+F1973',  # 󱥳
    'kin': 'U+F1979',  # 󱥹
    'oko': 'U+F197A',  # 󱥺
    'ike': 'U+F190D',  # 󱤍
    'ala': 'U+F1902',  # 󱤂
    'ale': 'U+F1904',  # 󱤄
    'anu': 'U+F1907',  # 󱤇
    'ijo': 'U+F190C',  # 󱤌
    'jo': 'U+F1913',  # 󱤓
    'ko': 'U+F191C',  # 󱤜
    'la': 'U+F1921',  # 󱤡
    'li': 'U+F1927',  # 󱤧
    'ma': 'U+F1930',  # 󱤰
    'mi': 'U+F1934',  # 󱤴
    'mu': 'U+F1939',  # 󱤹
    'ni': 'U+F1941',  # 󱥁
    'pi': 'U+F194D',  # 󱥍
    'pu': 'U+F1955',  # 󱥕
    'tu': 'U+F196E',  # 󱥮
    'ku': 'U+F1988',  # 󱦈
    'en': 'U+F190A',  # 󱤊
    'o': 'U+F1944',  # 󱥄
    'n': 'U+F1986',  # 󱦆
    'a': 'U+F1900',  # 󱤀
    'e': 'U+F1909',  # 󱤉
}
other = {
    '[': 'U+F1990',  # cartouche start
    ']': 'U+F1991',  # cartouche end
    '=': 'U+F1992',  # cartouche extender

    '-': 'U+200D',  # default zero width joiner
    '^': 'U+F1995',  # stacking joiner
    '*': 'U+F1996',  # scaling joiner

    '(': 'U+F1997',  # start left-combining (normal) long glyph
    ')': 'U+F1998',  # end left-combining (normal) long glyph
    '_': 'U+F1999',  # container extender

    '{': 'U+F199A',  # start right-combining (reversed) long glyph
    '}': 'U+F199B',  # end right-combining (reversed) long glyph

    '.': 'U+F199C',  # sitelen pona full stop
    ':': 'U+F199D',  # sitelen pona colon


    ' ': 'U+3000',  # logograph fullwidth space
    '<': 'U+300C',  # 「 start quote
    '>': 'U+300D',  # 」 end quote


    '~~': 'U+FE01',  # variation selector 2
    '~': 'U+FE00',  # variation selector 1
}

re_word = re.compile(r'\w+')

a = ahk.AHK(version='v1')


def copy() -> str:
    a.set_clipboard('')
    a.send('^c')
    a.clip_wait(1)
    return a.get_clipboard()


def paste(text: str = ''):
    if text:
        a.set_clipboard(text)
        a.clip_wait(1)
    a.send('^v')


def cut():
    a.send('^x')


def delete():
    a.send('{Delete}')


def replace(only_nimi=False):
    clipboard = copy()
    words: list[str] = re_word.findall(clipboard)
    items = (nimi if only_nimi else (nimi | other)).items()
    for k, v in items:
        for word in words:
            if k == word:
                clipboard = clipboard.replace(word, word.replace(k, chr(int(v[2:], 16))))
                break
    delete()
    paste(clipboard)


def main():
    a.add_hotkey('!r', replace)
    a.add_hotkey('!+r', lambda: replace(True))
    a.start_hotkeys()
    a.block_forever()


if __name__ == '__main__':
    main()
