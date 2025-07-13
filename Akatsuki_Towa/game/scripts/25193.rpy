label avg25193:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 5)
$ update_narrator('c23')
window show
with fade_in
play sfxvoice "avg_vocal_ch05.ogg"
c23 '[textdict[1210647]]'
hide p2
$ update_portrait('oc001_01 24', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na20.ogg"
c13 '[textdict[1210648]]'
hide p1
c20133 '[textdict[1210649]]'
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch04.ogg"
c23 '[textdict[1210650]]'
hide p2
c20133 '[textdict[1210651]]'
return