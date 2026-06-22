label avg12224:

$ play_music("ED6103.ogg")
scene avg_bg_072
$ update_narrator('c21')
window show
with fade_in
$ update_portrait('oc002_01 5', 'p2', [l_entrance(-3), light, flip], 6)
play sfx2 "other_7047.ogg"
play sfxvoice "avg_vocal_ch07.ogg"
get_char('c21') '[convertstrid(1121018)]' (**arg(1, 1121018))
$ update_portrait('oc002_01 5', 'p2', [l(-3), dark, flip], 5)
play sfx2 "other_7004.ogg"
get_char('c6873') '[convertstrid(1121019)]' (**arg(2, 1121019))
hide p2
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1121020)]' (**arg(3, 1121020))
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('sc039_01 4', 'p46', [r(-13), light], 6)
get_char('c463') '[convertstrid(1121021)]' (**arg(4, 1121021))
$ update_portrait('sc039_01 4', 'p46', [r(-13), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1121489)]' (**arg(5, 1121489))
hide p46
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
get_char('c6873') '[convertstrid(1121023)]' (**arg(6, 1121023))
hide p1
$ update_portrait('sc039_01 4', 'p46', [l(-13), l_shake, light, flip], 6)
get_char('c461') '[convertstrid(1121490)]' (**arg(7, 1121490))
$ update_portrait('sc039_01 4', 'p46', [l(-13), dark, flip], 5)
get_char('c6873') '[convertstrid(1121024)]' (**arg(8, 1121024))
hide p46
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na02.ogg"
get_char('c11') '[convertstrid(1121025)]' (**arg(9, 1121025))
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 5)
get_char('c6873') '[convertstrid(1121026)]' (**arg(10, 1121026))
hide p1
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1121574)]' (**arg(11, 1121574))
return