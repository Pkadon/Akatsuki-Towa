label avg25265:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 17', 'p1', [mid(-2), light], 5)
window show
with fade_in
play sfx2 "other_7050.ogg"
play sfxvoice "avg_vocal_na06.ogg"
c13 '[textdict[1210989]]'
hide p1
$ update_portrait('oc002_01 7', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch31.ogg"
c23 '[textdict[1210990]]'
hide p2
play sfx2 "other_7037.ogg"
c20133 '[textdict[1210991]]'
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na21.ogg"
c13 '[textdict[1210992]]'
hide p1
c20133 '[textdict[1210993]]'
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na05.ogg"
c13 '[textdict[1210994]]'
return