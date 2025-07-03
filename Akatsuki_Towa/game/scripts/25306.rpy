label avg25306:
stop music

scene placeholderbackground
with fade
play sfx2 "fight_6015.ogg"
c0 '[textdict[1211180]]'
play sfxvoice "avg_vocal_ch11.ogg"
show oc002_01 12 as p2 at mid(-3), light, zorder 5
c23 '[textdict[1211181]]'
play sfxvoice "bcv_oc001_hurt_02.ogg"
hide p2
show oc001_01 19 as p1 at mid(-2), light, zorder 5
c13 '[textdict[1211182]]'
return