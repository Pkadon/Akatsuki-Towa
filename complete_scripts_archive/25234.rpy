label avg25234:

stop music
scene placeholderbackground
$ update_narrator('c6123')
window show
with fade_in
play sfx2 "other_7092.ogg"
c6123 '[convertstrid(1210832)]'
play sfx2 "common_36rewardsp.ogg"
c0 '[convertstrid(1210833)]'
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch05.ogg"
c23 '[convertstrid(1210834)]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
play sfx2 "common_35rewardholy.ogg"
play sfxvoice "avg_vocal_na05.ogg"
c13 '[convertstrid(1210835)]'
return