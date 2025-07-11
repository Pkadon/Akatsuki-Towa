label avg25218:

scene placeholderbackground
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 5)
window show
with fade_in
play sfx2 "fight_6020.ogg"
play sfxvoice "bcv_oc002_hurt_02.ogg"
c23 '[textdict[1210755]]'
hide p2
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
c13 '[textdict[1210756]]'
hide p1
$ update_portrait('oc002_01 21', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch25.ogg"
c23 '[textdict[1210757]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na04.ogg"
c13 '[textdict[1210758]]'
return