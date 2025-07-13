label avg25158:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 5', 'p1', [mid(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "other_7092.ogg"
play sfxvoice "avg_vocal_na19.ogg"
c13 '[textdict[1210502]]'
hide p1
play sfx2 "elc_5004.ogg"
c6123 '[textdict[1210503]]'
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 5)
play sfx2 "other_7080.ogg"
play sfxvoice "bcv_oc002_atk_01.ogg"
c23 '[textdict[1210504]]'
return