label avg24086(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_038
$ update_portrait('st044_01 2', 'p243', [r(10), light], 6)
$ update_narrator('c2433')
window show
with trans
get_char('c2433') '[convertstrid(1200317)]' (**arg(1, 1200317))
$ update_portrait('st044_01 2', 'p243', [r(10), dark], 5)
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1200318)]' (**arg(2, 1200318))
return "avg24086"