label avg25200:

stop music
scene placeholderbackground
$ update_portrait('uc001_01 2', 'p2022', [mid(-2), light], 6)
$ update_narrator('c20223')
window show
with fade_in
c20223 '[convertstrid(1210676)]'
hide p2022
$ update_portrait('oc001_01 17', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na03.ogg"
c13 '[convertstrid(1210677)]'
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
c23 '[convertstrid(1210678)]'
hide p2
$ update_portrait('uc001_01 1', 'p2022', [mid(-2), light], 6)
c20223 '[convertstrid(1210679)]'
hide p2022
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1210680)]'
hide p1
$ update_portrait('uc001_01 1', 'p2022', [mid(-2), light], 6)
play sfx2 "common_36rewardsp.ogg"
c20223 '[convertstrid(1210681)]'
return