label avg25095:

scene placeholderbackground
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 5)
window show
with fade_in
play sfxvoice "avg_vocal_na05.ogg"
c13 '[textdict[1210267]]'
hide p1
$ update_portrait('oc002_01 13', 'p2', [mid(-3), light], 5)
play sfx2 "common_36rewardsp.ogg"
play sfxvoice "avg_vocal_ch05.ogg"
c23 '[textdict[1210268]]'
return