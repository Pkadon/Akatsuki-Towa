label avg24064(trans=fade_in):

stop music
scene placeholderbackground
$ update_narrator('c7573')
window show
with trans
get_char('c7573') '[convertstrid(1200258)]' (**arg(1, 1200258))
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1200259)]' (**arg(2, 1200259))
hide p2
get_char('c7573') '[convertstrid(1200260)]' (**arg(3, 1200260))
return "avg24064"