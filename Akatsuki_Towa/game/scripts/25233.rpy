label avg25233:
stop music

scene placeholderbackground
show oc001_01 19 as p1 at mid(-2), light, zorder 5
window show
with fade_in
play sfx2 "fight_6003.ogg"
play sfxvoice "avg_vocal_na07.ogg"
c13 '[textdict[1210829]]'
hide p1
show oc002_01 9 as p2 at mid(-3), light, zorder 5
play sfxvoice "bcv_oc002_atk_01.ogg"
c23 '[textdict[1210830]]'
hide p2
show oc001_01 7 as p1 at mid(-2), light, zorder 5
play sfxvoice "avg_vocal_na02.ogg"
c13 '[textdict[1210831]]'
return