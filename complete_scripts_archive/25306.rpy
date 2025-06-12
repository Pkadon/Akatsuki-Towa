label avg25306:
stop music

scene placeholderbackground
with fade
play sfx2 "fight_6015.ogg"
c0 '[textdict[1211180]]'
play sfxvoice "avg_vocal_ch11.ogg"
show oc002_01 12 as c2portrait at centerpos(-3), zorder 5
c23 '[textdict[1211181]]'
play sfxvoice "bcv_oc001_hurt_02.ogg"
hide c2portrait
show oc001_01 19 as c1portrait at centerpos(-2), zorder 5
c13 '[textdict[1211182]]'
return