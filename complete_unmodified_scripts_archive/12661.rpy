label avg12661:

$ play_music("ED6105.ogg")
scene avg_bg_072
$ update_narrator('c13')
window show
with fade_in
$ update_portrait('oc001_01 1', 'p1', [r_entrance(-2), light], 6)
play sfx2 "other_7047.ogg"
get_char('c13') '[convertstrid(1166439)]' (**arg(1, 1166439))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
get_char('c13371') '[convertstrid(1166440)]' (**arg(2, 1166440))
hide p1
$ update_portrait('st061_01 2', 'p1304', [r(-2), l_shake, light], 6)
get_char('c13043') '[convertstrid(1166441)]' (**arg(3, 1166441))
$ update_portrait('st061_01 2', 'p1304', [r(-2), dark], 5)
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1166442)]' (**arg(4, 1166442))
hide p1304
$ update_portrait('oc003_01 2', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 14', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1166443)]' (**arg(5, 1166443))
hide p3
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
get_char('c13371') '[convertstrid(1166444)]' (**arg(6, 1166444))
hide p2
$ update_portrait('st061_01 1', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1166445)]' (**arg(7, 1166445))
hide p1304
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1166446)]' (**arg(8, 1166446))
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
get_char('c13371') '[convertstrid(1166447)]' (**arg(9, 1166447))
get_char('c13371') '[convertstrid(1166448)]' (**arg(10, 1166448))
get_char('c13371') '[convertstrid(1166449)]' (**arg(11, 1166449))
get_char('c13371') '[convertstrid(1166450)]' (**arg(12, 1166450))
hide p4
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1166451)]' (**arg(13, 1166451))
hide p3
$ update_portrait('oc002_01 23', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1166452)]' (**arg(14, 1166452))
$ update_portrait('oc002_01 23', 'p2', [r(-3), dark], 5)
get_char('c13371') '[convertstrid(1166453)]' (**arg(15, 1166453))
get_char('c13371') '[convertstrid(1166454)]' (**arg(16, 1166454))
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1166455)]' (**arg(17, 1166455))
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1166456)]' (**arg(18, 1166456))
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1166457)]' (**arg(19, 1166457))
hide p4
get_char('c13371') '[convertstrid(1166458)]' (**arg(20, 1166458))
hide p2
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1166459)]' (**arg(21, 1166459))
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1166460)]' (**arg(22, 1166460))
$ update_portrait('st061_01 1', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 12', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1166461)]' (**arg(23, 1166461))
$ update_portrait('oc003_01 12', 'p3', [r(-6), dark], 5)
$ update_portrait('st061_01 5', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1166462)]' (**arg(24, 1166462))
$ update_portrait('st061_01 4', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1166463)]' (**arg(25, 1166463))
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1166464)]' (**arg(26, 1166464))
hide p3
$ update_portrait('st061_01 1', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1166465)]' (**arg(27, 1166465))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1166466)]' (**arg(28, 1166466))
$ update_portrait('st061_01 5', 'p1304', [l_exit(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1166467)]' (**arg(29, 1166467))
hide p1304
hide p2
$ update_portrait('oc003_01 12', 'p3', [r_midback(-6), light], 6)
get_char('c33') '[convertstrid(1166468)]' (**arg(30, 1166468))
$ update_portrait('oc003_01 12', 'p3', [r(-6), dark], 5)
$ update_portrait('st061_01 1', 'p1304', [l_entrance(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1166469)]' (**arg(31, 1166469))
hide p1304
get_char('c13371') '[convertstrid(1166470)]' (**arg(32, 1166470))
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1166471)]' (**arg(33, 1166471))
$ update_portrait('oc003_01 8', 'p3', [r(-6), dark], 5)
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1166472)]' (**arg(34, 1166472))
scene avg_bg_070
$ update_narrator('c0')
with fade
get_char('c0') '[convertstrid(1166473)]' (**arg(35, 1166473))
get_char('c0') '[convertstrid(1166474)]' (**arg(36, 1166474))
return