label avg12675(trans=fade_in):

$ play_music("ED6105.ogg")
scene avg_bg_203
$ update_narrator('c21')
window show
with trans
$ update_portrait('oc002_01 4', 'p2', [l_entrance(-3), light, flip], 6)
get_char('c21') '[convertstrid(1166896)]' (**arg(1, 1166896))
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1166897)]' (**arg(2, 1166897))
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1166898)]' (**arg(3, 1166898))
hide p3
$ update_portrait('oc002_01 10', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1166899)]' (**arg(4, 1166899))
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1166900)]' (**arg(5, 1166900))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 15', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1166901)]' (**arg(6, 1166901))
hide p1
$ update_portrait('oc002_01 15', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 7', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1166902)]' (**arg(7, 1166902))
$ update_portrait('oc004_01 7', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 13', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1166903)]' (**arg(8, 1166903))
hide p4
$ update_portrait('oc002_01 13', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1166904)]' (**arg(9, 1166904))
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 22', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1166905)]' (**arg(10, 1166905))
$ update_portrait('oc002_01 22', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 23', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1166906)]' (**arg(11, 1166906))
hide p1
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1166907)]' (**arg(12, 1166907))
$ play_music("ed6564.ogg")
scene avg_bg_004
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
with fade
get_char('c13') '[convertstrid(1166908)]' (**arg(13, 1166908))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1166909)]' (**arg(14, 1166909))
hide p4
$ update_portrait('oc002_01 17', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1166910)]' (**arg(15, 1166910))
$ update_portrait('oc002_01 17', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1166911)]' (**arg(16, 1166911))
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 16', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1166912)]' (**arg(17, 1166912))
return "avg12675"