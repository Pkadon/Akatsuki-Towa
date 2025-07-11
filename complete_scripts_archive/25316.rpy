label avg25316:

stop music
scene placeholderbackground
window show
with fade_in
play sfx2 "other_7092.ogg"
c6123 '[textdict[1211221]]'
c6123 '[textdict[1211222]]'
play sfx2 "other_7092.ogg"
c0 '[textdict[1211223]]'
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[textdict[1211224]]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na03.ogg"
c13 '[textdict[1211225]]'
return