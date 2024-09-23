label avg25295:
stop music

scene placeholderbackground
with fade
play sfx2 "other_7088.ogg"
play sfxvoice "bcv_oc001_hurt_01.ogg"
show oc001_01 19 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[1211125]]'
play sfxvoice "bcv_oc002_com_01.ogg"
hide c1portrait
show oc002_01 4 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[1211126]]'
play sfx2 "elc_5002.ogg"
hide c2portrait
show oc001_01 4 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[1211127]]'
return