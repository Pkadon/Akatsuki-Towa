label avg12024:

$ play_music("ed7161.ogg")
scene avg_bg_013
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
$ update_narrator('c561')
window show
with fade_in
get_char('c561') '[convertstrid(1120015)]' (**arg(1, 1120015))
scene avg_bg_023
$ update_portrait('sc050_01 3', 'p57', [r(-19), light], 6)
$ update_narrator('c573')
with fade
get_char('c573') '[convertstrid(1120016)]' (**arg(2, 1120016))
$ update_portrait('sc050_01 3', 'p57', [r(-19), dark], 5)
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
play sfx2 "fight_6024.ogg"
get_char('c11') '[convertstrid(1120017)]' (**arg(3, 1120017))
hide p57
$ update_portrait('oc001_01 8', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('sc052_01 3', 'p59', [r(-25), light], 6)
get_char('c593') '[convertstrid(1120018)]' (**arg(4, 1120018))
hide p1
$ update_portrait('sc052_01 3', 'p59', [r(-25), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1120019)]' (**arg(5, 1120019))
hide p59
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 11', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120020)]' (**arg(6, 1120020))
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c23') '[convertstrid(1120021)]' (**arg(7, 1120021))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1120022)]' (**arg(8, 1120022))
hide p56
hide p2
play sfx2 "other_7088.ogg"
get_char('c0') '[convertstrid(1120023)]' (**arg(9, 1120023))
$ update_portrait('sc052_01 6', 'p59', [r(-25), light], 6)
get_char('c593') '[convertstrid(1120024)]' (**arg(10, 1120024))
hide p59
$ update_portrait('sc050_01 1', 'p57', [r(-19), light], 6)
get_char('c573') '[convertstrid(1120025)]' (**arg(11, 1120025))
$ update_portrait('sc050_01 1', 'p57', [r(-19), dark], 5)
$ update_portrait('sc049_01 2', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1120026)]' (**arg(12, 1120026))
hide p57
$ update_portrait('sc049_01 2', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1120027)]' (**arg(13, 1120027))
$ update_portrait('oc001_01 23', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120028)]' (**arg(14, 1120028))
hide p56
$ update_portrait('oc001_01 23', 'p1', [r(-2), dark], 5)
$ update_portrait('sc052_01 2', 'p59', [l(-25), light, flip], 6)
get_char('c591') '[convertstrid(1120029)]' (**arg(15, 1120029))
hide p1
$ update_portrait('sc052_01 2', 'p59', [l(-25), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1120030)]' (**arg(16, 1120030))
$ update_portrait('oc002_01 11', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1120031)]' (**arg(17, 1120031))
hide p59
$ update_portrait('oc002_01 11', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1120032)]' (**arg(18, 1120032))
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1120033)]' (**arg(19, 1120033))
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('sc049_01 7', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1120034)]' (**arg(20, 1120034))
$ update_portrait('sc049_01 6', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1120035)]' (**arg(21, 1120035))
hide p2
$ update_portrait('sc049_01 6', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120036)]' (**arg(22, 1120036))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
play sfx2 "other_7091.ogg"
get_char('c561') '[convertstrid(1120037)]' (**arg(23, 1120037))
hide p1
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc002_01 9', 'p2', [r(-3), r_shake, light], 6)
play sfxvoice "avg_vocal_ch24.ogg"
get_char('c23') '[convertstrid(1120038)]' (**arg(24, 1120038))
hide p56
$ update_portrait('oc002_01 9', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1120039)]' (**arg(25, 1120039))
return