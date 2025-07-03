label avg25305:
stop music

scene placeholderbackground
with fade
play sfx2 "other_7080.ogg"
c0 '[textdict[1211175]]'
play sfxvoice "bcv_oc002_hurt_02.ogg"
show oc002_01 12 as p2 at mid(-3), light, zorder 5
c23 '[textdict[1211176]]'
hide p2
show oc001_01 4 as p1 at mid(-2), light, zorder 5
c13 '[textdict[1211177]]'
play sfxvoice "bcv_oc002_arts_03.ogg"
hide p1
show oc002_01 9 as p2 at mid(-3), light, zorder 5
c23 '[textdict[1211178]]'
hide p2
show oc001_01 4 as p1 at mid(-2), light, zorder 5
c13 '[textdict[1211179]]'
return