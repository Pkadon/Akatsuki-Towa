label avg25205:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 5)
$ update_narrator('c23')
window show
with fade_in
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[textdict[1210700]]'
hide p2
$ update_portrait('oc001_01 19', 'p1', [mid(-2), light], 5)
play sfx2 "other_7088.ogg"
c13 '[textdict[1210701]]'
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 5)
play sfxvoice "bcv_oc002_arts_03.ogg"
c23 '[textdict[1210702]]'
return