label avg10390(trans=fade_in):

$ play_music("ed7511.ogg")
scene avg_bg_049
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1132472)]' (**arg(1, 1132472))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1132474)]' (**arg(2, 1132474))
hide p2
$ update_portrait('oc003_01 3', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1132475)]' (**arg(3, 1132475))
hide p1
$ update_portrait('oc003_01 3', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 16', 'p4', [r(-5), light], 6)
play sfx2 "other_7085.ogg"
play sfxvoice "avg_vocal_li23.ogg"
get_char('c43') '[convertstrid(1132476)]' (**arg(4, 1132476))
hide p3
hide p4
$ update_portrait('uc003_04 3', 'p1045', [l(-14), light, flip], 6)
$ update_narrator('c10451')
with fade
play sfx2 "fight_6006.ogg"
get_char('c10451') '[convertstrid(1132477)]' (**arg(5, 1132477)) with shake
hide p1045
$ update_portrait('uc003_04 3', 'p1046', [l(-14), light, flip], 6)
play sfx2 "fight_6003.ogg"
get_char('c10461') '[convertstrid(1132478)]' (**arg(6, 1132478)) with shake
hide p1046
get_char('c0') '[convertstrid(1132479)]' (**arg(7, 1132479))
$ update_portrait('sc048_01 4', 'p55', [r_entrance_midback(-7), light], 6)
play sfx2 "fight_6003.ogg"
get_char('c553') '[convertstrid(1132480)]' (**arg(8, 1132480))
$ update_portrait('sc048_01 4', 'p55', [r(-7), dark], 5)
$ update_portrait('uc003_04 3', 'p1045', [l(-14), light, flip], 6)
get_char('c10451') '[convertstrid(1132481)]' (**arg(9, 1132481))
hide p1045
$ update_portrait('uc003_04 3', 'p1046', [l(-14), light, flip], 6)
get_char('c10461') '[convertstrid(1132482)]' (**arg(10, 1132482))
hide p1046
$ update_portrait('uc003_04 4', 'p1045', [l(-14), light, flip], 6)
get_char('c10451') '[convertstrid(1132483)]' (**arg(11, 1132483))
hide p1045
$ update_portrait('uc003_04 3', 'p1046', [l(-14), light, flip], 6)
get_char('c10461') '[convertstrid(1132484)]' (**arg(12, 1132484))
hide p1046
hide p55
$ update_narrator('c2391')
$ update_portrait('st040_01 5', 'p239', [l(-19), light, flip], 6)
with fade
$ update_portrait('st040_01 5', 'p239', [l_midback(-19), light, flip], 6)
play sfx2 "fight_6006.ogg"
get_char('c2391') '[convertstrid(1132485)]' (**arg(13, 1132485))
$ update_portrait('st040_01 5', 'p239', [l(-19), dark, flip], 5)
$ update_portrait('uc003_04 2', 'p1046', [r(-14), light], 6)
play sfx2 "other_7007.ogg"
get_char('c10463') '[convertstrid(1132486)]' (**arg(14, 1132486)) with shake
$ update_portrait('uc003_04 2', 'p1046', [r(-14), r_shake, light], 6)
get_char('c10463') '[convertstrid(1132487)]' (**arg(15, 1132487))
hide p1046
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1132488)]' (**arg(16, 1132488))
hide p239
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 10', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1132489)]' (**arg(17, 1132489))
hide p4
hide p1
$ update_narrator('c553')
$ update_portrait('sc048_01 4', 'p55', [r(-7), light], 6)
with fade
$ update_portrait('sc048_01 4', 'p55', [r_midback(-7), light], 6)
play sfx2 "fight_6003.ogg"
get_char('c553') '[convertstrid(1132490)]' (**arg(18, 1132490))
$ update_portrait('sc048_01 4', 'p55', [r(-7), dark], 5)
$ update_portrait('uc003_04 3', 'p1045', [l(-14), light, flip], 6)
get_char('c10451') '[convertstrid(1132491)]' (**arg(19, 1132491))
$ update_portrait('uc003_04 3', 'p1045', [l(-14), light, flip], 6)
get_char('c10451') '[convertstrid(1132492)]' (**arg(20, 1132492))
hide p55
$ update_portrait('uc003_04 3', 'p1045', [l(-14), dark, flip], 5)
play sfx2 "other_7085.ogg"
get_char('c10473') '[convertstrid(1132493)]' (**arg(21, 1132493))
play sfx2 "other_7085.ogg"
get_char('c10483') '[convertstrid(1132494)]' (**arg(22, 1132494))
hide p1045
$ update_portrait('oc004_01 12', 'p4', [r(-5), light], 6)
$ update_narrator('c43')
with fade
play sfxvoice "avg_vocal_li31.ogg"
get_char('c43') '[convertstrid(1132495)]' (**arg(23, 1132495))
$ update_portrait('oc004_01 12', 'p4', [r(-5), dark], 5)
$ update_portrait('st040_01 4', 'p239', [l(-19), light, flip], 6)
get_char('c2391') '[convertstrid(1132496)]' (**arg(24, 1132496))
stop music
scene avg_bg_070
$ update_narrator('c0')
with fade
get_char('c0') '[convertstrid(1132497)]' (**arg(25, 1132497))
$ play_music("ed7151.ogg")
scene avg_bg_049
$ update_portrait('st040_01 4', 'p239', [r(-19), light], 6)
$ update_narrator('c2393')
with fade
get_char('c2393') '[convertstrid(1132498)]' (**arg(26, 1132498))
$ update_portrait('st040_01 4', 'p239', [r(-19), dark], 5)
$ update_portrait('sc048_01 2', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1132499)]' (**arg(27, 1132499))
$ update_portrait('sc048_01 2', 'p55', [l(-7), dark, flip], 5)
$ update_portrait('st040_01 4', 'p239', [r(-19), light], 6)
get_char('c2393') '[convertstrid(1132500)]' (**arg(28, 1132500))
$ update_portrait('st040_01 4', 'p239', [r(-19), dark], 5)
$ update_portrait('sc048_01 4', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1132501)]' (**arg(29, 1132501))
hide p239
$ update_portrait('sc048_01 4', 'p55', [l(-7), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1132502)]' (**arg(30, 1132502))
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1132503)]' (**arg(31, 1132503))
$ update_portrait('oc001_01 17', 'p1', [r(-2), dark], 5)
$ update_portrait('sc048_01 1', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1132504)]' (**arg(32, 1132504))
hide p1
$ update_portrait('sc048_01 1', 'p55', [l(-7), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c23') '[convertstrid(1132505)]' (**arg(33, 1132505))
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('sc048_01 4', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1132506)]' (**arg(34, 1132506))
$ update_portrait('sc048_01 4', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1132507)]' (**arg(35, 1132507))
hide p2
$ update_portrait('sc048_01 4', 'p55', [l(-7), dark, flip], 5)
$ update_portrait('st040_01 5', 'p239', [r(-19), light], 6)
get_char('c2393') '[convertstrid(1132508)]' (**arg(36, 1132508))
hide p239
$ update_portrait('oc002_01 9', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1132509)]' (**arg(37, 1132509))
$ update_portrait('oc002_01 9', 'p2', [r(-3), dark], 5)
$ update_portrait('sc048_01 1', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1132510)]' (**arg(38, 1132510))
hide p2
$ update_portrait('sc048_01 1', 'p55', [l(-7), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1132511)]' (**arg(39, 1132511))
hide p1
$ update_portrait('oc004_01 18', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li18.ogg"
get_char('c43') '[convertstrid(1132512)]' (**arg(40, 1132512))
hide p4
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1132513)]' (**arg(41, 1132513))
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1132514)]' (**arg(42, 1132514))
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
$ update_portrait('sc048_01 3', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1132515)]' (**arg(43, 1132515))
$ update_portrait('sc048_01 3', 'p55', [l(-7), dark, flip], 5)
$ update_portrait('oc002_01 17', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1132516)]' (**arg(44, 1132516))
$ update_portrait('oc002_01 17', 'p2', [r(-3), dark], 5)
$ update_portrait('sc048_01 4', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1132517)]' (**arg(45, 1132517))
$ update_portrait('sc048_01 4', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1132518)]' (**arg(46, 1132518))
$ update_portrait('sc048_01 4', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1132519)]' (**arg(47, 1132519))
$ update_portrait('sc048_01 1', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1132520)]' (**arg(48, 1132520))
$ update_portrait('sc048_01 4', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1132521)]' (**arg(49, 1132521))
$ update_portrait('sc048_01 4', 'p55', [l(-7), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1132522)]' (**arg(50, 1132522))
hide p2
$ update_portrait('oc004_01 21', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li19.ogg"
get_char('c43') '[convertstrid(1132523)]' (**arg(51, 1132523))
hide p4
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1132524)]' (**arg(52, 1132524))
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na06.ogg"
get_char('c13') '[convertstrid(1132525)]' (**arg(53, 1132525))
$ update_portrait('oc001_01 18', 'p1', [r(-2), dark], 5)
$ update_portrait('sc048_01 1', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1132526)]' (**arg(54, 1132526))
$ update_portrait('sc048_01 4', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1132527)]' (**arg(55, 1132527))
hide p1
$ update_portrait('sc048_01 4', 'p55', [l(-7), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro19.ogg"
get_char('c33') '[convertstrid(1132528)]' (**arg(56, 1132528))
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('sc048_01 4', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1132529)]' (**arg(57, 1132529))
hide p3
$ update_portrait('sc048_01 4', 'p55', [l(-7), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch17.ogg"
get_char('c23') '[convertstrid(1132530)]' (**arg(58, 1132530))
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1132531)]' (**arg(59, 1132531))
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na06.ogg"
get_char('c13') '[convertstrid(1132532)]' (**arg(60, 1132532))
hide p55
$ update_portrait('oc001_01 18', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 17', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li18.ogg"
get_char('c41') '[convertstrid(1132533)]' (**arg(61, 1132533))
hide p4
$ update_portrait('sc048_01 4', 'p55', [l_entrance(-7), light, flip], 6)
get_char('c551') '[convertstrid(1132534)]' (**arg(62, 1132534))
$ update_portrait('sc048_01 4', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1132535)]' (**arg(63, 1132535))
$ update_portrait('sc048_01 1', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1132536)]' (**arg(64, 1132536))
$ update_portrait('sc048_01 4', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1132537)]' (**arg(65, 1132537))
$ update_portrait('sc048_01 1', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1132538)]' (**arg(66, 1132538))
$ update_portrait('sc048_01 1', 'p55', [l(-7), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1132539)]' (**arg(67, 1132539))
hide p55
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch24.ogg"
get_char('c21') '[convertstrid(1132540)]' (**arg(68, 1132540))
hide p2
$ update_portrait('oc004_01 16', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li23.ogg"
get_char('c41') '[convertstrid(1132541)]' (**arg(69, 1132541))
hide p4
hide p1
$ update_portrait('st040_01 5', 'p239', [l(-19), light, flip], 6)
$ update_narrator('c2391')
with fade
get_char('c2391') '[convertstrid(1132542)]' (**arg(70, 1132542))
$ update_portrait('st040_01 1', 'p239', [l(-19), light, flip], 6)
get_char('c2391') '[convertstrid(1132543)]' (**arg(71, 1132543))
hide p239
get_char('c10471') '[convertstrid(1132544)]' (**arg(72, 1132544))
get_char('c10481') '[convertstrid(1132545)]' (**arg(73, 1132545))
$ update_portrait('uc003_04 4', 'p1045', [r(-14), l_shake, light], 6)
get_char('c10453') '[convertstrid(1132546)]' (**arg(74, 1132546))
hide p1045
$ update_portrait('uc003_04 4', 'p1046', [r(-14), l_shake, light], 6)
get_char('c10463') '[convertstrid(1132547)]' (**arg(75, 1132547))
hide p1046
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
with fade
get_char('c13') '[convertstrid(1132548)]' (**arg(76, 1132548))
$ update_portrait('oc001_01 18', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro19.ogg"
get_char('c31') '[convertstrid(1132549)]' (**arg(77, 1132549))
hide p1
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 9', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1132550)]' (**arg(78, 1132550))
hide p2
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1132551)]' (**arg(79, 1132551))
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1132552)]' (**arg(80, 1132552))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1132553)]' (**arg(81, 1132553))
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc048_01 4', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1132554)]' (**arg(82, 1132554))
hide p1
$ update_portrait('sc048_01 4', 'p55', [l(-7), dark, flip], 5)
get_char('c10573') '[convertstrid(1132555)]' (**arg(83, 1132555, size=(1.3)))
return "avg10390"