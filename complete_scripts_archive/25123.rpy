label avg25123:
stop music

scene placeholderbackground
with fade
show oc001_01 2 as p1 at mid(-2), light, zorder 5
c13 '[textdict[1210367]]'
play sfxvoice "avg_vocal_ch12.ogg"
hide p1
show oc002_01 2 as p2 at mid(-3), light, zorder 5
c23 '[textdict[1210368]]'
hide p2
show oc001_01 4 as p1 at mid(-2), light, zorder 5
c13 '[textdict[1210369]]'
menu:
    extend ""
    "[textdict[1214997]]":
        call avg25124
    "[textdict[1214996]]":
        call avg25026
return