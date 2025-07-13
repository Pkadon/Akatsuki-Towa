label avg25246:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 6', 'p1', [mid(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
play sfxvoice "avg_vocal_na16.ogg"
c13 '[textdict[1210890]]'
hide p1
c20243 '[textdict[1210891]]'
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch29.ogg"
c23 '[textdict[1210892]]'
hide p2
c20243 '[textdict[1210893]]'
$ update_portrait('oc001_01 21', 'p1', [mid(-2), light], 5)
play sfx2 "common_36rewardsp.ogg"
c13 '[textdict[1210894]]'
return