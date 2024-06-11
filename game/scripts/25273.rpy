label avg25273:
stop music

scene placeholderbackground
with fade
play sfx2 "other_7079.ogg"
show oc001_01 19 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[1211040]]'
play sfx2 "other_7077.ogg"
play sfxvoice "avg_vocal_ch11.ogg"
hide c1portrait
show oc002_01 12 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[1211041]]'
hide c2portrait
show oc001_01 18 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[1211042]]'
menu:
    "[textdict[1214998]]":
        call avg25274
    "[textdict[1214996]]":
        call avg25275
return