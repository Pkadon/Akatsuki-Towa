label avg25307:
stop music

scene placeholderbackground
show oc002_01 4 as p2 at mid(-3), light, zorder 5
with fade
play sfx2 "other_7079.ogg"
c23 '[textdict[1211183]]'
hide p2
show oc001_01 18 as p1 at mid(-2), light, zorder 5
c13 '[textdict[1211184]]'
menu:
    extend ""
    "[textdict[1214998]]":
        call avg25308
    "[textdict[1214996]]":
        call avg25309
return