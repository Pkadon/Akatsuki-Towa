label avg25303:

stop music
scene placeholderbackground
window show
with fade_in
c20283 '[textdict[1211167]]'
$ update_portrait('oc002_01 10', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch17.ogg"
c23 '[textdict[1211168]]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 5)
play sfx2 "other_7088.ogg"
play sfxvoice "avg_vocal_na06.ogg"
c13 '[textdict[1211169]]'
return