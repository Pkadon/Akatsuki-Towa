label avg25144:
stop music

scene placeholderbackground
window show
with fade_in
play sfx2 "other_7068.ogg"
c0 '[textdict[1210456]]'
$ update_portrait('oc002_01 7', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch31.ogg"
c23 '[textdict[1210457]]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na05.ogg"
c13 '[textdict[1210458]]'
return