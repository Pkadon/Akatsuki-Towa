label avg25295:
stop music

scene placeholderbackground
show oc001_01 19 as p1 at mid(-2), light, zorder 5
window show
with fade_in
play sfx2 "other_7088.ogg"
play sfxvoice "bcv_oc001_hurt_01.ogg"
c13 '[textdict[1211125]]'
hide p1
show oc002_01 4 as p2 at mid(-3), light, zorder 5
play sfxvoice "bcv_oc002_com_01.ogg"
c23 '[textdict[1211126]]'
hide p2
show oc001_01 4 as p1 at mid(-2), light, zorder 5
play sfx2 "elc_5002.ogg"
c13 '[textdict[1211127]]'
return