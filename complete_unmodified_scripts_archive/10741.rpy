label avg10741(trans=fade_in):

$ play_music("ed7510.ogg")
scene avg_bg_003
$ update_narrator('c0')
window show
with trans
get_char('c0') '[convertstrid(1172711)]' (**arg(1, 1172711))
$ update_portrait('oc005_01 4', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1172712)]' (**arg(2, 1172712))
$ update_portrait('oc005_01 4', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1172713)]' (**arg(3, 1172713))
$ update_portrait('oc005_01 4', 'p5', [l(-6), dark, flip], 5)
$ update_portrait('oc003_01 16', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1172714)]' (**arg(4, 1172714))
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1172715)]' (**arg(5, 1172715))
hide p5
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 17', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1172716)]' (**arg(6, 1172716))
$ update_portrait('oc004_01 18', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1172717)]' (**arg(7, 1172717))
hide p4
$ update_portrait('st044_01 4', 'p692', [l(10), light, flip], 6)
get_char('c6921') '[convertstrid(1172718)]' (**arg(8, 1172718))
hide p3
$ update_portrait('st044_01 4', 'p692', [l(10), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1172719)]' (**arg(9, 1172719))
hide p692
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1172720)]' (**arg(10, 1172720))
$ update_portrait('oc004_01 11', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1172721)]' (**arg(11, 1172721))
$ update_portrait('oc004_01 20', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1172722)]' (**arg(12, 1172722))
$ update_portrait('oc004_01 20', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1172723)]' (**arg(13, 1172723))
$ update_portrait('oc001_01 16', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1172724)]' (**arg(14, 1172724))
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1172726)]' (**arg(15, 1172726))
hide p4
$ update_portrait('oc001_01 16', 'p1', [r(-2), dark], 5)
$ update_portrait('oc005_01 4', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1172732)]' (**arg(16, 1172732))
stop music
hide p1
$ update_portrait('oc005_01 4', 'p5', [l(-6), dark, flip], 5)
$ update_portrait('st061_01 2', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1172733)]' (**arg(17, 1172733))
hide p5
$ update_portrait('st061_01 2', 'p1304', [r(-2), dark], 5)
$ update_portrait('st044_01 2', 'p692', [l(10), light, flip], 6)
get_char('c6921') '[convertstrid(1172734)]' (**arg(18, 1172734))
hide p692
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1172735)]' (**arg(19, 1172735))
hide p1304
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1172736)]' (**arg(20, 1172736))
hide p3
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 23', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1172737)]' (**arg(21, 1172737))
hide p1
$ update_portrait('oc004_01 23', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc005_01 7', 'p5', [r(-6), light], 6)
get_char('c53') '[convertstrid(1172738)]' (**arg(22, 1172738))
scene avg_bg_070
$ update_narrator('c0')
with fade
play sfx2 "other_7017.ogg"
get_char('c0') '[convertstrid(1172739)]' (**arg(23, 1172739))
$ play_music("ed7551.ogg")
scene avg_bg_505
$ update_narrator('c33')
with fade
get_char('c33') '[convertstrid(1172740)]' (**arg(24, 1172740))
play sfx2 "other_7080.ogg"
get_char('c14451') '[convertstrid(1172741)]' (**arg(25, 1172741)) with shake
scene avg_bg_070
$ update_narrator('c0')
with fade
get_char('c0') '[convertstrid(1172742)]' (**arg(26, 1172742))
get_char('c0') '[convertstrid(1172743)]' (**arg(27, 1172743))
return "avg10741"