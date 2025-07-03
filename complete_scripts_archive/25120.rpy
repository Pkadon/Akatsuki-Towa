label avg25120:
stop music

scene placeholderbackground
with fade
play sfx2 "fight_6030.ogg"
c6123 '[textdict[1210352]]'
show oc001_01 2 as p1 at mid(-2), light, zorder 5
c13 '[textdict[1210353]]'
hide p1
show oc002_01 12 as p2 at mid(-3), light, zorder 5
c23 '[textdict[1210354]]'
play sfxvoice "bcv_oc001_com_01.ogg"
hide p2
show oc001_01 4 as p1 at mid(-2), light, zorder 5
c13 '[textdict[1210355]]'
return