label avg24041(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_055
$ update_portrait('oc002_01 1', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1200164)]' (**arg(1, 1200164))
$ update_portrait('oc002_01 1', 'p2', [r(-3), dark], 5)
get_char('c10921') '[convertstrid(1200165)]' (**arg(2, 1200165))
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1200166)]' (**arg(3, 1200166))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
get_char('c10921') '[convertstrid(1200167)]' (**arg(4, 1200167))
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1200168)]' (**arg(5, 1200168))
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
get_char('c10921') '[convertstrid(1200169)]' (**arg(6, 1200169))
return "avg24041"