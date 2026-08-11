label avg14099(trans=fade_in):

$ play_music("ed7150.ogg")
scene avg_bg_023
$ update_portrait('sc049_01 5', 'p56', [mid(-8), light], 6)
$ update_narrator('c563')
window show
with trans
get_char('c563') '[convertstrid(1202040)]' (**arg(1, 1202040))
$ update_portrait('sc049_01 10', 'p56', [mid(-8), light], 6)
get_char('c563') '[convertstrid(1202041)]' (**arg(2, 1202041))
$ update_portrait('sc049_01 1', 'p56', [mid(-8), light], 6)
get_char('c563') '[convertstrid(1202042)]' (**arg(3, 1202042))
return "avg14099"