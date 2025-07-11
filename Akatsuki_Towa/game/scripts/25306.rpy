label avg25306:

scene placeholderbackground
window show
with fade_in
play sfx2 "fight_6015.ogg"
c0 '[textdict[1211180]]'
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[textdict[1211181]]'
hide p2
$ update_portrait('oc001_01 19', 'p1', [mid(-2), light], 5)
play sfxvoice "bcv_oc001_hurt_02.ogg"
c13 '[textdict[1211182]]'
return