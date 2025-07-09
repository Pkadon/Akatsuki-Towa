label avg25078:
stop music

scene placeholderbackground
$ update_portrait('oc002_01 14', 'p2', [mid(-3), light], 5)
window show
with fade_in
play sfx2 "fight_6025.ogg"
play sfxvoice "avg_vocal_ch06.ogg"
c23 '[textdict[1210235]]'
hide p2
$ update_portrait('oc001_01 11', 'p1', [mid(-2), light], 5)
c13 '[textdict[1210236]]'
$ update_portrait('oc001_01 5', 'p1', [mid(-2), light], 5)
play sfx2 "common_36rewardsp.ogg"
play sfxvoice "avg_vocal_na19.ogg"
c13 '[textdict[1210237]]'
return