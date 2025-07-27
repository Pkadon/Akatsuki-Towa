label avg12579:

play music "ED6523.ogg"
scene avg_bg_080
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1155375)]'
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
c12611 '[convertstrid(1155376)]'
c12611 '[convertstrid(1155377)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1155378)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 6', 'p2', [l(-3), l_shake, light, flip], 6)
c21 '[convertstrid(1155379)]'
hide p2
hide p1
$ update_portrait('sc021_01 1', 'p29', [l(-17), light, flip], 6)
$ update_narrator('c291')
with fade
c291 '[convertstrid(1155380)]'
$ update_portrait('sc021_01 1', 'p29', [l(-17), dark, flip], 6)
$ update_portrait('oc002_01 14', 'p2', [r(-3), light], 5)
c23 '[convertstrid(1155381)]'
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('sc021_01 1', 'p29', [l(-17), light, flip], 6)
c291 '[convertstrid(1155382)]'
$ update_portrait('sc021_01 1', 'p29', [l(-17), dark, flip], 6)
$ update_portrait('oc002_01 5', 'p2', [r(-3), r_shake, light], 5)
c23 '[convertstrid(1155383)]'
$ update_portrait('oc002_01 5', 'p2', [r(-3), dark], 5)
$ update_portrait('sc021_01 1', 'p29', [l(-17), light, flip], 6)
c291 '[convertstrid(1155384)]'
hide p2
$ update_portrait('sc021_01 1', 'p29', [l(-17), dark, flip], 6)
$ update_portrait('oc004_01 8', 'p4', [r(-5), light], 5)
c43 '[convertstrid(1155385)]'
$ update_portrait('oc004_01 8', 'p4', [r(-5), dark], 5)
$ update_portrait('sc021_01 4', 'p29', [l(-17), light, flip], 6)
c291 '[convertstrid(1155386)]'
return