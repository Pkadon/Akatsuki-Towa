label avg24006(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1200019)]' (**arg(1, 1200019))
hide p1
get_char('c7433') '[convertstrid(1200020)]' (**arg(2, 1200020))
get_char('c7433') '[convertstrid(1200021)]' (**arg(3, 1200021))
$ update_portrait('oc001_01 11', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1200022)]' (**arg(4, 1200022))
return "avg24006"