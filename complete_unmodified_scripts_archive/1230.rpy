label avg1230:

$ play_music("ed7150.ogg")
scene avg_bg_013
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(2111394)]' (**arg(1, 2111394))
scene avg_bg_023
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
with fade
get_char('c13') '[convertstrid(2111395)]' (**arg(2, 2111395))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc048_01 1', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(2111396)]' (**arg(3, 2111396))
hide p1
$ update_portrait('sc048_01 1', 'p55', [l(-7), dark, flip], 5)
$ update_portrait('sc050_01 1', 'p57', [r(-19), light], 6)
get_char('c573') '[convertstrid(2111397)]' (**arg(4, 2111397))
hide p55
$ update_portrait('sc050_01 1', 'p57', [r(-19), dark], 5)
$ update_portrait('sc052_01 1', 'p59', [l(-25), light, flip], 6)
get_char('c591') '[convertstrid(2111398)]' (**arg(5, 2111398))
hide p57
$ update_portrait('sc052_01 1', 'p59', [l(-25), dark, flip], 5)
$ update_portrait('sc051_01 4', 'p58', [r(-32), light], 6)
get_char('c583') '[convertstrid(2111399)]' (**arg(6, 2111399))
hide p59
$ update_portrait('sc051_01 4', 'p58', [r(-32), dark], 5)
$ update_portrait('sc053_01 1', 'p60', [l(-32), light, flip], 6)
get_char('c601') '[convertstrid(2111400)]' (**arg(7, 2111400))
hide p58
$ update_portrait('sc053_01 1', 'p60', [l(-32), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2111401)]' (**arg(8, 2111401))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2111402)]' (**arg(9, 2111402))
hide p60
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 22', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(2111403)]' (**arg(10, 2111403))
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(2111404)]' (**arg(11, 2111404))
hide p1
$ update_portrait('oc002_01 5', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('sc048_01 1', 'p55', [r(-7), light], 6)
get_char('c553') '[convertstrid(2111405)]' (**arg(12, 2111405))
hide p2
$ update_portrait('sc048_01 1', 'p55', [r(-7), dark], 5)
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(2111406)]' (**arg(13, 2111406))
hide p55
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('sc052_01 5', 'p59', [r(-25), light], 6)
get_char('c593') '[convertstrid(2111407)]' (**arg(14, 2111407))
hide p3
$ update_portrait('sc052_01 5', 'p59', [r(-25), dark], 5)
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(2111408)]' (**arg(15, 2111408))
hide p59
$ update_portrait('oc004_01 9', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2111409)]' (**arg(16, 2111409))
hide p4
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 2', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2111410)]' (**arg(17, 2111410))
$ update_portrait('sc049_01 2', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2111411)]' (**arg(18, 2111411))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2111412)]' (**arg(19, 2111412))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2111413)]' (**arg(20, 2111413))
stop music
scene avg_bg_070
$ update_narrator('c0')
with fade
get_char('c0') '[convertstrid(2111414)]' (**arg(21, 2111414))
scene avg_bg_023
$ update_narrator('c561')
with fade
$ update_portrait('sc049_01 2', 'p56', [l_entrance(-8), light, flip], 6)
play sfx2 "other_7045.ogg"
get_char('c561') '[convertstrid(2111415)]' (**arg(22, 2111415))
$ update_portrait('sc049_01 2', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), r_shake, light], 6)
play sfx2 "other_7045.ogg"
get_char('c13') '[convertstrid(2111416)]' (**arg(23, 2111416))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
play sfx2 "other_7045.ogg"
get_char('c13') '[convertstrid(2111417)]' (**arg(24, 2111417))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 2', 'p56', [l(-8), light, flip], 6)
play sfx2 "other_7052.ogg"
get_char('c561') '[convertstrid(2111418)]' (**arg(25, 2111418))
$ play_music("ed7455.ogg")
hide p56
play sfx2 "other_7074.ogg"
get_char('c21') '[convertstrid(2111419)]' (**arg(26, 2111419)) with shake
play sfx2 "other_7074.ogg"
get_char('c41') '[convertstrid(2111420)]' (**arg(27, 2111420))
get_char('c41') '[convertstrid(2111421)]' (**arg(28, 2111421))
get_char('c21') '[convertstrid(2111422)]' (**arg(29, 2111422))
play sfx2 "other_7087.ogg"
get_char('c41') '[convertstrid(2111423)]' (**arg(30, 2111423)) with shake
get_char('c31') '[convertstrid(2111424)]' (**arg(31, 2111424))
get_char('c21') '[convertstrid(2111425)]' (**arg(32, 2111425))
get_char('c21') '[convertstrid(2111426)]' (**arg(33, 2111426))
get_char('c21') '[convertstrid(2111427)]' (**arg(34, 2111427))
play sfx2 "other_7087.ogg"
get_char('c41') '[convertstrid(2111428)]' (**arg(35, 2111428))
play sfx2 "other_7022.ogg"
get_char('c41') '[convertstrid(2111429)]' (**arg(36, 2111429))
play sfx2 "other_7004.ogg"
get_char('c31') '[convertstrid(2111430)]' (**arg(37, 2111430))
stop music
hide p1
$ update_portrait('sc049_01 4', 'p56', [l(-8), light, flip], 6)
$ update_narrator('c561')
with fade
get_char('c561') '[convertstrid(2111431)]' (**arg(38, 2111431))
$ update_portrait('sc049_01 4', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
play sfx2 "other_7045.ogg"
get_char('c13') '[convertstrid(2111432)]' (**arg(39, 2111432))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2111433)]' (**arg(40, 2111433))
$ update_portrait('oc001_01 22', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2111434)]' (**arg(41, 2111434))
$ update_portrait('oc001_01 22', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 2', 'p56', [l(-8), light, flip], 6)
play sfx2 "other_7044.ogg"
get_char('c561') '[convertstrid(2111435)]' (**arg(42, 2111435))
$ update_portrait('sc049_01 2', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2111436)]' (**arg(43, 2111436))
scene avg_bg_070
$ update_narrator('c0')
with fade
get_char('c0') '[convertstrid(2111437)]' (**arg(44, 2111437))
$ play_music("ed7455.ogg")
scene avg_bg_023
$ update_narrator('c21')
with fade
play sfx2 "other_7074.ogg"
get_char('c21') '[convertstrid(2111438)]' (**arg(45, 2111438))
get_char('c21') '[convertstrid(2111439)]' (**arg(46, 2111439))
get_char('c41') '[convertstrid(2111440)]' (**arg(47, 2111440))
get_char('c41') '[convertstrid(2111441)]' (**arg(48, 2111441))
get_char('c31') '[convertstrid(2111442)]' (**arg(49, 2111442))
play sfx2 "fight_6010.ogg"
get_char('c41') '[convertstrid(2111443)]' (**arg(50, 2111443))
get_char('c31') '[convertstrid(2111444)]' (**arg(51, 2111444))
play sfx2 "fight_6010.ogg"
get_char('c41') '[convertstrid(2111445)]' (**arg(52, 2111445))
get_char('c21') '[convertstrid(2111446)]' (**arg(53, 2111446)) with shake
get_char('c41') '[convertstrid(2111447)]' (**arg(54, 2111447))
get_char('c21') '[convertstrid(2111448)]' (**arg(55, 2111448))
get_char('c41') '[convertstrid(2111449)]' (**arg(56, 2111449))
get_char('c21') '[convertstrid(2111450)]' (**arg(57, 2111450))
get_char('c21') '[convertstrid(2111451)]' (**arg(58, 2111451))
stop music
$ update_portrait('sc049_01 4', 'p56', [l(-8), light, flip], 6)
$ update_narrator('c561')
with fade
play sfx2 "other_7052.ogg"
get_char('c561') '[convertstrid(2111452)]' (**arg(59, 2111452))
$ update_portrait('sc049_01 4', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), r_shake, light], 6)
play sfx2 "other_7045.ogg"
get_char('c13') '[convertstrid(2111453)]' (**arg(60, 2111453))
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2111454)]' (**arg(61, 2111454))
scene avg_bg_070
$ update_narrator('c0')
with fade
get_char('c0') '[convertstrid(2111455)]' (**arg(62, 2111455))
$ play_music("ed7455.ogg")
scene avg_bg_023
$ update_narrator('c51')
with fade
get_char('c51') '[convertstrid(2111456)]' (**arg(63, 2111456)) with shake
get_char('c31') '[convertstrid(2111457)]' (**arg(64, 2111457))
play sfx2 "other_7023.ogg"
get_char('c61') '[convertstrid(2111458)]' (**arg(65, 2111458))
play sfx2 "other_7004.ogg"
get_char('c41') '[convertstrid(2111459)]' (**arg(66, 2111459))
play sfx2 "other_7074.ogg"
get_char('c41') '[convertstrid(2111460)]' (**arg(67, 2111460))
play sfx2 "other_7074.ogg"
get_char('c21') '[convertstrid(2111461)]' (**arg(68, 2111461))
get_char('c31') '[convertstrid(2111462)]' (**arg(69, 2111462))
get_char('c21') '[convertstrid(2111463)]' (**arg(70, 2111463))
get_char('c21') '[convertstrid(2111464)]' (**arg(71, 2111464))
get_char('c41') '[convertstrid(2111465)]' (**arg(72, 2111465))
get_char('c31') '[convertstrid(2111466)]' (**arg(73, 2111466))
get_char('c61') '[convertstrid(2111467)]' (**arg(74, 2111467))
get_char('c51') '[convertstrid(2111468)]' (**arg(75, 2111468))
stop music
$ update_portrait('sc049_01 2', 'p56', [l(-8), light, flip], 6)
$ update_narrator('c561')
with fade
get_char('c561') '[convertstrid(2111469)]' (**arg(76, 2111469))
$ update_portrait('sc049_01 2', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2111470)]' (**arg(77, 2111470))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2111471)]' (**arg(78, 2111471))
scene avg_bg_070
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
with fade
play sfx2 "other_7083.ogg"
get_char('c13') '[convertstrid(2111472)]' (**arg(79, 2111472))
$ play_music("ed7565.ogg")
scene avg_bg_023
$ update_portrait('sc050_01 1', 'p57', [l(-19), light, flip], 6)
$ update_narrator('c571')
with fade
get_char('c571') '[convertstrid(2111473)]' (**arg(80, 2111473))
$ update_portrait('sc050_01 1', 'p57', [l(-19), dark, flip], 5)
$ update_portrait('sc051_01 4', 'p58', [r(-32), light], 6)
get_char('c583') '[convertstrid(2111474)]' (**arg(81, 2111474))
hide p57
$ update_portrait('sc051_01 4', 'p58', [r(-32), dark], 5)
$ update_portrait('sc048_01 4', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(2111475)]' (**arg(82, 2111475))
hide p58
$ update_portrait('sc048_01 4', 'p55', [l(-7), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2111476)]' (**arg(83, 2111476))
hide p55
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc053_01 2', 'p60', [l(-32), light, flip], 6)
get_char('c601') '[convertstrid(2111477)]' (**arg(84, 2111477))
hide p60
$ update_portrait('sc052_01 1', 'p59', [l(-25), light, flip], 6)
get_char('c591') '[convertstrid(2111478)]' (**arg(85, 2111478))
$ update_portrait('sc052_01 1', 'p59', [l(-25), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2111479)]' (**arg(86, 2111479))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2111480)]' (**arg(87, 2111480))
hide p59
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l_entrance(-8), light, flip], 6)
play sfx2 "other_7047.ogg"
get_char('c561') '[convertstrid(2111481)]' (**arg(88, 2111481))
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2111482)]' (**arg(89, 2111482))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2111483)]' (**arg(90, 2111483))
$ update_portrait('sc049_01 5', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2111484)]' (**arg(91, 2111484))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2111485)]' (**arg(92, 2111485))
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2111486)]' (**arg(93, 2111486))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2111487)]' (**arg(94, 2111487))
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2111488)]' (**arg(95, 2111488))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2111489)]' (**arg(96, 2111489))
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2111490)]' (**arg(97, 2111490))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 2', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2111491)]' (**arg(98, 2111491))
$ update_portrait('sc049_01 2', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(2111492)]' (**arg(99, 2111492))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2111493)]' (**arg(100, 2111493))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2111494)]' (**arg(101, 2111494))
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2111495)]' (**arg(102, 2111495))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2111496)]' (**arg(103, 2111496))
$ update_portrait('sc049_01 5', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2111497)]' (**arg(104, 2111497))
scene avg_bg_013
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
with fade
play sfx2 "other_7060.ogg"
get_char('c13') '[convertstrid(2111498)]' (**arg(105, 2111498))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2111499)]' (**arg(106, 2111499))
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2111500)]' (**arg(107, 2111500))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2111501)]' (**arg(108, 2111501))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
get_char('c561') '[convertstrid(2111502)]' (**arg(109, 2111502, size=(1.25)))
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(2111503)]' (**arg(110, 2111503))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2111504)]' (**arg(111, 2111504))
$ update_portrait('oc001_01 22', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2111505)]' (**arg(112, 2111505))
return