label avg25185:

stop music
scene placeholderbackground
window show
with fade_in
play sfx2 "other_7092.ogg"
c6123 '[textdict[1210612]]'
c6123 '[textdict[1210613]]'
play sfx2 "other_7092.ogg"
c0 '[textdict[1210614]]'
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[textdict[1210615]]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na05.ogg"
c13 '[textdict[1210616]]'
return