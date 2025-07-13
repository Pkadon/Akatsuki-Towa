label avg25200:

stop music
scene placeholderbackground
$ update_portrait('uc001_01 2', 'p2022', [mid(-2), light], 5)
$ update_narrator('c20223')
window show
with fade_in
c20223 '[textdict[1210676]]'
hide p2022
$ update_portrait('oc001_01 17', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na03.ogg"
c13 '[textdict[1210677]]'
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 5)
c23 '[textdict[1210678]]'
hide p2
$ update_portrait('uc001_01 1', 'p2022', [mid(-2), light], 5)
c20223 '[textdict[1210679]]'
hide p2022
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 5)
c13 '[textdict[1210680]]'
hide p1
$ update_portrait('uc001_01 1', 'p2022', [mid(-2), light], 5)
play sfx2 "common_36rewardsp.ogg"
c20223 '[textdict[1210681]]'
return