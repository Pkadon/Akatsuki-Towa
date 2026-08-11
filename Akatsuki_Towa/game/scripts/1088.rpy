label avg1088(trans=fade_in):

$ play_music("ed7150.ogg")
scene avg_bg_023
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
$ update_narrator('c561')
window show
with trans
play sfx2 "other_7047.ogg"
get_char('c561') '[convertstrid(2101921)]' (**arg(1, 2101921))
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r_entrance(-2), light], 6)
play sfxvoice "avg_vocal_na20.ogg"
get_char('c13') '[convertstrid(2101922)]' (**arg(2, 2101922))
hide p56
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(2101923)]' (**arg(3, 2101923))
hide p1
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 7', 'p4', [r(-5), r_shake, light], 6)
get_char('c43') '[convertstrid(2101924)]' (**arg(4, 2101924))
hide p4
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch23.ogg"
get_char('c23') '[convertstrid(2101925)]' (**arg(5, 2101925))
hide p3
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2101926)]' (**arg(6, 2101926))
hide p2
$ update_portrait('sc049_01 5', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc004_01 12', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li11.ogg"
get_char('c43') '[convertstrid(2101927)]' (**arg(7, 2101927))
$ update_portrait('oc004_01 12', 'p4', [r(-5), dark], 5)
$ update_portrait('sc049_01 2', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2101928)]' (**arg(8, 2101928))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2101929)]' (**arg(9, 2101929))
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc004_01 11', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(2101930)]' (**arg(10, 2101930))
hide p56
$ update_portrait('oc004_01 11', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro08.ogg"
get_char('c31') '[convertstrid(2101931)]' (**arg(11, 2101931))
hide p4
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 6', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(2101932)]' (**arg(12, 2101932))
hide p3
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 12', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(2101933)]' (**arg(13, 2101933))
hide p4
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2101934)]' (**arg(14, 2101934))
hide p56
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(2101935)]' (**arg(15, 2101935))
hide p2
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2101936)]' (**arg(16, 2101936))
hide p3
hide p1
get_char('c0') '[convertstrid(2101937)]' (**arg(17, 2101937))
$ update_portrait('oc001_01 22', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2101938)]' (**arg(18, 2101938))
$ update_portrait('oc001_01 22', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(2101939)]' (**arg(19, 2101939))
scene avg_bg_013
$ update_narrator('c0')
with fade
get_char('c0') '[convertstrid(2101940)]' (**arg(20, 2101940))
get_char('c0') '[convertstrid(2101941)]' (**arg(21, 2101941))
return "avg1088"