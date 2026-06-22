label avg12459:

$ play_music("ed7300.ogg")
scene avg_bg_071
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
get_char('c23') '[convertstrid(1143735)]' (**arg(1, 1143735))
$ update_portrait('oc002_01 13', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1143736)]' (**arg(2, 1143736))
$ update_portrait('oc002_01 8', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1143737)]' (**arg(3, 1143737))
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1143738)]' (**arg(4, 1143738))
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1143739)]' (**arg(5, 1143739))
$ update_portrait('oc002_01 8', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1143740)]' (**arg(6, 1143740))
hide p2
play sfx2 "other_7074.ogg"
get_char('c0') '[convertstrid(1143741)]' (**arg(7, 1143741))
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
play sfx2 "other_7073.ogg"
get_char('c23') '[convertstrid(1143742)]' (**arg(8, 1143742))
return