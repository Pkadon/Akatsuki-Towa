label avg25232:
stop music

scene placeholderbackground
show oc002_01 12 as p2 at mid(-3), light, zorder 5
window show
with fade_out
play sfx2 "fight_6024.ogg"
c23 '[textdict[1210826]]'
hide p2
show oc001_01 19 as p1 at mid(-2), light, zorder 5
play sfxvoice "bcv_oc001_hurt_02.ogg"
c13 '[textdict[1210827]]'
hide p1
show oc002_01 4 as p2 at mid(-3), light, zorder 5
c23 '[textdict[1210828]]'
return