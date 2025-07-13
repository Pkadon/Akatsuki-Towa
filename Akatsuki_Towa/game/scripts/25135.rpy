label avg25135:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 21', 'p1', [mid(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
c13 '[textdict[1210409]]'
hide p1
c20133 '[textdict[1210410]]'
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch10.ogg"
c23 '[textdict[1210411]]'
hide p2
c20133 '[textdict[1210412]]'
$ update_portrait('oc002_01 13', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch05.ogg"
c23 '[textdict[1210413]]'
hide p2
play sfx2 "other_7039.ogg"
c20133 '[textdict[1210414]]'
$ update_portrait('oc001_01 6', 'p1', [mid(-2), light], 5)
play sfx2 "common_35rewardholy.ogg"
play sfxvoice "avg_vocal_na17.ogg"
c13 '[textdict[1210415]]'
return