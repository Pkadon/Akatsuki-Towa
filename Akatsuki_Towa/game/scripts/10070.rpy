label avg10070:

$ play_music("ED6103.ogg")
scene avg_bg_038
$ update_narrator('c6923')
window show
with fade_in
$ update_portrait('st044_01 2', 'p692', [r_entrance(10), light], 6)
get_char('c6923') '[convertstrid(1005040)]' (**arg(1, 1005040))
$ update_portrait('st044_01 2', 'p692', [r(10), dark], 5)
$ update_portrait('oc001_01 10', 'p1', [l_entrance(-2), light, flip], 6)
play sfx2 "other_7047.ogg"
play sfxvoice "avg_vocal_na20.ogg"
get_char('c11') '[convertstrid(1005041)]' (**arg(2, 1005041))
$ update_portrait('oc001_01 10', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('st044_01 4', 'p692', [r(10), light], 6)
get_char('c6923') '[convertstrid(1005042)]' (**arg(3, 1005042))
$ update_portrait('st044_01 2', 'p692', [r(10), light], 6)
get_char('c6923') '[convertstrid(1005043)]' (**arg(4, 1005043))
$ update_portrait('st044_01 1', 'p692', [r(10), light], 6)
get_char('c6923') '[convertstrid(1005044)]' (**arg(5, 1005044))
hide p1
$ update_portrait('st044_01 1', 'p692', [r(10), dark], 5)
$ update_portrait('sc040_01 1', 'p47', [l(-9), light, flip], 6)
get_char('c471') '[convertstrid(1005045)]' (**arg(6, 1005045))
hide p47
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005049)]' (**arg(7, 1005049))
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('st044_01 1', 'p692', [r(10), light], 6)
get_char('c6923') '[convertstrid(1005050)]' (**arg(8, 1005050))
hide p1
hide p692
play sfx2 "other_7064.ogg"
get_char('c0') '[convertstrid(1005051)]' (**arg(9, 1005051))
$ update_portrait('st044_01 4', 'p692', [r_entrance(10), light], 6)
get_char('c6923') '[convertstrid(1005052)]' (**arg(10, 1005052))
hide p692
$ update_portrait('sc007_01 4', 'p15', [r_entrance(-17), light], 6)
get_char('c153') '[convertstrid(1005053)]' (**arg(11, 1005053))
$ update_portrait('sc007_01 4', 'p15', [r(-17), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1005054)]' (**arg(12, 1005054))
hide p15
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('sc040_01 4', 'p47', [r(-9), light], 6)
get_char('c473') '[convertstrid(1005055)]' (**arg(13, 1005055))
hide p4
$ update_portrait('sc040_01 4', 'p47', [r(-9), dark], 5)
$ update_portrait('sc015_01 1', 'p23', [l(9), light, flip], 6)
get_char('c231') '[convertstrid(1005056)]' (**arg(14, 1005056))
$ update_portrait('sc015_01 1', 'p23', [l(9), dark, flip], 5)
$ update_portrait('sc040_01 1', 'p47', [r(-9), light], 6)
get_char('c473') '[convertstrid(1005057)]' (**arg(15, 1005057))
hide p23
$ update_portrait('sc040_01 1', 'p47', [r(-9), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1005058)]' (**arg(16, 1005058))
hide p47
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('sc007_01 2', 'p15', [r(-17), light], 6)
get_char('c153') '[convertstrid(1005059)]' (**arg(17, 1005059))
hide p15
$ update_portrait('st044_01 2', 'p692', [r(10), light], 6)
get_char('c6923') '[convertstrid(1005060)]' (**arg(18, 1005060))
$ update_portrait('st044_01 2', 'p692', [r(10), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1005061)]' (**arg(19, 1005061))
hide p4
$ update_portrait('sc015_01 1', 'p23', [l(9), light, flip], 6)
get_char('c231') '[convertstrid(1005062)]' (**arg(20, 1005062))
hide p692
$ update_portrait('sc015_01 1', 'p23', [l(9), dark, flip], 5)
$ update_portrait('sc040_01 1', 'p47', [r(-9), light], 6)
get_char('c473') '[convertstrid(1005063)]' (**arg(21, 1005063))
hide p47
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1005064)]' (**arg(22, 1005064))
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1005065)]' (**arg(23, 1005065))
hide p23
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1005066)]' (**arg(24, 1005066))
hide p2
$ update_portrait('sc039_01 5', 'p46', [l(-13), light, flip], 6)
get_char('c461') '[convertstrid(1005067)]' (**arg(25, 1005067))
$ update_portrait('sc039_01 5', 'p46', [l(-13), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1005068)]' (**arg(26, 1005068))
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1005069)]' (**arg(27, 1005069))
hide p46
$ update_portrait('oc001_01 20', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1005070)]' (**arg(28, 1005070))
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1005071)]' (**arg(29, 1005071))
hide p2
hide p1
get_char('c0') '[convertstrid(1005072)]' (**arg(30, 1005072))
return