# 당대표 - 죽이기, 보호하기, 탄핵소추안
# 보좌관 - 추적하기 (연속X)
# 국힘-민주당-국힘 순서

alive = [
    [True, True], # A A' (국힘 - 민주당)
    [True, True]  # B B'
]

log = []

mpcard = ['kill 10', 'kill 11', 'save 00', 'save 01', 'impeach 10', 'dansik 00', 'skip 00']
mhcard = ['track 10', 'track 11', 'skip 01']
gpcard = ['kill 00', 'kill 01', 'save 10', 'save 11', 'impeach 00', 'dansik 10', 'skip 10']
ghcard = ['track 00', 'track 01', 'skip 11']

def check_win():
    if not alive[0][0] and not alive[1][0]:
        return 0 # 무승부
    elif not alive[0][0]:
        return -1 # 민주당 승리 
    elif not alive[1][0]:
        return 1 # 국힘 승리
    else:
        return 0 # 게임 진행