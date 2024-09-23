label avg25061:
stop music

scene placeholderbackground
with fade
show uc001_01 2 as c2004portrait at centerpos(-2), zorder 5
c20042 '[textdict[1210177]]'
hide c2004portrait
show uc001_02 1 as c2005portrait at centerpos(6), zorder 5
c20052 '[textdict[1210178]]'
play sfx2 "other_7004.ogg"
play sfxvoice "avg_vocal_ch12.ogg"
hide c2005portrait
show oc002_01 2 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[1210179]]'
play sfxvoice "avg_vocal_ch07.ogg"
hide c2portrait
show oc002_01 5 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[1210180]]'
menu:
    "[textdict[1214997]]":
        call avg25062
    "[textdict[1215000]]":
        call avg25026
return