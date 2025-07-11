label avg25187:

scene placeholderbackground
window show
with fade_in
play sfx2 "other_7092.ogg"
c6123 '[textdict[1210620]]'
play sfx2 "common_36rewardsp.ogg"
c0 '[textdict[1210621]]'
$ update_portrait('oc001_01 17', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na06.ogg"
c13 '[textdict[1210622]]'
hide p1
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch08.ogg"
c23 '[textdict[1210623]]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na02.ogg"
c13 '[textdict[1210624]]'
return