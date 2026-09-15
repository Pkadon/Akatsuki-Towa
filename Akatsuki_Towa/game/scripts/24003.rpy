label avg24003(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_038
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with trans
get_char('c11') '[convertstrid(1200011)]' (**arg(1, 1200011))
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('st044_01 1', 'p243', [r(10), light], 6)
get_char('c2433') '[convertstrid(1200012)]' (**arg(2, 1200012))
$ update_portrait('st044_01 1', 'p243', [r(10), dark], 5)
$ update_portrait('oc001_01 11', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1200013)]' (**arg(3, 1200013))
return "avg24003"