label avg25177:

scene placeholderbackground
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 5)
window show
with fade_in
play sfx2 "fight_6025.ogg"
play sfxvoice "avg_vocal_ch08.ogg"
c23 '[textdict[1210569]]'
hide p2
$ update_portrait('oc001_01 23', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na03.ogg"
c13 '[textdict[1210570]]'
return