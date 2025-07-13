label avg20141:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
c13 '[textdict[1100024]]'
hide p1
$ update_portrait('oc004_01 9', 'p4', [mid(-5), light], 5)
c43 '[textdict[1100025]]'
hide p4
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch07.ogg"
c23 '[textdict[1100026]]'
return