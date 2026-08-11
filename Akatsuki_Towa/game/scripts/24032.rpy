label avg24032(trans=fade_in):

stop music
scene placeholderbackground
$ update_narrator('c10153')
window show
with trans
get_char('c10153') '[convertstrid(1200128)]' (**arg(1, 1200128))
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1200129)]' (**arg(2, 1200129))
return "avg24032"