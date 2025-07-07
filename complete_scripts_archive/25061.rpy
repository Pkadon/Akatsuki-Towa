label avg25061:
stop music

scene placeholderbackground
show uc001_01 2 as p2004 at mid(-2), light, zorder 5
window show
with fade_out
c20043 '[textdict[1210177]]'
hide p2004
show uc001_02 1 as p2005 at mid(6), light, zorder 5
c20053 '[textdict[1210178]]'
hide p2005
show oc002_01 2 as p2 at mid(-3), light, zorder 5
play sfx2 "other_7004.ogg"
play sfxvoice "avg_vocal_ch12.ogg"
c23 '[textdict[1210179]]'
hide p2
show oc002_01 5 as p2 at mid(-3), light, zorder 5
play sfxvoice "avg_vocal_ch07.ogg"
c23 '[textdict[1210180]]'
menu:
    extend ""
    "[textdict[1214997]]":
        call avg25062
    "[textdict[1215000]]":
        call avg25026
return