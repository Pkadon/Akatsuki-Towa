label avg1025:

$ play_music("ed7113.ogg")
scene avg_bg_024
$ update_narrator('c23')
window show
with fade_in
$ update_portrait('oc002_01 6', 'p2', [r_entrance(-3), light], 6)
get_char('c23') '[convertstrid(2100475)]' (**arg(1, 2100475))
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
$ update_portrait('sc039_01 1', 'p46', [l(-13), light, flip], 6)
get_char('c461') '[convertstrid(2100476)]' (**arg(2, 2100476))
hide p2
$ update_portrait('sc039_01 1', 'p46', [l(-13), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2100477)]' (**arg(3, 2100477))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc039_01 1', 'p46', [l(-13), light, flip], 6)
get_char('c461') '[convertstrid(2100478)]' (**arg(4, 2100478))
$ update_portrait('sc039_01 5', 'p46', [l(-13), light, flip], 6)
get_char('c461') '[convertstrid(2100479)]' (**arg(5, 2100479))
$ update_portrait('sc039_01 5', 'p46', [l(-13), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2100480)]' (**arg(6, 2100480))
hide p46
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(2100481)]' (**arg(7, 2100481))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2100482)]' (**arg(8, 2100482))
hide p2
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('st053_01 1', 'p1007', [l_entrance(-12), light, flip], 6)
get_char('c10071') '[convertstrid(2100483)]' (**arg(9, 2100483))
hide p1007
$ update_portrait('st051_01 5', 'p258', [l_entrance(-9), light, flip], 6)
get_char('c2581') '[convertstrid(2100484)]' (**arg(10, 2100484))
hide p258
$ update_portrait('sc038_01 1', 'p45', [l(-1), light, flip], 6)
get_char('c451') '[convertstrid(2100485)]' (**arg(11, 2100485))
$ update_portrait('sc038_01 1', 'p45', [l(-1), light, flip], 6)
get_char('c451') '[convertstrid(2100486)]' (**arg(12, 2100486))
hide p1
$ update_portrait('sc038_01 1', 'p45', [l(-1), dark, flip], 5)
get_char('c2593') '[convertstrid(2100487)]' (**arg(13, 2100487))
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(2100488)]' (**arg(14, 2100488))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('sc038_01 5', 'p45', [l(-1), light, flip], 6)
get_char('c451') '[convertstrid(2100489)]' (**arg(15, 2100489))
hide p45
$ update_portrait('sc039_01 1', 'p46', [l(-13), light, flip], 6)
get_char('c461') '[convertstrid(2100490)]' (**arg(16, 2100490))
$ update_portrait('sc039_01 1', 'p46', [l(-13), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(2100491)]' (**arg(17, 2100491))
hide p46
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('sc038_01 1', 'p45', [l(-1), light, flip], 6)
get_char('c451') '[convertstrid(2100492)]' (**arg(18, 2100492))
hide p2
$ update_portrait('sc038_01 1', 'p45', [l(-1), dark, flip], 5)
$ update_portrait('sc039_01 1', 'p46', [r(-13), light], 6)
get_char('c463') '[convertstrid(2100493)]' (**arg(19, 2100493))
hide p45
hide p46
$ update_portrait('sc039_01 1', 'p46', [l(-13), light, flip], 6)
$ update_narrator('c461')
with fade
get_char('c461') '[convertstrid(2100495)]' (**arg(20, 2100495))
$ update_portrait('sc039_01 1', 'p46', [l(-13), light, flip], 6)
get_char('c461') '[convertstrid(2100496)]' (**arg(21, 2100496))
$ update_portrait('sc039_01 1', 'p46', [l(-13), dark, flip], 5)
$ update_portrait('oc002_01 14', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch06.ogg"
get_char('c23') '[convertstrid(2100497)]' (**arg(22, 2100497))
hide p46
hide p2
$ update_portrait('sc038_01 4', 'p45', [l(-1), light, flip], 6)
$ update_narrator('c451')
with fade
get_char('c451') '[convertstrid(2100498)]' (**arg(23, 2100498))
$ update_portrait('sc038_01 1', 'p45', [l(-1), light, flip], 6)
get_char('c451') '[convertstrid(2100499)]' (**arg(24, 2100499))
$ update_portrait('sc038_01 1', 'p45', [l(-1), dark, flip], 5)
$ update_portrait('sc039_01 1', 'p46', [r(-13), light], 6)
get_char('c463') '[convertstrid(2100500)]' (**arg(25, 2100500))
$ update_portrait('sc039_01 1', 'p46', [r(-13), dark], 5)
$ update_portrait('sc038_01 1', 'p45', [l(-1), light, flip], 6)
get_char('c451') '[convertstrid(2100501)]' (**arg(26, 2100501))
hide p45
hide p46
$ update_narrator('c9771')
with fade
get_char('c9771') '[convertstrid(2100502)]' (**arg(27, 2100502))
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(2100503)]' (**arg(28, 2100503))
stop music
scene avg_bg_070
$ update_narrator('c0')
with fade
play sfx2 "other_7019.ogg"
get_char('c0') '[convertstrid(2100504)]' (**arg(29, 2100504))
scene avg_bg_025
$ update_narrator('c5051')
with fade
get_char('c5051') '[convertstrid(2100505)]' (**arg(30, 2100505))
get_char('c5051') '[convertstrid(2100506)]' (**arg(31, 2100506))
play sfx2 "other_7063.ogg"
get_char('c5051') '[convertstrid(2100507)]' (**arg(32, 2100507))
$ update_portrait('oc002_01 8', 'p2', [l_entrance(-3), light, flip], 6)
get_char('c21') '[convertstrid(2100508)]' (**arg(33, 2100508))
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2100509)]' (**arg(34, 2100509))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 15', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(2100510)]' (**arg(35, 2100510))
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(2100511)]' (**arg(36, 2100511))
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2100512)]' (**arg(37, 2100512))
$ play_music("ed7500.ogg")
hide p2
hide p1
get_char('c0') '[convertstrid(2100513)]' (**arg(38, 2100513))
get_char('c6881') '[convertstrid(2100514)]' (**arg(39, 2100514))
get_char('c6881') '[convertstrid(2100515)]' (**arg(40, 2100515))
get_char('c6881') '[convertstrid(2100516)]' (**arg(41, 2100516))
get_char('c6881') '[convertstrid(2100517)]' (**arg(42, 2100517))
get_char('c6881') '[convertstrid(2100518)]' (**arg(43, 2100518))
scene avg_bg_024
$ update_portrait('sc015_01 4', 'p23', [l(9), light, flip], 6)
$ update_narrator('c231')
with fade
get_char('c231') '[convertstrid(2100519)]' (**arg(44, 2100519))
$ update_portrait('sc015_01 4', 'p23', [l(9), dark, flip], 5)
$ update_portrait('sc038_01 1', 'p45', [r(-1), light], 6)
get_char('c453') '[convertstrid(2100520)]' (**arg(45, 2100520))
hide p45
$ update_portrait('sc039_01 2', 'p46', [r(-13), light], 6)
get_char('c463') '[convertstrid(2100521)]' (**arg(46, 2100521))
$ update_portrait('sc039_01 2', 'p46', [r(-13), dark], 5)
$ update_portrait('sc015_01 3', 'p23', [l(9), light, flip], 6)
get_char('c231') '[convertstrid(2100522)]' (**arg(47, 2100522))
$ update_portrait('sc015_01 3', 'p23', [l(9), dark, flip], 5)
$ update_portrait('sc039_01 1', 'p46', [r(-13), light], 6)
get_char('c463') '[convertstrid(2100523)]' (**arg(48, 2100523))
$ update_portrait('sc039_01 1', 'p46', [r(-13), dark], 5)
$ update_portrait('sc015_01 3', 'p23', [l(9), light, flip], 6)
get_char('c231') '[convertstrid(2100524)]' (**arg(49, 2100524))
$ update_portrait('sc015_01 1', 'p23', [l(9), light, flip], 6)
get_char('c231') '[convertstrid(2100525)]' (**arg(50, 2100525))
hide p23
$ update_portrait('sc038_01 1', 'p45', [l(-1), light, flip], 6)
get_char('c451') '[convertstrid(2100526)]' (**arg(51, 2100526))
hide p45
$ update_portrait('sc015_01 3', 'p23', [l(9), light, flip], 6)
get_char('c231') '[convertstrid(2100527)]' (**arg(52, 2100527))
$ play_music("ed7506.ogg")
scene avg_bg_025
$ update_narrator('c0')
with fade
play sfx2 "other_7063.ogg"
get_char('c0') '[convertstrid(2100528)]' (**arg(53, 2100528))
get_char('c9773') '[convertstrid(2100529)]' (**arg(54, 2100529))
$ update_portrait('st053_01 1', 'p1007', [l(-12), light, flip], 6)
get_char('c10071') '[convertstrid(2100530)]' (**arg(55, 2100530))
hide p1007
get_char('c11041') '[convertstrid(2100531)]' (**arg(56, 2100531))
get_char('c9773') '[convertstrid(2100532)]' (**arg(57, 2100532))
$ update_portrait('st053_01 1', 'p1007', [l(-12), light, flip], 6)
get_char('c10071') '[convertstrid(2100533)]' (**arg(58, 2100533))
$ update_portrait('st053_01 1', 'p1007', [l(-12), dark, flip], 5)
get_char('c9773') '[convertstrid(2100534)]' (**arg(59, 2100534))
$ update_portrait('st053_01 1', 'p1007', [l(-12), light, flip], 6)
get_char('c10071') '[convertstrid(2100535)]' (**arg(60, 2100535))
hide p1007
get_char('c11041') '[convertstrid(2100536)]' (**arg(61, 2100536))
get_char('c9773') '[convertstrid(2100537)]' (**arg(62, 2100537))
return