label avg25214:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "other_7076.ogg"
play sfxvoice "avg_vocal_na03.ogg"
c13 '[textdict[1210742]]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 5)
c23 '[textdict[1210743]]'
return