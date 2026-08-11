label avg12784(trans=fade_in):

$ play_music("ed6323.ogg")
scene avg_bg_214
$ update_portrait('st064_01 2', 'p1469', [l(-2), light, flip], 6)
$ update_narrator('c14691')
window show
with trans
get_char('c14691') '[convertstrid(1176562)]' (**arg(1, 1176562))
$ update_portrait('st064_01 2', 'p1469', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 23', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1176563)]' (**arg(2, 1176563))
$ update_portrait('oc002_01 23', 'p2', [r(-3), dark], 5)
$ update_portrait('st064_01 5', 'p1469', [l(-2), light, flip], 6)
get_char('c14691') '[convertstrid(1176564)]' (**arg(3, 1176564))
hide p2
$ update_portrait('st064_01 5', 'p1469', [l(-2), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1176565)]' (**arg(4, 1176565))
hide p1469
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 5', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1176566)]' (**arg(5, 1176566))
hide p1304
$ update_portrait('st064_01 3', 'p1469', [l(-2), light, flip], 6)
get_char('c14691') '[convertstrid(1176567)]' (**arg(6, 1176567))
hide p1
$ update_portrait('st064_01 3', 'p1469', [l(-2), dark, flip], 5)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1176568)]' (**arg(7, 1176568))
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('st064_01 3', 'p1469', [l(-2), light, flip], 6)
get_char('c14691') '[convertstrid(1176569)]' (**arg(8, 1176569))
hide p4
$ update_portrait('st064_01 3', 'p1469', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1176570)]' (**arg(9, 1176570))
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1176571)]' (**arg(10, 1176571))
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
$ update_portrait('st064_01 3', 'p1469', [l(-2), light, flip], 6)
get_char('c14691') '[convertstrid(1176572)]' (**arg(11, 1176572))
$ update_portrait('st064_01 3', 'p1469', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 5', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1176573)]' (**arg(12, 1176573))
$ update_portrait('oc003_01 5', 'p3', [r(-6), dark], 5)
$ update_portrait('st064_01 5', 'p1469', [l(-2), light, flip], 6)
get_char('c14691') '[convertstrid(1176574)]' (**arg(13, 1176574))
hide p1469
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1176575)]' (**arg(14, 1176575))
$ update_portrait('oc004_01 8', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1176576)]' (**arg(15, 1176576))
hide p4
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
$ update_portrait('st064_01 1', 'p1469', [l(-2), light, flip], 6)
get_char('c14691') '[convertstrid(1176577)]' (**arg(16, 1176577))
return "avg12784"