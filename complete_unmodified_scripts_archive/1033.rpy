label avg1033:

$ play_music("ed7201.ogg")
scene avg_bg_010
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
window show
with fade_in
get_char('c21') '[convertstrid(2100571)]' (**arg(1, 2100571))
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2100572)]' (**arg(2, 2100572))
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc052_01 5', 'p59', [l_entrance(-25), light, flip], 6)
get_char('c591') '[convertstrid(2100573)]' (**arg(3, 2100573))
$ update_portrait('sc052_01 1', 'p59', [l(-25), light, flip], 6)
get_char('c591') '[convertstrid(2100574)]' (**arg(4, 2100574))
$ update_portrait('sc052_01 1', 'p59', [l(-25), light, flip], 6)
get_char('c591') '[convertstrid(2100575)]' (**arg(5, 2100575))
return