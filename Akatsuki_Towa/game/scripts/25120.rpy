label avg25120:
stop music

scene placeholderbackground
with fade
play sfx2 "fight_6030.ogg"
c6120 '[textdict[1210352]]'
show oc001_01 2 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[1210353]]'
hide c1portrait
show oc002_01 12 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[1210354]]'
play sfxvoice "bcv_oc001_com_01.ogg"
hide c2portrait
show oc001_01 4 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[1210355]]'
return