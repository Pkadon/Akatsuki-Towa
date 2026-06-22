label avg10120:

$ play_music("ed7561.ogg")
scene avg_bg_012
$ update_narrator('c0')
window show
with fade_in
play sfx2 "other_7022.ogg"
get_char('c0') '[convertstrid(1123036)]' (**arg(1, 1123036))
play sfx2 "other_7022.ogg"
get_char('c7143') '[convertstrid(1006641)]' (**arg(2, 1006641))
$ update_portrait('st051_01 3', 'p258', [l(-9), light, flip], 6)
play sfx2 "other_7023.ogg"
get_char('c2581') '[convertstrid(1006642)]' (**arg(3, 1006642))
scene avg_bg_033
$ update_narrator('c0')
with fade
play sfx2 "other_7022.ogg"
get_char('c0') '[convertstrid(1123037)]' (**arg(4, 1123037))
play sfx2 "other_7022.ogg"
get_char('c6753') '[convertstrid(1006643)]' (**arg(5, 1006643))
play sfx2 "other_7023.ogg"
get_char('c7131') '[convertstrid(1006644)]' (**arg(6, 1006644))
$ update_portrait('st034_01 2', 'p233', [r(12), light], 6)
get_char('c2333') '[convertstrid(1006645)]' (**arg(7, 1006645))
$ update_portrait('st034_01 2', 'p233', [r(12), dark], 5)
get_char('c6771') '[convertstrid(1006646)]' (**arg(8, 1006646))
hide p233
$ update_portrait('st027_01 5', 'p226', [r(5), light], 6)
play sfx2 "other_7022.ogg"
get_char('c2263') '[convertstrid(1006647)]' (**arg(9, 1006647))
return