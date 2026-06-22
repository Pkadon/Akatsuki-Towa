label avg10537:

$ play_music("ED6301.ogg")
scene avg_bg_102
$ update_portrait('sc021_01 4', 'p29', [l(-17), light, flip], 6)
$ update_narrator('c291')
window show
with fade_in
get_char('c291') '[convertstrid(1152574)]' (**arg(1, 1152574))
$ update_portrait('sc021_01 4', 'p29', [l(-17), dark, flip], 5)
$ update_portrait('oc002_01 4', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1152575)]' (**arg(2, 1152575))
hide p29
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1152576)]' (**arg(3, 1152576))
hide p2
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1152577)]' (**arg(4, 1152577))
return