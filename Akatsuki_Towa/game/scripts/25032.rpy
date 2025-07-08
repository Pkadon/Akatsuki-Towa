label avg25032:
stop music

scene placeholderbackground
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 5)
window show
with fade_in
play sfx2 "other_7086.ogg"
play sfxvoice "avg_vocal_na05.ogg"
c13 '[textdict[1210078]]'
hide p1
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 5)
play sfx2 "fight_6025.ogg"
c23 '[textdict[1210079]]'
hide p2
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 5)
play sfx2 "other_7034.ogg"
c23 '[textdict[1210080]]'
hide p2
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch07.ogg"
c23 '[textdict[1210081]]'
hide p2
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 5)
c13 '[textdict[1210082]]'
return