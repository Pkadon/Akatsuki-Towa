label avg10659(trans=fade_in):

$ play_music("ED6105.ogg")
scene avg_bg_070
$ update_narrator('c0')
window show
with trans
get_char('c0') '[convertstrid(1165430)]' (**arg(1, 1165430))
get_char('c0') '[convertstrid(1165431)]' (**arg(2, 1165431))
scene avg_bg_023
$ update_portrait('oc002_01 15', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
with fade
get_char('c23') '[convertstrid(1165432)]' (**arg(3, 1165432))
$ update_portrait('oc002_01 15', 'p2', [r(-3), dark], 5)
get_char('c13501') '[convertstrid(1165433)]' (**arg(4, 1165433))
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1165434)]' (**arg(5, 1165434))
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
get_char('c161') '[convertstrid(1165435)]' (**arg(6, 1165435))
hide p2
$ update_portrait('sc008_01 4', 'p16', [l(-18), dark, flip], 5)
$ update_portrait('st061_01 5', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1165436)]' (**arg(7, 1165436))
hide p16
$ update_portrait('st061_01 5', 'p1304', [r(-2), dark], 5)
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1165437)]' (**arg(8, 1165437))
hide p1304
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1165438)]' (**arg(9, 1165438))
$ update_portrait('oc004_01 8', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1165439)]' (**arg(10, 1165439))
hide p3
$ update_portrait('oc004_01 8', 'p4', [r(-5), dark], 5)
get_char('c13351') '[convertstrid(1165440)]' (**arg(11, 1165440))
hide p4
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1165441)]' (**arg(12, 1165441))
hide p1
$ update_portrait('oc004_01 7', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1165442)]' (**arg(13, 1165442))
$ update_portrait('oc004_01 7', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1165443)]' (**arg(14, 1165443))
hide p4
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1165444)]' (**arg(15, 1165444))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1165445)]' (**arg(16, 1165445))
hide p1
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1165446)]' (**arg(17, 1165446))
hide p2
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('sc008_01 2', 'p16', [l(-18), light, flip], 6)
get_char('c161') '[convertstrid(1165447)]' (**arg(18, 1165447))
$ play_music("ed7516.ogg")
hide p16
hide p3
get_char('c0') '[convertstrid(1165448)]' (**arg(19, 1165448))
get_char('c0') '[convertstrid(1165449)]' (**arg(20, 1165449))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1165450)]' (**arg(21, 1165450))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
get_char('c161') '[convertstrid(1165451)]' (**arg(22, 1165451))
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
get_char('c161') '[convertstrid(1165452)]' (**arg(23, 1165452))
hide p1
$ update_portrait('sc008_01 4', 'p16', [l(-18), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 6)
play sfx2 "common_correct.ogg"
get_char('c23') '[convertstrid(1165453)]' (**arg(24, 1165453))
hide p16
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1165454)]' (**arg(25, 1165454))
hide p2
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1165455)]' (**arg(26, 1165455))
hide p4
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1165456)]' (**arg(27, 1165456))
hide p3
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
get_char('c161') '[convertstrid(1165457)]' (**arg(28, 1165457))
hide p1
$ update_portrait('sc008_01 4', 'p16', [l(-18), dark, flip], 5)
$ update_portrait('oc002_01 14', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1165458)]' (**arg(29, 1165458))
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
get_char('c161') '[convertstrid(1165459)]' (**arg(30, 1165459))
hide p2
$ update_portrait('sc008_01 4', 'p16', [l(-18), dark, flip], 5)
get_char('c13353') '[convertstrid(1165460)]' (**arg(31, 1165460))
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
get_char('c161') '[convertstrid(1165461)]' (**arg(32, 1165461))
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
get_char('c161') '[convertstrid(1165462)]' (**arg(33, 1165462))
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
get_char('c161') '[convertstrid(1165463)]' (**arg(34, 1165463))
$ update_portrait('sc008_01 4', 'p16', [l(-18), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1165464)]' (**arg(35, 1165464))
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1165465)]' (**arg(36, 1165465))
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1165466)]' (**arg(37, 1165466))
hide p1
$ update_portrait('oc002_01 17', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1165467)]' (**arg(38, 1165467))
$ update_portrait('oc002_01 17', 'p2', [r(-3), dark], 5)
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
get_char('c161') '[convertstrid(1165468)]' (**arg(39, 1165468))
hide p2
$ update_portrait('sc008_01 4', 'p16', [l(-18), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1165469)]' (**arg(40, 1165469))
$ update_portrait('oc003_01 10', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1165470)]' (**arg(41, 1165470))
hide p16
$ update_portrait('oc003_01 10', 'p3', [r(-6), dark], 5)
$ update_portrait('st061_01 4', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1165471)]' (**arg(42, 1165471))
$ update_portrait('st061_01 4', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1165472)]' (**arg(43, 1165472))
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1165473)]' (**arg(44, 1165473))
$ update_portrait('st061_01 1', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1165474)]' (**arg(45, 1165474))
hide p1304
$ update_portrait('oc003_01 8', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 16', 'p4', [l(-5), l_shake, light, flip], 6)
get_char('c41') '[convertstrid(1165475)]' (**arg(46, 1165475))
$ update_portrait('oc004_01 16', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1165476)]' (**arg(47, 1165476))
hide p4
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
$ update_portrait('st061_01 5', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1165477)]' (**arg(48, 1165477))
hide p3
$ update_portrait('st061_01 5', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1165478)]' (**arg(49, 1165478))
hide p1304
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c13351') '[convertstrid(1165479)]' (**arg(50, 1165479))
return "avg10659"