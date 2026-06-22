label avg24030:

stop music
scene placeholderbackground
$ update_narrator('c10153')
window show
with fade_in
get_char('c10153') '[convertstrid(1200123)]' (**arg(1, 1200123))
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1200124)]' (**arg(2, 1200124))
return