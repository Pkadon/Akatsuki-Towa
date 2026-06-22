label avg24083:

$ play_music("ed7105.ogg")
scene avg_bg_064
$ update_narrator('c7421')
window show
with fade_in
get_char('c7421') '[convertstrid(1200308)]' (**arg(1, 1200308))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1200309)]' (**arg(2, 1200309))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
get_char('c7421') '[convertstrid(1200310)]' (**arg(3, 1200310))
$ update_portrait('oc001_01 5', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1200311)]' (**arg(4, 1200311))
return