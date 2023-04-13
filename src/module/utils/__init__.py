import re

unsafeStr = re.compile(r'[\u0001-\u001f\u007f-\u009f\u00ad\u0600-\u0605\u061c\u06dd\u070f\u08e2\u180e\u200b-\u200f\u202a-\u202e\u2060-\u2064\u2066-\u206f\ufdd0-\ufdef\ufeff\ufff9-\ufffb\ufffe\uffff]')
fullWidthDict = [
    ['\\\\', '＼'],
    ['/', '／'],
    [':', '：'],
    ['\\?', '？'],
    ['"', '＂'],
    ['<', '＜'],
    ['>', '＞'],
    ['\\*', '＊'],
    ['\\|', '｜'],
    ['~', '～'],
]
windowsReservedNames = [
    'CON',
    'PRN',
    'AUX',
    'NUL',
    'COM1',
    'LPT1',
    'LPT2',
    'LPT3',
    'COM2',
    'COM3',
    'COM4',
]

def replaceUnsafeStr(str):
    # for name in self.windowsReservedNames:
    #     if str.upper() == name:
    #         return str + 'UnsafeName'
    # str = self.unsafeStr.sub('', str)
    # 把一些特殊字符替换成全角字符
    for index in range(len(fullWidthDict)):
        rule = fullWidthDict[index]
        reg = re.compile(rule[0])
        str = reg.sub(rule[1], str)
    return str
