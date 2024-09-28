label avg25090:
stop music

scene placeholderbackground
with fade
play sfx2 "other_7080.ogg"
play sfxvoice "bcv_oc002_hurt_01.ogg"
show oc002_01 3 as c2portrait at centerpos(-3), zorder 5
c23 '[textdict[1210256]]'
play sfxvoice "bcv_oc001_hurt_02.ogg"
hide c2portrait
show oc001_01 19 as c1portrait at centerpos(-2), zorder 5
c13 '[textdict[1210257]]'
hide c1portrait
show oc002_01 12 as c2portrait at centerpos(-3), zorder 5
c23 '[textdict[1210258]]'
hide c2portrait
show oc001_01 4 as c1portrait at centerpos(-2), zorder 5
c13 '[textdict[1210259]]'
menu:
    "[textdict[1214997]]":
        call avg25091
    "[textdict[1215000]]":
        call avg25026
return