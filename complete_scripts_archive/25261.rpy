label avg25261:
stop music

scene placeholderbackground
with fade
play sfx2 "fight_6020.ogg"
play sfxvoice "bcv_oc001_hurt_02.ogg"
show oc001_01 19 as c1portrait at centerpos(-2), zorder 5
c13 '[textdict[1210974]]'
play sfxvoice "avg_vocal_ch23.ogg"
hide c1portrait
show oc002_01 11 as c2portrait at centerpos(-3), zorder 5
c23 '[textdict[1210975]]'
return