label avg10526:

play music "ED6103.ogg"
scene avg_bg_070
$ update_narrator('c0')
window show
with fade_in
play sfx2 "other_7047.ogg"
c0 '[textdict[1152185]]'
scene avg_bg_023
$ update_portrait('uc001_01 1', 'p1255', [l(-2), light, flip], 6)
$ update_narrator('c12551')
with fade
c12551 '[textdict[1152186]]'
$ update_portrait('uc001_01 1', 'p1255', [l(-2), dark, flip], 6)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[1152187]]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('uc001_01 1', 'p1255', [l(-2), light, flip], 6)
c12551 '[textdict[1152188]]'
hide p1
$ update_portrait('uc001_01 1', 'p1255', [l(-2), dark, flip], 6)
$ update_portrait('oc003_01 5', 'p3', [r(-6), light], 5)
play sfxvoice "avg_vocal_ro02.ogg"
c33 '[textdict[1152189]]'
$ update_portrait('oc003_01 5', 'p3', [r(-6), dark], 5)
$ update_portrait('uc001_01 1', 'p1255', [l(-2), light, flip], 6)
c12551 '[textdict[1152190]]'
hide p3
$ update_portrait('uc001_01 1', 'p1255', [l(-2), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1152191]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('uc001_01 1', 'p1255', [l(-2), light, flip], 6)
c12551 '[textdict[1152192]]'
hide p1
$ update_portrait('uc001_01 1', 'p1255', [l(-2), dark, flip], 6)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 5)
c23 '[textdict[1152193]]'
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('uc001_01 1', 'p1255', [l(-2), light, flip], 6)
c12551 '[textdict[1152194]]'
hide p2
$ update_portrait('uc001_01 1', 'p1255', [l(-2), dark, flip], 6)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 5)
play sfxvoice "avg_vocal_ro13.ogg"
c33 '[textdict[1152195]]'
return