label avg25138:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 5)
window show
with fade_in
c13 '[textdict[1210425]]'
hide p1
$ update_portrait('oc002_01 7', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch31.ogg"
c23 '[textdict[1210426]]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na02.ogg"
c13 '[textdict[1210427]]'
hide p1
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 5)
play sfx2 "other_7092.ogg"
play sfxvoice "avg_vocal_ch08.ogg"
c23 '[textdict[1210428]]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 5)
c13 '[textdict[1210429]]'
hide p1
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 5)
play sfx2 "common_35rewardholy.ogg"
play sfxvoice "avg_vocal_ch07.ogg"
c23 '[textdict[1210430]]'
return