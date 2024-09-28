label avg25233:
stop music

scene placeholderbackground
with fade
play sfx2 "fight_6003.ogg"
play sfxvoice "avg_vocal_na07.ogg"
show oc001_01 19 as c1portrait at centerpos(-2), zorder 5
c13 '[textdict[1210829]]'
play sfxvoice "bcv_oc002_atk_01.ogg"
hide c1portrait
show oc002_01 9 as c2portrait at centerpos(-3), zorder 5
c23 '[textdict[1210830]]'
play sfxvoice "avg_vocal_na02.ogg"
hide c2portrait
show oc001_01 7 as c1portrait at centerpos(-2), zorder 5
c13 '[textdict[1210831]]'
return