label avg25261:
stop music

scene placeholderbackground
show oc001_01 19 as p1 at mid(-2), light, zorder 5
window show
with fade_in
play sfx2 "fight_6020.ogg"
play sfxvoice "bcv_oc001_hurt_02.ogg"
c13 '[textdict[1210974]]'
hide p1
show oc002_01 11 as p2 at mid(-3), light, zorder 5
play sfxvoice "avg_vocal_ch23.ogg"
c23 '[textdict[1210975]]'
return