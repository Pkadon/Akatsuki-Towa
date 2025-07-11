label avg25249:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
window show
with fade_in
play sfx2 "other_7088.ogg"
play sfxvoice "avg_vocal_na04.ogg"
c13 '[textdict[1210909]]'
hide p1
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 5)
c23 '[textdict[1210910]]'
hide p2
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na03.ogg"
c13 '[textdict[1210911]]'
hide p1
$ update_portrait('oc002_01 16', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch23.ogg"
c23 '[textdict[1210912]]'
return