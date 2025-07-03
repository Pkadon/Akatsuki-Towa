label avg25295:
stop music

scene placeholderbackground
with fade
play sfx2 "other_7088.ogg"
play sfxvoice "bcv_oc001_hurt_01.ogg"
show oc001_01 19 as p1 at mid(-2), light, zorder 5
c13 '[textdict[1211125]]'
play sfxvoice "bcv_oc002_com_01.ogg"
hide p1
show oc002_01 4 as p2 at mid(-3), light, zorder 5
c23 '[textdict[1211126]]'
play sfx2 "elc_5002.ogg"
hide p2
show oc001_01 4 as p1 at mid(-2), light, zorder 5
c13 '[textdict[1211127]]'
return