label avg25090:
stop music

scene placeholderbackground
show oc002_01 3 as p2 at mid(-3), light, zorder 5
window show
with fade_out
play sfx2 "other_7080.ogg"
play sfxvoice "bcv_oc002_hurt_01.ogg"
c23 '[textdict[1210256]]'
hide p2
show oc001_01 19 as p1 at mid(-2), light, zorder 5
play sfxvoice "bcv_oc001_hurt_02.ogg"
c13 '[textdict[1210257]]'
hide p1
show oc002_01 12 as p2 at mid(-3), light, zorder 5
c23 '[textdict[1210258]]'
hide p2
show oc001_01 4 as p1 at mid(-2), light, zorder 5
c13 '[textdict[1210259]]'
menu:
    extend ""
    "[textdict[1214997]]":
        call avg25091
    "[textdict[1215000]]":
        call avg25026
return