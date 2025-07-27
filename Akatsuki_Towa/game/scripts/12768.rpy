label avg12768:

play music "ed6564.ogg"
scene placeholderbackground
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 5)
$ update_narrator('c23')
window show
with fade_in
c23 '[convertstrid(1174753)]'
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1174754)]'
hide p2
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1174755)]'
hide p4
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 2', 'p1304', [l(-2), light, flip], 6)
c13041 '[convertstrid(1174756)]'
hide p1
$ update_portrait('st061_01 2', 'p1304', [l(-2), dark, flip], 6)
$ update_portrait('oc003_01 9', 'p3', [r(-6), light], 5)
c33 '[convertstrid(1174757)]'
return