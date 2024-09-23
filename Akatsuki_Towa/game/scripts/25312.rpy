label avg25312:
stop music

scene placeholderbackground
with fade
play sfx2 "other_7007.ogg"
play sfxvoice "bcv_oc002_hurt_02.ogg"
show oc002_01 20 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[1211199]]'
play sfx2 "other_7057.ogg"
hide c2portrait
c00 '[textdict[1211200]]'
c20150 '[textdict[1211201]]'
menu:
    "[textdict[1214995]]":
        call avg25313
    "[textdict[1214996]]":
        call avg25026
return