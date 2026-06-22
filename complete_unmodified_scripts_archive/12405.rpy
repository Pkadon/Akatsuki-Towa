label avg12405:

$ play_music("ed7518.ogg")
scene avg_bg_059
$ update_narrator('c13')
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
window show
with fade_in
$ update_portrait('oc001_01 7', 'p1', [r(-2), r_shake, light], 6)
play sfx2 "fight_6010.ogg"
play sfxvoice "avg_vocal_na02.ogg"
get_char('c13') '[convertstrid(1142452)]' (**arg(1, 1142452))
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 5', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li30.ogg"
get_char('c41') '[convertstrid(1142453)]' (**arg(2, 1142453))
hide p4
$ update_portrait('oc003_01 12', 'p3', [l_entrance(-6), light, flip], 6)
play sfx2 "common_wrong.ogg"
play sfxvoice "avg_vocal_ro09.ogg"
get_char('c31') '[convertstrid(1142454)]' (**arg(3, 1142454))
$ update_portrait('oc003_01 14', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1142455)]' (**arg(4, 1142455))
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1142456)]' (**arg(5, 1142456))
hide p1
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 5)
get_char('c11473') '[convertstrid(1142457)]' (**arg(6, 1142457))
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1142458)]' (**arg(7, 1142458))
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 6', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro06.ogg"
get_char('c31') '[convertstrid(1142459)]' (**arg(8, 1142459))
hide p1
$ update_portrait('oc003_01 6', 'p3', [l(-6), dark, flip], 5)
get_char('c11483') '[convertstrid(1142460)]' (**arg(9, 1142460, size=(1.2)))
get_char('c11373') '[convertstrid(1142461)]' (**arg(10, 1142461))
hide p3
$ update_portrait('oc004_01 23', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li09.ogg"
get_char('c41') '[convertstrid(1142462)]' (**arg(11, 1142462))
$ play_music("ed7514.ogg")
hide p4
$ update_narrator('c0')
with fade
get_char('c0') '[convertstrid(1142463)]' (**arg(12, 1142463))
get_char('c11471') '[convertstrid(1142464)]' (**arg(13, 1142464))
get_char('c11483') '[convertstrid(1142465)]' (**arg(14, 1142465))
get_char('c6081') '[convertstrid(1142466)]' (**arg(15, 1142466))
$ update_portrait('oc002_01 14', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1142467)]' (**arg(16, 1142467))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1142468)]' (**arg(17, 1142468))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 10', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1142469)]' (**arg(18, 1142469))
hide p1
$ update_portrait('oc004_01 10', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1142470)]' (**arg(19, 1142470))
hide p4
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1142471)]' (**arg(20, 1142471))
hide p2
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 7', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1142472)]' (**arg(21, 1142472))
hide p4
$ update_portrait('oc001_01 5', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na19.ogg"
get_char('c13') '[convertstrid(1142473)]' (**arg(22, 1142473))
hide p3
$ update_portrait('oc001_01 5', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1142474)]' (**arg(23, 1142474))
hide p2
$ update_portrait('oc004_01 13', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1142475)]' (**arg(24, 1142475))
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1142476)]' (**arg(25, 1142476))
$ update_portrait('oc004_01 7', 'p4', [l(-5), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_li19.ogg"
get_char('c41') '[convertstrid(1142477)]' (**arg(26, 1142477))
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1142478)]' (**arg(27, 1142478))
hide p4
hide p1
$ update_narrator('c11371')
with fade
get_char('c11371') '[convertstrid(1142479)]' (**arg(28, 1142479))
$ update_portrait('oc003_01 5', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1142480)]' (**arg(29, 1142480))
$ update_portrait('oc003_01 5', 'p3', [r(-6), dark], 5)
get_char('c11371') '[convertstrid(1142481)]' (**arg(30, 1142481))
$ update_portrait('oc003_01 12', 'p3', [r(-6), r_shake, light], 6)
get_char('c33') '[convertstrid(1142482)]' (**arg(31, 1142482))
scene avg_bg_070
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
with fade
get_char('c13') '[convertstrid(1142483)]' (**arg(32, 1142483))
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1142484)]' (**arg(33, 1142484))
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1142485)]' (**arg(34, 1142485))
return