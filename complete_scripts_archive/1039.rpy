label avg1039:

play music "ed7201.ogg"
scene avg_bg_010
$ update_portrait('sc051_01 4', 'p58', [l(-32), light, flip], 6)
$ update_narrator('c581')
window show
with fade_in
c581 '[textdict[2100620]]'
$ update_portrait('sc051_01 4', 'p58', [l(-32), dark, flip], 6)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 5)
c23 '[textdict[2100621]]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('sc051_01 4', 'p58', [l(-32), light, flip], 6)
c581 '[textdict[2100622]]'
$ update_portrait('sc051_01 4', 'p58', [l(-32), dark, flip], 6)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 5)
c23 '[textdict[2100623]]'
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('sc051_01 4', 'p58', [l(-32), light, flip], 6)
c581 '[textdict[2100624]]'
hide p2
$ update_portrait('sc051_01 4', 'p58', [l(-32), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[2100625]]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc051_01 4', 'p58', [l(-32), light, flip], 6)
c581 '[textdict[2100626]]'
return