label avg25106:
stop music

scene placeholderbackground
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 5)
window show
with fade_in
play sfxvoice "avg_vocal_ch05.ogg"
c23 '[textdict[1210301]]'
hide p2
c20073 '[textdict[1210302]]'
$ update_portrait('oc001_01 6', 'p1', [mid(-2), light], 5)
c13 '[textdict[1210303]]'
hide p1
play sfx2 "other_7051.ogg"
c20073 '[textdict[1210304]]'
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 5)
play sfx2 "other_7092.ogg"
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[textdict[1210305]]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na05.ogg"
c13 '[textdict[1210306]]'
hide p1
c20073 '[textdict[1210307]]'
c20073 '[textdict[1210308]]'
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 5)
play sfx2 "common_36rewardsp.ogg"
play sfxvoice "avg_vocal_na06.ogg"
c13 '[textdict[1210309]]'
return