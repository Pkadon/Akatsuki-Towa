label avg12584:

play music "ed7151.ogg"
scene avg_bg_080
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
window show
with fade_in
c21 '[convertstrid(1155435)]'
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1155436)]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc021_01 2', 'p29', [l(-17), light, flip], 6)
c291 '[convertstrid(1155437)]'
$ update_portrait('sc021_01 2', 'p29', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1155438)]'
hide p29
hide p1
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
$ update_narrator('c41')
with fade
c41 '[convertstrid(1155439)]'
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1155440)]'
hide p4
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
play sfx2 "other_7080.ogg"
c31 '[convertstrid(1155441)]'
return