label avg25039:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 11', 'p2', [mid(-3), light], 5)
$ update_narrator('c23')
window show
with fade_in
c23 '[convertstrid(1210099)]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 5)
c13 '[convertstrid(1210100)]'
hide p1
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 5)
play sfx2 "common_36rewardsp.ogg"
play sfxvoice "bcv_oc002_win_02.ogg"
c23 '[convertstrid(1210101)]'
return