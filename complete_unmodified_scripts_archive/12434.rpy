label avg12434(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_023
$ update_narrator('c561')
window show
with trans
$ update_portrait('sc049_01 2', 'p56', [l_entrance(-8), light, flip], 6)
get_char('c561') '[convertstrid(1143130)]' (**arg(1, 1143130))
$ update_portrait('sc049_01 2', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na02.ogg"
get_char('c13') '[convertstrid(1143131)]' (**arg(2, 1143131))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1143132)]' (**arg(3, 1143132))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1143133)]' (**arg(4, 1143133))
hide p1
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1143134)]' (**arg(5, 1143134))
$ update_portrait('oc002_01 5', 'p2', [r(-3), dark], 5)
$ update_portrait('sc049_01 2', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1143135)]' (**arg(6, 1143135))
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1143136)]' (**arg(7, 1143136))
$ update_portrait('sc049_01 5', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc002_01 21', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1143137)]' (**arg(8, 1143137))
$ update_portrait('oc002_01 21', 'p2', [r(-3), dark], 5)
$ update_portrait('sc049_01 4', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1143138)]' (**arg(9, 1143138))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1143139)]' (**arg(10, 1143139))
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc002_01 14', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch08.ogg"
get_char('c23') '[convertstrid(1143140)]' (**arg(11, 1143140))
hide p2
$ update_portrait('oc003_01 16', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1143141)]' (**arg(12, 1143141))
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1143142)]' (**arg(13, 1143142))
hide p56
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
$ update_portrait('oc001_01 18', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1143143)]' (**arg(14, 1143143))
hide p3
$ update_portrait('oc001_01 18', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1143144)]' (**arg(15, 1143144))
hide p1
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1143145)]' (**arg(16, 1143145))
$ update_portrait('oc003_01 18', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1143146)]' (**arg(17, 1143146))
hide p2
$ update_portrait('oc003_01 18', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1143147)]' (**arg(18, 1143147))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1143148)]' (**arg(19, 1143148))
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 6', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1143149)]' (**arg(20, 1143149))
hide p1
$ update_portrait('sc049_01 6', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc002_01 9', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1143150)]' (**arg(21, 1143150))
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na02.ogg"
get_char('c13') '[convertstrid(1143151)]' (**arg(22, 1143151))
return "avg12434"