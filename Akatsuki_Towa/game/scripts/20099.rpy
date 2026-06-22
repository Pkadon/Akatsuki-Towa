label avg20099:

$ play_music("ed7104.ogg")
scene avg_bg_037
$ update_narrator('c6831')
window show
with fade_in
play sfx2 "other_7064.ogg"
get_char('c6831') '[convertstrid(1004837)]' (**arg(1, 1004837))
get_char('c6843') '[convertstrid(1004838)]' (**arg(2, 1004838))
get_char('c6831') '[convertstrid(1004839)]' (**arg(3, 1004839))
get_char('c6843') '[convertstrid(1004840)]' (**arg(4, 1004840))
get_char('c6831') '[convertstrid(1004841)]' (**arg(5, 1004841))
get_char('c6831') '[convertstrid(1004842)]' (**arg(6, 1004842))
get_char('c6853') '[convertstrid(1004843)]' (**arg(7, 1004843))
get_char('c6861') '[convertstrid(1004844)]' (**arg(8, 1004844))
get_char('c6853') '[convertstrid(1004845)]' (**arg(9, 1004845))
get_char('c6861') '[convertstrid(1004846)]' (**arg(10, 1004846))
get_char('c6853') '[convertstrid(1004847)]' (**arg(11, 1004847))
$ update_portrait('oc001_01 1', 'p1', [l_entrance(-2), light, flip], 6)
play sfxvoice "avg_vocal_na15.ogg"
get_char('c11') '[convertstrid(1004848)]' (**arg(12, 1004848))
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('sc039_01 1', 'p46', [r(-13), light], 6)
get_char('c463') '[convertstrid(1004849)]' (**arg(13, 1004849))
return