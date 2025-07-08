label avg25273:
stop music

scene placeholderbackground
show oc001_01 19 as p1 at mid(-2), light, zorder 5
window show
with fade_in
play sfx2 "other_7079.ogg"
c13 '[textdict[1211040]]'
hide p1
show oc002_01 12 as p2 at mid(-3), light, zorder 5
play sfx2 "other_7077.ogg"
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[textdict[1211041]]'
hide p2
show oc001_01 18 as p1 at mid(-2), light, zorder 5
c13 '[textdict[1211042]]'
menu:
    extend ""
    "[textdict[1214998]]":
        call avg25274
    "[textdict[1214996]]":
        call avg25275
return