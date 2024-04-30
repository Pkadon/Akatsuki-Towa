label avg25142:
stop music

scene placeholderbackground
with fade
play sfx2 "other_7092.ogg"
c00 '[textdict[str(1210444)]]'
play sfxvoice "avg_vocal_ch08.ogg"
show oc002_01 14 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210445)]]'
hide c2portrait
show oc001_01 8 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210446)]]'
play sfxvoice "avg_vocal_ch07.ogg"
hide c1portrait
show oc002_01 5 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210447)]]'
play sfxvoice "avg_vocal_na10.ogg"
hide c2portrait
show oc001_01 4 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210448)]]'
play sfxvoice "avg_vocal_ch04.ogg"
hide c1portrait
show oc002_01 14 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210449)]]'
hide c2portrait
show oc001_01 17 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210450)]]'
menu:
    "[textdict[str(1210451)]]":
        call avg25144
    "[textdict[str(1210452)]]":
        call avg25145
    "[textdict[str(1210453)]]":
        call avg25143
return