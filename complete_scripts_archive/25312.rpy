label avg25312:
stop music

scene placeholderbackground
with fade
play sfx2 "other_7007.ogg"
play sfxvoice "bcv_oc002_hurt_02.ogg"
show oc002_01 20 as p2 at mid(-3), light, zorder 5
c23 '[textdict[1211199]]'
play sfx2 "other_7057.ogg"
hide p2
c0 '[textdict[1211200]]'
c20153 '[textdict[1211201]]'
menu:
    extend ""
    "[textdict[1214995]]":
        call avg25313
    "[textdict[1214996]]":
        call avg25026
return