label avg25229:
stop music

scene placeholderbackground
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 5)
window show
with fade_in
play sfx2 "fight_6024.ogg"
play sfxvoice "avg_vocal_na03.ogg"
c13 '[textdict[1210813]]'
hide p1
play sfx2 "other_7082.ogg"
c20173 '[textdict[1210814]]'
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 5)
play sfx2 "elc_5004.ogg"
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[textdict[1210815]]'
hide p2
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
c13 '[textdict[1210816]]'
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 5)
c23 '[textdict[1210817]]'
return