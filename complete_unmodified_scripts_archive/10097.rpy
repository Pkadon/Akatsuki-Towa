label avg10097(trans=fade_in):

$ play_music("ED6103.ogg")
scene avg_bg_038
$ update_narrator('c6923')
window show
with trans
$ update_portrait('st044_01 2', 'p692', [r_entrance(10), light], 6)
play sfx2 "other_7047.ogg"
get_char('c6923') '[convertstrid(1005503)]' (**arg(1, 1005503))
$ update_portrait('st044_01 2', 'p692', [r(10), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l_entrance(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005504)]' (**arg(2, 1005504))
hide p1
hide p692
get_char('c0') '[convertstrid(1005505)]' (**arg(3, 1005505))
$ update_portrait('st044_01 4', 'p692', [r(10), light], 6)
get_char('c6923') '[convertstrid(1005506)]' (**arg(4, 1005506))
$ update_portrait('st044_01 4', 'p692', [r(10), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na02.ogg"
get_char('c11') '[convertstrid(1005507)]' (**arg(5, 1005507))
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('st044_01 2', 'p692', [r(10), light], 6)
get_char('c6923') '[convertstrid(1005508)]' (**arg(6, 1005508))
$ update_portrait('st044_01 1', 'p692', [r(10), light], 6)
play sfx2 "other_7022.ogg"
get_char('c6923') '[convertstrid(1005509)]' (**arg(7, 1005509))
hide p1
$ update_portrait('st044_01 1', 'p692', [r(10), dark], 5)
$ update_portrait('sc007_01 1', 'p15', [l(-17), light, flip], 6)
get_char('c151') '[convertstrid(1005512)]' (**arg(8, 1005512))
$ update_portrait('sc007_01 1', 'p15', [l(-17), dark, flip], 5)
$ update_portrait('st044_01 4', 'p692', [r(10), light], 6)
get_char('c6923') '[convertstrid(1005513)]' (**arg(9, 1005513))
hide p15
hide p692
get_char('c0') '[convertstrid(1005514)]' (**arg(10, 1005514))
$ play_music("ed7151.ogg")
$ update_portrait('oc004_01 12', 'p4', [l(-5), l_shake, light, flip], 6)
play sfx2 "other_7007.ogg"
play sfxvoice "avg_vocal_li31.ogg"
get_char('c41') '[convertstrid(1005515)]' (**arg(11, 1005515))
$ update_portrait('oc004_01 12', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('sc039_01 2', 'p46', [r(-13), light], 6)
get_char('c463') '[convertstrid(1005516)]' (**arg(12, 1005516))
$ update_portrait('sc039_01 2', 'p46', [r(-13), dark], 5)
$ update_portrait('oc004_01 3', 'p4', [l_exit(-5), light, flip], 6)
get_char('c41') '[convertstrid(1005517)]' (**arg(13, 1005517))
hide p4
$ update_portrait('oc001_01 12', 'p1', [l_entrance(-2), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c11') '[convertstrid(1005518)]' (**arg(14, 1005518))
hide p46
$ update_portrait('oc001_01 12', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 9', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1005519)]' (**arg(15, 1005519))
hide p1
$ update_portrait('oc002_01 9', 'p2', [r(-3), dark], 5)
$ update_portrait('sc015_01 1', 'p23', [l(9), light, flip], 6)
get_char('c231') '[convertstrid(1005520)]' (**arg(16, 1005520))
hide p2
$ update_portrait('sc015_01 1', 'p23', [l(9), dark, flip], 5)
$ update_portrait('sc007_01 2', 'p15', [r(-17), light], 6)
get_char('c153') '[convertstrid(1005521)]' (**arg(17, 1005521))
hide p15
$ update_portrait('sc039_01 1', 'p46', [r(-13), light], 6)
get_char('c463') '[convertstrid(1005522)]' (**arg(18, 1005522))
hide p23
$ update_portrait('sc039_01 1', 'p46', [r(-13), dark], 5)
$ update_portrait('sc040_01 4', 'p47', [l(-9), light, flip], 6)
get_char('c471') '[convertstrid(1005523)]' (**arg(19, 1005523))
hide p46
$ update_portrait('sc040_01 4', 'p47', [l(-9), dark, flip], 5)
$ update_portrait('st044_01 2', 'p692', [r(10), light], 6)
get_char('c6923') '[convertstrid(1005524)]' (**arg(20, 1005524))
hide p47
$ update_portrait('st044_01 2', 'p692', [r(10), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch19.ogg"
get_char('c21') '[convertstrid(1005525)]' (**arg(21, 1005525))
hide p692
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1005526)]' (**arg(22, 1005526))
hide p2
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005527)]' (**arg(23, 1005527))
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc004_01 3', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li26.ogg"
get_char('c43') '[convertstrid(1005528)]' (**arg(24, 1005528))
$ update_portrait('oc004_01 3', 'p4', [r(-5), dark], 5)
$ update_portrait('oc001_01 12', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005529)]' (**arg(25, 1005529))
$ update_portrait('oc001_01 12', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc004_01 7', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1005530)]' (**arg(26, 1005530))
hide p4
$ update_portrait('sc040_01 4', 'p47', [r(-9), light], 6)
get_char('c473') '[convertstrid(1005531)]' (**arg(27, 1005531))
$ update_portrait('sc040_01 4', 'p47', [r(-9), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005532)]' (**arg(28, 1005532))
hide p47
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc004_01 7', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1005533)]' (**arg(29, 1005533))
hide p1
$ update_portrait('oc004_01 7', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1005534)]' (**arg(30, 1005534))
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1005535)]' (**arg(31, 1005535))
hide p2
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na22.ogg"
get_char('c11') '[convertstrid(1005536)]' (**arg(32, 1005536, size=(0.8)))
menu:
    extend ""
    '[convertstrid(1005537)]':
        call avg10098
    '[convertstrid(1005538)]':
        call avg10099
return _return