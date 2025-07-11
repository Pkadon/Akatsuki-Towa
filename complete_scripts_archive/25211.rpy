label avg25211:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
window show
with fade_in
play sfx2 "other_7059.ogg"
c13 '[textdict[1210732]]'
hide p1
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 5)
play sfx2 "common_35rewardholy.ogg"
play sfxvoice "avg_vocal_ch07.ogg"
c23 '[textdict[1210733]]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 5)
c13 '[textdict[1210734]]'
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 5)
play sfxvoice "bcv_oc002_arts_03.ogg"
c23 '[textdict[1210735]]'
hide p2
$ update_portrait('oc001_01 6', 'p1', [mid(-2), light], 5)
play sfx2 "common_36rewardsp.ogg"
play sfxvoice "avg_vocal_na20.ogg"
c13 '[textdict[1210736]]'
return