label avg10067:

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
play sfxvoice "avg_vocal_na21.ogg"
get_char('c11') '[convertstrid(1005013)]' (**arg(4, 1005013))
hide p693
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('sc015_01 1', 'p23', [r(9), light], 6)
get_char('c233') '[convertstrid(1005014)]' (**arg(5, 1005014))
$ update_portrait('sc015_01 1', 'p23', [r(9), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005015)]' (**arg(6, 1005015))
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005016)]' (**arg(7, 1005016))
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('sc015_01 1', 'p23', [r(9), light], 6)
get_char('c233') '[convertstrid(1005017)]' (**arg(8, 1005017))
hide p1
$ update_portrait('sc015_01 1', 'p23', [r(9), dark], 5)
$ update_portrait('sc040_01 2', 'p47', [l(-9), light, flip], 6)
get_char('c471') '[convertstrid(1005027)]' (**arg(9, 1005027))
$ update_portrait('sc040_01 2', 'p47', [l(-9), dark, flip], 5)
$ update_portrait('sc015_01 1', 'p23', [r(9), light], 6)
get_char('c233') '[convertstrid(1005028)]' (**arg(10, 1005028))
$ update_portrait('sc015_01 1', 'p23', [r(9), dark], 5)
$ update_portrait('sc040_01 6', 'p47', [l(-9), light, flip], 6)
get_char('c471') '[convertstrid(1005029)]' (**arg(11, 1005029))
hide p47
hide p23
get_char('c0') '[convertstrid(1005030)]' (**arg(12, 1005030))
$ update_portrait('sc015_01 2', 'p23', [l(9), light, flip], 6)
get_char('c231') '[convertstrid(1005031)]' (**arg(13, 1005031))
$ update_portrait('sc015_01 6', 'p23', [l(9), light, flip], 6)
get_char('c231') '[convertstrid(1005032)]' (**arg(14, 1005032))
$ update_portrait('sc015_01 1', 'p23', [l(9), light, flip], 6)
get_char('c231') '[convertstrid(1005033)]' (**arg(15, 1005033))
$ update_portrait('sc015_01 1', 'p23', [l(9), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na02.ogg"
get_char('c13') '[convertstrid(1005034)]' (**arg(16, 1005034))
hide p1
$ update_portrait('sc040_01 1', 'p47', [r(-9), light], 6)
get_char('c473') '[convertstrid(1005035)]' (**arg(17, 1005035))
hide p23
$ update_portrait('sc040_01 1', 'p47', [r(-9), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1005036)]' (**arg(18, 1005036))
hide p47
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1005037)]' (**arg(19, 1005037))
hide p1
$ update_portrait('sc039_01 1', 'p46', [r(-13), light], 6)
get_char('c463') '[convertstrid(1005038)]' (**arg(20, 1005038))
hide p2
$ update_portrait('sc039_01 1', 'p46', [r(-13), dark], 5)
$ update_portrait('sc015_01 1', 'p23', [l(9), light, flip], 6)
get_char('c231') '[convertstrid(1005039)]' (**arg(21, 1005039))
return