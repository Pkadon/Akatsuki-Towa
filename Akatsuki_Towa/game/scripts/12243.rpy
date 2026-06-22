label avg12243:

$ play_music("ed7101.ogg")
scene avg_bg_020
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(1121265)]' (**arg(1, 1121265))
$ update_portrait('oc002_01 18', 'p2', [l_entrance(-3), light, flip], 6)
get_char('c21') '[convertstrid(1121266)]' (**arg(2, 1121266))
$ update_portrait('oc002_01 18', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 22', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1121267)]' (**arg(3, 1121267))
hide p2
$ update_portrait('oc004_01 22', 'p4', [r(-5), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1121268)]' (**arg(4, 1121268))
hide p1
hide p4
$ update_portrait('st033_01 4', 'p232', [r(-7), light], 6)
$ update_narrator('c2323')
with fade
get_char('c2323') '[convertstrid(1121269)]' (**arg(5, 1121269))
$ update_portrait('st033_01 4', 'p232', [r(-7), dark], 5)
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1121270)]' (**arg(6, 1121270))
$ update_portrait('oc004_01 9', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('st033_01 3', 'p232', [r(-7), r_shake, light], 6)
get_char('c2323') '[convertstrid(1121271)]' (**arg(7, 1121271))
hide p4
hide p232
get_char('c0') '[convertstrid(1121272)]' (**arg(8, 1121272))
$ update_portrait('st033_01 1', 'p232', [r(-7), light], 6)
get_char('c2323') '[convertstrid(1121273)]' (**arg(9, 1121273))
$ update_portrait('st033_01 1', 'p232', [r(-7), light], 6)
get_char('c2323') '[convertstrid(1121274)]' (**arg(10, 1121274))
$ update_portrait('st033_01 2', 'p232', [r(-7), light], 6)
get_char('c2323') '[convertstrid(1121523)]' (**arg(11, 1121523))
$ update_portrait('st033_01 2', 'p232', [r(-7), dark], 5)
$ update_portrait('oc001_01 12', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1121275)]' (**arg(12, 1121275))
$ update_portrait('oc001_01 12', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('st033_01 2', 'p232', [r(-7), light], 6)
get_char('c2323') '[convertstrid(1121590)]' (**arg(13, 1121590))
$ update_portrait('st033_01 2', 'p232', [r(-7), dark], 5)
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1121591)]' (**arg(14, 1121591))
hide p1
$ update_portrait('oc002_01 14', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1121592)]' (**arg(15, 1121592))
$ update_portrait('oc002_01 14', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('st033_01 3', 'p232', [r(-7), light], 6)
get_char('c2323') '[convertstrid(1121593)]' (**arg(16, 1121593))
return