label avg25136:
stop music

scene placeholderbackground
with fade
play sfxvoice "bcv_oc001_hurt_02.ogg"
show oc001_01 9 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[1210417]]'
hide c1portrait
show oc002_01 2 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[1210418]]'
play sfx2 "other_7004.ogg"
hide c2portrait
c00 '[textdict[1210419]]'
show oc001_01 4 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[1210420]]'
play sfxvoice "bcv_oc002_c02_01.ogg"
hide c1portrait
show oc002_01 9 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[1210421]]'
return