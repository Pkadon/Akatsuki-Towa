label avg26033(trans=fade_in):

$ play_music("ed7302.ogg")
scene avg_bg_212
$ update_narrator('c11')
window show
with trans
$ update_portrait('oc001_01 7', 'p1', [l_entrance(-2), light, flip], 6)
get_char('c11') '[convertstrid(1215719)]' (**arg(1, 1215719))
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1215720)]' (**arg(2, 1215720))
$ update_portrait('oc002_01 5', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1215721)]' (**arg(3, 1215721))
$ update_portrait('oc001_01 8', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 6', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1215722)]' (**arg(4, 1215722))
hide p1
hide p2
play sfx2 "other_7002.ogg"
get_char('c0') '[convertstrid(1215753)]' (**arg(5, 1215753))
get_char('c0') '[convertstrid(1215723)]' (**arg(6, 1215723))
get_char('c0') '[convertstrid(1215724)]' (**arg(7, 1215724))
get_char('c0') '[convertstrid(1215725)]' (**arg(8, 1215725))
return "avg26033"