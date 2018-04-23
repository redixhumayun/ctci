import os

path = os.path.abspath(os.sep) + '/Users/zaidhumayun/Downloads'

if os.path.exists(path):
    os.chdir(path)
    with open('./Game.of.Thrones.S07E05.Eastwatch.1080p.10bit.WEBRip.6CH.x265.HEVC-PSA.mkv', 'rb') as f:
        byte = f.read(32)
        while byte != '':
            print(byte)
