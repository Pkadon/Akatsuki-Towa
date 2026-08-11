label avg24063(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1200255)]' (**arg(1, 1200255))
hide p1
get_char('c7573') '[convertstrid(1200256)]' (**arg(2, 1200256))
$ update_portrait('oc001_01 5', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1200257)]' (**arg(3, 1200257))
return "avg24063"