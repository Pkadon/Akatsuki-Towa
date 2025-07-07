label avg25069:
stop music

scene placeholderbackground
show oc002_01 2 as p2 at mid(-3), light, zorder 5
with fade
play sfxvoice "avg_vocal_ch12.ogg"
c23 '[textdict[1210220]]'
hide p2
show oc001_01 4 as p1 at mid(-2), light, zorder 5
c13 '[textdict[1210221]]'
menu:
    extend ""
    "[textdict[1214997]]":
        call avg25070
    "[textdict[1215000]]":
        call avg25026
return