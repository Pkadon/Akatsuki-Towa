label avg25306:
stop music

scene placeholderbackground
window show
with fade_in
play sfx2 "fight_6015.ogg"
c0 '[textdict[1211180]]'
show oc002_01 12 as p2 at mid(-3), light, zorder 5
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[textdict[1211181]]'
hide p2
show oc001_01 19 as p1 at mid(-2), light, zorder 5
play sfxvoice "bcv_oc001_hurt_02.ogg"
c13 '[textdict[1211182]]'
return