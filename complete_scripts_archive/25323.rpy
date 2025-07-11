label avg25323:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 5)
window show
with fade_in
c13 '[textdict[1211246]]'
hide p1
c20243 '[textdict[1211247]]'
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch12.ogg"
c23 '[textdict[1211248]]'
hide p2
c20243 '[textdict[1211249]]'
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na21.ogg"
c13 '[textdict[1211250]]'
hide p1
c20243 '[textdict[1211251]]'
c20243 '[textdict[1211252]]'
$ update_portrait('oc002_01 13', 'p2', [mid(-3), light], 5)
play sfx2 "common_36rewardsp.ogg"
play sfxvoice "avg_vocal_ch09.ogg"
c23 '[textdict[1211253]]'
return