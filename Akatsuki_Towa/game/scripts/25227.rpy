label avg25227:
stop music

scene placeholderbackground
window show
with fade_out
play sfx2 "fight_6025.ogg"
c0 '[textdict[1210807]]'
show oc001_01 19 as p1 at mid(-2), light, zorder 5
play sfxvoice "bcv_oc001_hurt_02.ogg"
c13 '[textdict[1210808]]'
hide p1
play sfx2 "other_7082.ogg"
c20173 '[textdict[1210809]]'
show oc002_01 9 as p2 at mid(-3), light, zorder 5
play sfx2 "other_7079.ogg"
play sfxvoice "bcv_oc002_atk_01.ogg"
c23 '[textdict[1210810]]'
return