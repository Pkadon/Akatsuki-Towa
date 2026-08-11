label avg12334(trans=fade_in):

$ play_music("ed7565.ogg")
scene avg_bg_059
$ update_portrait('oc001_01 18', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with trans
play sfx2 "common_select.ogg"
get_char('c11') '[convertstrid(1133440)]' (**arg(1, 1133440))
$ update_portrait('oc001_01 18', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc004_01 13', 'p4', [r(-5), r_shake, light], 6)
play sfxvoice "avg_vocal_li13.ogg"
get_char('c43') '[convertstrid(1133441)]' (**arg(2, 1133441))
hide p1
$ update_portrait('oc004_01 13', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 13', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1133442)]' (**arg(3, 1133442))
hide p4
$ update_portrait('oc002_01 13', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 7', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1133443)]' (**arg(4, 1133443))
hide p2
$ update_portrait('oc003_01 7', 'p3', [r(-6), dark], 5)
$ update_portrait('oc001_01 17', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1133444)]' (**arg(5, 1133444))
hide p3
$ update_portrait('oc001_01 17', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc004_01 13', 'p4', [r(-5), r_shake, light], 6)
get_char('c43') '[convertstrid(1133445)]' (**arg(6, 1133445))
$ update_portrait('oc004_01 11', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li16.ogg"
get_char('c43') '[convertstrid(1133446)]' (**arg(7, 1133446))
$ update_portrait('oc004_01 16', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li24.ogg"
get_char('c43') '[convertstrid(1133447)]' (**arg(8, 1133447))
hide p1
$ update_portrait('oc004_01 16', 'p4', [r(-5), dark], 5)
$ update_portrait('st004_01 2', 'p204', [l(4), light, flip], 6)
get_char('c2041') '[convertstrid(1133448)]' (**arg(9, 1133448))
hide p204
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1133449)]' (**arg(10, 1133449))
hide p2
$ update_portrait('st004_01 5', 'p204', [l(4), light, flip], 6)
get_char('c2041') '[convertstrid(1133450)]' (**arg(11, 1133450))
$ update_portrait('st004_01 2', 'p204', [l(4), light, flip], 6)
get_char('c2041') '[convertstrid(1133451)]' (**arg(12, 1133451))
hide p4
$ update_portrait('st004_01 2', 'p204', [l(4), dark, flip], 5)
$ update_portrait('oc002_01 14', 'p2', [r(-3), r_shake, light], 6)
play sfxvoice "avg_vocal_ch06.ogg"
get_char('c23') '[convertstrid(1133452)]' (**arg(13, 1133452))
hide p204
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 5', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1133453)]' (**arg(14, 1133453))
hide p2
$ update_portrait('oc001_01 5', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 5', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro08.ogg"
get_char('c33') '[convertstrid(1133454)]' (**arg(15, 1133454))
hide p3
$ update_portrait('oc004_01 23', 'p4', [r(-5), r_shake, light], 6)
play sfxvoice "avg_vocal_li09.ogg"
get_char('c43') '[convertstrid(1133455)]' (**arg(16, 1133455))
$ update_portrait('oc004_01 16', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1133456)]' (**arg(17, 1133456))
$ update_portrait('oc004_01 16', 'p4', [r(-5), dark], 5)
$ update_portrait('oc001_01 12', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1133457)]' (**arg(18, 1133457))
hide p1
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1133458)]' (**arg(19, 1133458))
hide p3
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1133459)]' (**arg(20, 1133459))
return "avg12334"