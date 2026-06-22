label avg12540:

$ play_music("ED6105.ogg")
scene avg_bg_010
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(1152912)]' (**arg(1, 1152912))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1152913)]' (**arg(2, 1152913))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1152914)]' (**arg(3, 1152914))
hide p1
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1152915)]' (**arg(4, 1152915))
$ update_portrait('oc002_01 8', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1152916)]' (**arg(5, 1152916))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1152917)]' (**arg(6, 1152917))
return