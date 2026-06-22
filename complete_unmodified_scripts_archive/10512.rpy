label avg10512:

$ play_music("ED6300.ogg")
scene placeholderbackground
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1150495)]' (**arg(1, 1150495))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
play sfx2 "fight_6015.ogg"
get_char('c12031') '[convertstrid(1150496)]' (**arg(2, 1150496)) with shake
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
play sfx2 "fight_6016.ogg"
get_char('c23') '[convertstrid(1150497)]' (**arg(3, 1150497)) with shake
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
get_char('c12031') '[convertstrid(1150498)]' (**arg(4, 1150498))
hide p2
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1150499)]' (**arg(5, 1150499))
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
get_char('c12031') '[convertstrid(1150500)]' (**arg(6, 1150500))
get_char('c12031') '[convertstrid(1150501)]' (**arg(7, 1150501))
get_char('c12031') '[convertstrid(1150502)]' (**arg(8, 1150502))
hide p3
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1150503)]' (**arg(9, 1150503))
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1150504)]' (**arg(10, 1150504))
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
get_char('c12031') '[convertstrid(1150505)]' (**arg(11, 1150505))
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1150506)]' (**arg(12, 1150506))
hide p1
$ update_portrait('oc007_01 2', 'p7', [l(-24), light, flip], 6)
$ update_narrator('c71')
with fade
get_char('c71') '[convertstrid(1150507)]' (**arg(13, 1150507))
$ update_portrait('oc007_01 2', 'p7', [l(-24), dark, flip], 5)
$ update_portrait('st040_01 1', 'p239', [r(-19), light], 6)
get_char('c2393') '[convertstrid(1150508)]' (**arg(14, 1150508))
hide p7
hide p239
$ update_portrait('oc002_01 15', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
with fade
get_char('c23') '[convertstrid(1150509)]' (**arg(15, 1150509))
$ update_portrait('oc002_01 15', 'p2', [r(-3), dark], 5)
$ update_portrait('st040_01 1', 'p239', [l(-19), light, flip], 6)
get_char('c2391') '[convertstrid(1150510)]' (**arg(16, 1150510))
$ update_portrait('st040_01 1', 'p239', [l(-19), light, flip], 6)
get_char('c2391') '[convertstrid(1150511)]' (**arg(17, 1150511))
hide p2
$ update_portrait('st040_01 1', 'p239', [l(-19), dark, flip], 5)
$ update_portrait('oc004_01 2', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1150512)]' (**arg(18, 1150512))
$ update_portrait('oc004_01 2', 'p4', [r(-5), dark], 5)
$ update_portrait('st040_01 1', 'p239', [l(-19), light, flip], 6)
get_char('c2391') '[convertstrid(1150513)]' (**arg(19, 1150513))
hide p4
$ update_portrait('st040_01 1', 'p239', [l(-19), dark, flip], 5)
$ update_portrait('sc007_01 1', 'p15', [r(-17), light], 6)
get_char('c153') '[convertstrid(1150514)]' (**arg(20, 1150514))
hide p239
$ update_portrait('sc007_01 1', 'p15', [r(-17), dark], 5)
get_char('c12051') '[convertstrid(1150515)]' (**arg(21, 1150515))
hide p15
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1150516)]' (**arg(22, 1150516))
hide p2
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1150517)]' (**arg(23, 1150517))
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('oc007_01 1', 'p7', [l(-24), light, flip], 6)
get_char('c71') '[convertstrid(1150518)]' (**arg(24, 1150518))
$ update_portrait('oc007_01 1', 'p7', [l(-24), light, flip], 6)
get_char('c71') '[convertstrid(1150519)]' (**arg(25, 1150519))
$ update_portrait('oc007_01 1', 'p7', [l(-24), light, flip], 6)
get_char('c71') '[convertstrid(1150520)]' (**arg(26, 1150520))
hide p7
get_char('c12031') '[convertstrid(1150521)]' (**arg(27, 1150521))
$ update_portrait('oc007_01 2', 'p7', [l(-24), l_shake, light, flip], 6)
get_char('c71') '[convertstrid(1150522)]' (**arg(28, 1150522))
$ update_portrait('oc007_01 1', 'p7', [l(-24), light, flip], 6)
get_char('c71') '[convertstrid(1150523)]' (**arg(29, 1150523))
hide p3
$ update_portrait('oc007_01 1', 'p7', [l(-24), dark, flip], 5)
$ update_portrait('st040_01 3', 'p239', [r(-19), light], 6)
get_char('c2393') '[convertstrid(1150524)]' (**arg(30, 1150524))
hide p7
$ update_portrait('st040_01 3', 'p239', [r(-19), dark], 5)
get_char('c12031') '[convertstrid(1150525)]' (**arg(31, 1150525))
hide p239
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1150526)]' (**arg(32, 1150526))
hide p3
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1150527)]' (**arg(33, 1150527))
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
get_char('c12041') '[convertstrid(1150528)]' (**arg(34, 1150528))
hide p2
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1150529)]' (**arg(35, 1150529))
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('st040_01 4', 'p239', [l(-19), light, flip], 6)
get_char('c2391') '[convertstrid(1150530)]' (**arg(36, 1150530))
return