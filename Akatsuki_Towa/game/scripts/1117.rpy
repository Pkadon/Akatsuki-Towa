label avg1117(trans=fade_in):

$ play_music("ed7200.ogg")
scene avg_bg_026
$ update_portrait('oc004_01 13', 'p4', [l(-5), light, flip], 6)
$ update_narrator('c41')
window show
with trans
get_char('c41') '[convertstrid(2102897)]' (**arg(1, 2102897))
$ update_portrait('oc004_01 13', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2102898)]' (**arg(2, 2102898))
hide p4
hide p1
play sfx2 "other_7004.ogg"
get_char('c0') '[convertstrid(2102899)]' (**arg(3, 2102899))
play sfx2 "other_7004.ogg"
get_char('c0') '[convertstrid(2102900)]' (**arg(4, 2102900))
$ update_portrait('oc001_01 22', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2102901)]' (**arg(5, 2102901))
$ update_portrait('oc001_01 22', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(2102902)]' (**arg(6, 2102902))
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 5', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2102903)]' (**arg(7, 2102903))
hide p4
$ update_portrait('oc001_01 5', 'p1', [r(-2), dark], 5)
$ update_portrait('st004_01 6', 'p204', [l(4), light, flip], 6)
get_char('c2041') '[convertstrid(2102904)]' (**arg(8, 2102904))
hide p204
hide p1
$ update_portrait('sca15_01 5', 'p23', [r(9), light], 6)
$ update_narrator('c233')
with fade
get_char('c233') '[convertstrid(2102905)]' (**arg(9, 2102905))
$ update_portrait('sca15_01 1', 'p23', [r(9), light], 6)
get_char('c233') '[convertstrid(2102906)]' (**arg(10, 2102906))
return "avg1117"