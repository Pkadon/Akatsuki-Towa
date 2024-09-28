label avg25227:
stop music

scene placeholderbackground
with fade
play sfx2 "fight_6025.ogg"
c0 '[textdict[1210807]]'
play sfxvoice "bcv_oc001_hurt_02.ogg"
show oc001_01 19 as c1portrait at centerpos(-2), zorder 5
c13 '[textdict[1210808]]'
play sfx2 "other_7082.ogg"
hide c1portrait
c20173 '[textdict[1210809]]'
play sfx2 "other_7079.ogg"
play sfxvoice "bcv_oc002_atk_01.ogg"
show oc002_01 9 as c2portrait at centerpos(-3), zorder 5
c23 '[textdict[1210810]]'
return