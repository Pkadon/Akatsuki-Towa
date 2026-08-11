label avg24008(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1200025)]' (**arg(1, 1200025))
hide p2
get_char('c7433') '[convertstrid(1200026)]' (**arg(2, 1200026))
get_char('c7433') '[convertstrid(1200027)]' (**arg(3, 1200027))
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1200028)]' (**arg(4, 1200028))
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1200029)]' (**arg(5, 1200029))
return "avg24008"