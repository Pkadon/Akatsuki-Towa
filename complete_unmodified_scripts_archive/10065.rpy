label avg10065:

$ play_music("ED6103.ogg")
scene avg_bg_037
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with fade_in
get_char('c11') '[convertstrid(1005009)]' (**arg(1, 1005009))
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('sc015_01 1', 'p693', [r_entrance(9), light], 6)
get_char('c6933') '[convertstrid(1005010)]' (**arg(2, 1005010))
$ update_portrait('sc015_01 1', 'p693', [r(9), light], 6)
get_char('c6933') '[convertstrid(1005011)]' (**arg(3, 1005011))
$ update_portrait('sc015_01 1', 'p693', [r(9), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005012)]' (**arg(4, 1005012))
hide p1
$ update_portrait('sc007_01 2', 'p15', [l(-17), light, flip], 6)
get_char('c151') '[convertstrid(1005018)]' (**arg(5, 1005018))
hide p693
$ update_portrait('sc007_01 2', 'p15', [l(-17), dark, flip], 5)
$ update_portrait('sc015_01 1', 'p23', [r(9), light], 6)
get_char('c233') '[convertstrid(1005019)]' (**arg(6, 1005019))
$ update_portrait('sc015_01 1', 'p23', [r(9), dark], 5)
$ update_portrait('sc007_01 1', 'p15', [l(-17), light, flip], 6)
get_char('c151') '[convertstrid(1005020)]' (**arg(7, 1005020))
hide p15
hide p23
get_char('c0') '[convertstrid(1005021)]' (**arg(8, 1005021))
$ update_portrait('sc015_01 2', 'p23', [r(9), light], 6)
get_char('c233') '[convertstrid(1005022)]' (**arg(9, 1005022))
$ update_portrait('sc015_01 1', 'p23', [r(9), light], 6)
get_char('c233') '[convertstrid(1005023)]' (**arg(10, 1005023))
$ update_portrait('sc015_01 1', 'p23', [r(9), light], 6)
get_char('c233') '[convertstrid(1005024)]' (**arg(11, 1005024))
$ update_portrait('sc015_01 1', 'p23', [r(9), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na02.ogg"
get_char('c11') '[convertstrid(1005025)]' (**arg(12, 1005025))
hide p23
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('sc007_01 1', 'p15', [r(-17), light], 6)
get_char('c153') '[convertstrid(1005026)]' (**arg(13, 1005026))
hide p1
$ update_portrait('sc007_01 1', 'p15', [r(-17), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1005036)]' (**arg(14, 1005036))
hide p15
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1005037)]' (**arg(15, 1005037))
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc039_01 1', 'p46', [l(-13), light, flip], 6)
get_char('c461') '[convertstrid(1005038)]' (**arg(16, 1005038))
hide p1
$ update_portrait('sc039_01 1', 'p46', [l(-13), dark, flip], 5)
$ update_portrait('sc015_01 1', 'p23', [r(9), light], 6)
get_char('c233') '[convertstrid(1005039)]' (**arg(17, 1005039))
return