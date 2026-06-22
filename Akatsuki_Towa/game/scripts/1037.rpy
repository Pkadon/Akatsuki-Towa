label avg1037:

$ play_music("ed7201.ogg")
scene avg_bg_010
$ update_portrait('sc050_01 1', 'p57', [l(-19), light, flip], 6)
$ update_narrator('c571')
window show
with fade_in
get_char('c571') '[convertstrid(2100603)]' (**arg(1, 2100603))
$ update_portrait('sc050_01 1', 'p57', [l(-19), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(2100604)]' (**arg(2, 2100604))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('sc050_01 1', 'p57', [l(-19), light, flip], 6)
get_char('c571') '[convertstrid(2100605)]' (**arg(3, 2100605))
$ update_portrait('sc050_01 1', 'p57', [l(-19), dark, flip], 5)
$ update_portrait('oc002_01 14', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(2100606)]' (**arg(4, 2100606))
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(2100607)]' (**arg(5, 2100607))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2100608)]' (**arg(6, 2100608))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2100609)]' (**arg(7, 2100609))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc050_01 5', 'p57', [l(-19), light, flip], 6)
get_char('c571') '[convertstrid(2100610)]' (**arg(8, 2100610))
hide p1
$ update_portrait('sc050_01 5', 'p57', [l(-19), dark, flip], 5)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(2100611)]' (**arg(9, 2100611))
return