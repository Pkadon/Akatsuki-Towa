label avg25233:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 19', 'p1', [mid(-2), light], 5)
window show
with fade_in
play sfx2 "fight_6003.ogg"
play sfxvoice "avg_vocal_na07.ogg"
c13 '[textdict[1210829]]'
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 5)
play sfxvoice "bcv_oc002_atk_01.ogg"
c23 '[textdict[1210830]]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na02.ogg"
c13 '[textdict[1210831]]'
return