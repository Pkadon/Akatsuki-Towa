label avg25305:
stop music

scene placeholderbackground
with fade
play sfx2 "other_7080.ogg"
c0 '[textdict[1211175]]'
play sfxvoice "bcv_oc002_hurt_02.ogg"
show oc002_01 12 as c2portrait at centerpos(-3), zorder 5
c23 '[textdict[1211176]]'
hide c2portrait
show oc001_01 4 as c1portrait at centerpos(-2), zorder 5
c13 '[textdict[1211177]]'
play sfxvoice "bcv_oc002_arts_03.ogg"
hide c1portrait
show oc002_01 9 as c2portrait at centerpos(-3), zorder 5
c23 '[textdict[1211178]]'
hide c2portrait
show oc001_01 4 as c1portrait at centerpos(-2), zorder 5
c13 '[textdict[1211179]]'
return