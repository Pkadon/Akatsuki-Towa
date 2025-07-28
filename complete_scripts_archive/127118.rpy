label avg127118:

play music "ED6202.ogg"
scene avg_bg_010
$ update_narrator('c0')
window show
with fade_in
c0 '[convertstrid(1179502)]'
$ update_portrait('oc002_01 15', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1179503)]'
$ update_portrait('oc002_01 15', 'p2', [r(-3), dark], 5)
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
c13041 '[convertstrid(1179504)]'
hide p2
$ update_portrait('st061_01 1', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1179505)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1179506)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 5', 'p1304', [l(-2), light, flip], 6)
c13041 '[convertstrid(1179507)]'
return