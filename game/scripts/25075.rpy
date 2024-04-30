label avg25075:
stop music

scene placeholderbackground
with fade
play sfx2 "other_7079.ogg"
play sfxvoice "bcv_oc002_hurt_02.ogg"
show oc002_01 12 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210229)]]'
play sfx2 "fight_6024.ogg"
play sfxvoice "avg_vocal_na23.ogg"
hide c2portrait
show oc001_01 20 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210230)]]'
return