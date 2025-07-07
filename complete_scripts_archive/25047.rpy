label avg25047:
stop music

scene placeholderbackground
show uc001_02 3 as p2002 at mid(6), light, zorder 5
with fade
c20023 '[textdict[1210120]]'
hide p2002
show oc002_01 2 as p2 at mid(-3), light, zorder 5
play sfxvoice "avg_vocal_ch12.ogg"
c23 '[textdict[1210121]]'
hide p2
show uc001_02 2 as p2002 at mid(6), light, zorder 5
c20023 '[textdict[1210122]]'
menu:
    extend ""
    "[textdict[1214999]]":
        call avg25048
    "[textdict[1215000]]":
        call avg25000
return