label avg12237:

play music "ED6103.ogg"
scene avg_bg_038
window show
with fade_in
c9951 '[textdict[1121184]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1121185]]'
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 5)
c13 '[textdict[1121186]]'
$ update_portrait('oc001_01 18', 'p1', [r(-2), dark], 5)
c9951 '[textdict[1121187]]'
c6871 '[textdict[1121188]]'
hide p1
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 5)
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[textdict[1121189]]'
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
c6871 '[textdict[1121190]]'
hide p2
c9953 '[textdict[1121191]]'
c6871 '[textdict[1121192]]'
c9953 '[textdict[1121193]]'
$ update_portrait('oc002_01 13', 'p2', [r(-3), light], 5)
play sfxvoice "avg_vocal_ch03_b.ogg"
c23 '[textdict[1121194]]'
hide p2
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[textdict[1121195]]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
c6871 '[textdict[1121196]]'
return