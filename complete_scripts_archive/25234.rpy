label avg25234:

stop music
scene placeholderbackground
$ update_narrator('c6123')
window show
with fade_in
play sfx2 "other_7092.ogg"
c6123 '[textdict[1210832]]'
play sfx2 "common_36rewardsp.ogg"
c0 '[textdict[1210833]]'
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch05.ogg"
c23 '[textdict[1210834]]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 5)
play sfx2 "common_35rewardholy.ogg"
play sfxvoice "avg_vocal_na05.ogg"
c13 '[textdict[1210835]]'
return