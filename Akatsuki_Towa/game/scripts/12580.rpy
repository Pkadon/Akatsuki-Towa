label avg12580:

play music "ED6523.ogg"
scene avg_bg_080
$ update_portrait('oc001_01 14', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1155388)]'
$ update_portrait('oc001_01 14', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1155389)]'
hide p2
$ update_portrait('oc003_01 20', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1155390)]'
hide p3
$ update_portrait('sc021_01 1', 'p29', [l_entrance(-17), light, flip], 6)
c291 '[convertstrid(1155391)]'
hide p1
$ update_portrait('sc021_01 1', 'p29', [l(-17), dark, flip], 5)
$ update_portrait('oc004_01 20', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1155392)]'
$ update_portrait('oc004_01 20', 'p4', [r(-5), dark], 5)
$ update_portrait('sc021_01 1', 'p29', [l(-17), light, flip], 6)
c291 '[convertstrid(1155393)]'
hide p4
$ update_portrait('sc021_01 1', 'p29', [l(-17), dark, flip], 5)
$ update_portrait('oc002_01 15', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1155394)]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1155395)]'
hide p29
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1155396)]'
return