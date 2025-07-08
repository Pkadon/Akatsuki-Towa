label avg25129:
stop music

scene placeholderbackground
window show
with fade_in
play sfx2 "other_7004.ogg"
c0 '[textdict[1210386]]'
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na06.ogg"
c13 '[textdict[1210387]]'
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 5)
play sfxvoice "bcv_oc002_arts_03.ogg"
c23 '[textdict[1210388]]'
return