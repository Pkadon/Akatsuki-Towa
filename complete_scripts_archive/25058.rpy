label avg25058:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
window show
with fade_in
c13 '[textdict[1210167]]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 5)
c23 '[textdict[1210168]]'
hide p2
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 5)
c13 '[textdict[1210169]]'
hide p1
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch24.ogg"
c23 '[textdict[1210170]]'
return