label avg25286:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 5)
$ update_narrator('c23')
window show
with fade_in
play sfxvoice "avg_vocal_ch07.ogg"
c23 '[textdict[1211091]]'
hide p2
$ update_portrait('oc001_01 23', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na03.ogg"
c13 '[textdict[1211092]]'
hide p1
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 5)
play sfx2 "other_7059.ogg"
c23 '[textdict[1211093]]'
hide p2
play sfx2 "other_7092.ogg"
c0 '[textdict[1211094]]'
$ update_portrait('oc002_01 17', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch21.ogg"
c23 '[textdict[1211095]]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 5)
play sfx2 "common_36rewardsp.ogg"
play sfxvoice "avg_vocal_na02.ogg"
c13 '[textdict[1211096]]'
return