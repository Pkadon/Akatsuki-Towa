label avg25237:
stop music

scene placeholderbackground
window show
with fade_in
play sfx2 "other_7080.ogg"
c0 '[textdict[1210843]]'
c6123 '[textdict[1210844]]'
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[textdict[1210845]]'
hide p2
$ update_portrait('oc001_01 9', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na24.ogg"
c13 '[textdict[1210846]]'
return