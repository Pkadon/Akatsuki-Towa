label avg10316(trans=fade_in):

$ play_music("ed7102.ogg")
scene avg_bg_007
$ update_portrait('oc006_01 1', 'p6', [l(-5), light, flip], 6)
$ update_narrator('c61')
window show
with trans
play sfx2 "other_7024.ogg"
get_char('c61') '[convertstrid(1130400)]' (**arg(1, 1130400))
$ update_portrait('oc006_01 4', 'p6', [l(-5), light, flip], 6)
play sfx2 "other_7023.ogg"
get_char('c61') '[convertstrid(1130401)]' (**arg(2, 1130401))
$ update_portrait('oc006_01 1', 'p6', [l(-5), light, flip], 6)
play sfx2 "other_7022.ogg"
get_char('c61') '[convertstrid(1130402)]' (**arg(3, 1130402))
hide p6
$ update_narrator('c43')
with fade
play sfx2 "other_7047.ogg"
get_char('c43') '[convertstrid(1130403)]' (**arg(4, 1130403))
$ update_narrator('c61')
$ update_portrait('oc006_01 2', 'p6', [l(-5), light, flip], 6)
with fade
$ update_portrait('oc006_01 2', 'p6', [l(-5), l_shake, light, flip], 6)
get_char('c61') '[convertstrid(1130404)]' (**arg(5, 1130404))
$ update_portrait('oc006_01 2', 'p6', [l(-5), dark, flip], 5)
$ update_portrait('oc004_01 2', 'p4', [r_entrance(-5), light], 6)
get_char('c43') '[convertstrid(1130405)]' (**arg(6, 1130405))
$ update_portrait('oc004_01 2', 'p4', [r(-5), dark], 5)
$ update_portrait('oc006_01 1', 'p6', [l(-5), light, flip], 6)
get_char('c61') '[convertstrid(1130406)]' (**arg(7, 1130406))
hide p4
$ update_portrait('oc006_01 1', 'p6', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130407)]' (**arg(8, 1130407))
hide p6
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 10', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1130408)]' (**arg(9, 1130408))
$ update_portrait('oc004_01 10', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130409)]' (**arg(10, 1130409))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1130410)]' (**arg(11, 1130410))
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1130411)]' (**arg(12, 1130411))
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1130412)]' (**arg(13, 1130412))
hide p1
$ update_portrait('oc004_01 9', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1130413)]' (**arg(14, 1130413))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 12', 'p4', [l(-5), l_shake, light, flip], 6)
get_char('c41') '[convertstrid(1130414)]' (**arg(15, 1130414))
hide p4
hide p2
$ update_portrait('oc006_01 5', 'p6', [r(-5), light], 6)
$ update_narrator('c63')
with fade
play sfxvoice "avg_vocal_sa05.ogg"
get_char('c63') '[convertstrid(1130415)]' (**arg(16, 1130415))
$ update_portrait('oc006_01 5', 'p6', [r(-5), dark], 5)
$ update_portrait('oc004_01 13', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li10.ogg"
get_char('c41') '[convertstrid(1130416)]' (**arg(17, 1130416))
$ update_portrait('oc004_01 12', 'p4', [l(-5), l_shake, light, flip], 6)
get_char('c41') '[convertstrid(1130417)]' (**arg(18, 1130417))
hide p6
$ update_portrait('oc004_01 12', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1130418)]' (**arg(19, 1130418))
hide p2
$ update_portrait('oc006_01 5', 'p6', [r(-5), light], 6)
get_char('c63') '[convertstrid(1130419)]' (**arg(20, 1130419))
$ update_portrait('oc006_01 5', 'p6', [r(-5), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1130420)]' (**arg(21, 1130420))
hide p6
$ update_portrait('oc004_01 8', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130421)]' (**arg(22, 1130421))
hide p4
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1130422)]' (**arg(23, 1130422))
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1130423)]' (**arg(24, 1130423))
hide p2
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro13.ogg"
get_char('c31') '[convertstrid(1130424)]' (**arg(25, 1130424))
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130425)]' (**arg(26, 1130425))
hide p3
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l_midback(-5), light, flip], 6)
play sfxvoice "avg_vocal_li21.ogg"
get_char('c41') '[convertstrid(1130426)]' (**arg(27, 1130426))
hide p1
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 1', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1130427)]' (**arg(28, 1130427))
hide p2
$ update_portrait('oc006_01 5', 'p6', [r(-5), light], 6)
play sfxvoice "avg_vocal_sa08.ogg"
get_char('c63') '[convertstrid(1130428)]' (**arg(29, 1130428))
$ update_portrait('oc006_01 5', 'p6', [r(-5), dark], 5)
$ update_portrait('oc004_01 10', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1130429)]' (**arg(30, 1130429))
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1130430)]' (**arg(31, 1130430))
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1130431)]' (**arg(32, 1130431))
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1130432)]' (**arg(33, 1130432))
hide p6
$ update_portrait('oc004_01 8', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 22', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1130433)]' (**arg(34, 1130433))
$ update_portrait('oc002_01 22', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 6', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1130434)]' (**arg(35, 1130434))
$ update_portrait('oc004_01 15', 'p4', [l(-5), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_li11.ogg"
get_char('c41') '[convertstrid(1130435)]' (**arg(36, 1130435))
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1130436)]' (**arg(37, 1130436))
hide p2
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc006_01 2', 'p6', [r(-5), light], 6)
get_char('c63') '[convertstrid(1130437)]' (**arg(38, 1130437))
scene avg_bg_070
$ update_narrator('c0')
with fade
get_char('c0') '[convertstrid(1130438)]' (**arg(39, 1130438))
scene avg_bg_007
$ update_portrait('oc006_01 2', 'p6', [r(-5), light], 6)
$ update_narrator('c63')
with fade
get_char('c63') '[convertstrid(1130439)]' (**arg(40, 1130439))
$ update_portrait('oc006_01 2', 'p6', [r(-5), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l_midback(-5), light, flip], 6)
get_char('c41') '[convertstrid(1130440)]' (**arg(41, 1130440))
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc006_01 5', 'p6', [r(-5), light], 6)
get_char('c63') '[convertstrid(1130441)]' (**arg(42, 1130441))
$ update_portrait('oc006_01 4', 'p6', [r(-5), light], 6)
get_char('c63') '[convertstrid(1130442)]' (**arg(43, 1130442))
hide p4
$ update_portrait('oc006_01 4', 'p6', [r(-5), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1130443)]' (**arg(44, 1130443))
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc006_01 1', 'p6', [r(-5), light], 6)
get_char('c63') '[convertstrid(1130444)]' (**arg(45, 1130444))
hide p1
$ update_portrait('oc006_01 1', 'p6', [r(-5), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1130445)]' (**arg(46, 1130445))
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc006_01 5', 'p6', [r(-5), light], 6)
get_char('c63') '[convertstrid(1130446)]' (**arg(47, 1130446))
$ update_portrait('oc006_01 5', 'p6', [r(-5), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l(-5), l_shake, light, flip], 6)
get_char('c41') '[convertstrid(1130447)]' (**arg(48, 1130447))
hide p4
hide p6
$ update_narrator('c23')
with fade
$ update_portrait('oc002_01 22', 'p2', [r_entrance(-3), light], 6)
get_char('c23') '[convertstrid(1130448)]' (**arg(49, 1130448))
$ update_portrait('oc002_01 22', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1130449)]' (**arg(50, 1130449))
hide p2
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130450)]' (**arg(51, 1130450))
return "avg10316"