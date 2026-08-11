label avg20105(trans=fade_in):

$ play_music("ED6103.ogg")
scene avg_bg_038
$ update_narrator('c21')
window show
with trans
$ update_portrait('oc002_01 2', 'p2', [l_entrance(-3), light, flip], 6)
play sfx2 "other_7047.ogg"
get_char('c21') '[convertstrid(1005102)]' (**arg(1, 1005102))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
play sfx2 "other_7064.ogg"
get_char('c13') '[convertstrid(1005103)]' (**arg(2, 1005103))
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
get_char('c6961') '[convertstrid(1005104)]' (**arg(3, 1005104))
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1005105)]' (**arg(4, 1005105))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
get_char('c6961') '[convertstrid(1005106)]' (**arg(5, 1005106))
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1005107)]' (**arg(6, 1005107))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
get_char('c6971') '[convertstrid(1005108)]' (**arg(7, 1005108))
get_char('c6961') '[convertstrid(1005109)]' (**arg(8, 1005109))
get_char('c6961') '[convertstrid(1005110)]' (**arg(9, 1005110))
hide p1
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1005111)]' (**arg(10, 1005111))
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
get_char('c6981') '[convertstrid(1005112)]' (**arg(11, 1005112))
hide p2
$ update_portrait('sc039_01 2', 'p46', [r(-13), r_shake, light], 6)
get_char('c463') '[convertstrid(1005113)]' (**arg(12, 1005113))
$ update_portrait('sc039_01 2', 'p46', [r(-13), dark], 5)
get_char('c6961') '[convertstrid(1005114)]' (**arg(13, 1005114))
hide p46
$ update_portrait('oc001_01 12', 'p1', [r_midback(-2), light], 6)
get_char('c13') '[convertstrid(1005115)]' (**arg(14, 1005115))
hide p1
get_char('c6973') '[convertstrid(1005116)]' (**arg(15, 1005116))
get_char('c6961') '[convertstrid(1005117)]' (**arg(16, 1005117))
get_char('c6961') '[convertstrid(1005118)]' (**arg(17, 1005118))
get_char('c6983') '[convertstrid(1005119)]' (**arg(18, 1005119))
$ update_portrait('sc039_01 4', 'p46', [r(-13), light], 6)
get_char('c463') '[convertstrid(1005120)]' (**arg(19, 1005120))
$ update_portrait('sc039_01 4', 'p46', [r(-13), dark], 5)
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005121)]' (**arg(20, 1005121))
hide p46
$ update_portrait('oc001_01 8', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1005122)]' (**arg(21, 1005122))
hide p1
hide p2
get_char('c0') '[convertstrid(1005123)]' (**arg(22, 1005123))
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005124)]' (**arg(23, 1005124))
return "avg20105"