label avg24039(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_055
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1200157)]' (**arg(1, 1200157))
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
get_char('c10921') '[convertstrid(1200158)]' (**arg(2, 1200158))
get_char('c10921') '[convertstrid(1200159)]' (**arg(3, 1200159))
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1200160)]' (**arg(4, 1200160))
return "avg24039"