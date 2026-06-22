label avg12663:

$ play_music("ED6105.ogg")
scene avg_bg_072
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(1166542)]' (**arg(1, 1166542))
get_char('c0') '[convertstrid(1166543)]' (**arg(2, 1166543))
get_char('c0') '[convertstrid(1166544)]' (**arg(3, 1166544))
$ update_portrait('st061_01 5', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1166545)]' (**arg(4, 1166545))
return