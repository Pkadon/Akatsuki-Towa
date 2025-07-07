label avg25136:
stop music

scene placeholderbackground
with fade
show oc001_01 9 as p1 at mid(-2), light, zorder 5
play sfxvoice "bcv_oc001_hurt_02.ogg"
c13 '[textdict[1210417]]'
hide p1
show oc002_01 2 as p2 at mid(-3), light, zorder 5
c23 '[textdict[1210418]]'
hide p2
play sfx2 "other_7004.ogg"
c0 '[textdict[1210419]]'
show oc001_01 4 as p1 at mid(-2), light, zorder 5
c13 '[textdict[1210420]]'
hide p1
show oc002_01 9 as p2 at mid(-3), light, zorder 5
play sfxvoice "bcv_oc002_c02_01.ogg"
c23 '[textdict[1210421]]'
return