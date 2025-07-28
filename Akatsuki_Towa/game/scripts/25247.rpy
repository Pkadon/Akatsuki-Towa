label avg25247:

stop music
scene placeholderbackground
$ update_narrator('c20183')
window show
with fade_in
play sfx2 "other_7088.ogg"
c20183 '[convertstrid(1210896)]'
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
play sfxvoice "bcv_oc002_atk_01.ogg"
c23 '[convertstrid(1210897)]'
hide p2
play sfx2 "fight_6025.ogg"
c20183 '[convertstrid(1210898)]'
play sfx2 "fight_6026.ogg"
c20183 '[convertstrid(1210899)]'
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na05.ogg"
c13 '[convertstrid(1210900)]'
hide p1
c20183 '[convertstrid(1210901)]'
play sfx2 "other_7086.ogg"
c0 '[convertstrid(1210902)]'
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
play sfx2 "other_7088.ogg"
play sfxvoice "avg_vocal_ch12.ogg"
c23 '[convertstrid(1210903)]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
play sfx2 "common_36rewardsp.ogg"
c13 '[convertstrid(1210904)]'
return