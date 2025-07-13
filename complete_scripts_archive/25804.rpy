label avg25804:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 5)
$ update_narrator('c23')
window show
with fade_in
c23 '[textdict[1211259]]'
hide p2
$ update_portrait('oc001_01 11', 'p1', [mid(-2), light], 5)
play sfx2 "fight_6025.ogg"
play sfxvoice "avg_vocal_na03.ogg"
c13 '[textdict[1211260]]'
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 5)
play sfx2 "fight_6026.ogg"
c13 '[textdict[1211261]]'
$ update_portrait('oc001_01 5', 'p1', [mid(-2), light], 5)
play sfx2 "other_7034.ogg"
play sfxvoice "bcv_oc001_win_02.ogg"
c13 '[textdict[1211262]]'
return