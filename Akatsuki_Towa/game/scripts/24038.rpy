label avg24038(trans=fade_in):

$ play_music("ed7150.ogg")
scene avg_bg_014
$ update_narrator('c23')
window show
with trans
$ update_portrait('oc002_01 1', 'p2', [r_entrance(-3), light], 6)
get_char('c23') '[convertstrid(1200153)]' (**arg(1, 1200153))
$ update_portrait('oc002_01 1', 'p2', [r(-3), dark], 5)
get_char('c7621') '[convertstrid(1200154)]' (**arg(2, 1200154))
get_char('c7621') '[convertstrid(1200155)]' (**arg(3, 1200155))
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1200156)]' (**arg(4, 1200156))
return "avg24038"