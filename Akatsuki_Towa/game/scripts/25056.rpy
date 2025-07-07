label avg25056:
stop music

scene placeholderbackground
with fade
show oc001_01 18 as p1 at mid(-2), light, zorder 5
play sfxvoice "avg_vocal_na15.ogg"
c13 '[textdict[1210163]]'
hide p1
show oc002_01 2 as p2 at mid(-3), light, zorder 5
play sfxvoice "avg_vocal_ch12.ogg"
c23 '[textdict[1210164]]'
hide p2
show oc001_01 4 as p1 at mid(-2), light, zorder 5
c13 '[textdict[1210165]]'
menu:
    extend ""
    "[textdict[1214997]]":
        call avg25057
    "[textdict[1215000]]":
        call avg25026
return