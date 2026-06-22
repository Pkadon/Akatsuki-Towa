label avg101102:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1220386)]' (**arg(1, 1220386))
hide p1
$ update_portrait('sc003_01 5', 'p11', [mid(-4), light], 6)
get_char('c113') '[convertstrid(1220387)]' (**arg(2, 1220387))
$ update_portrait('sc003_01 6', 'p11', [mid(-4), light], 6)
get_char('c113') '[convertstrid(1220388)]' (**arg(3, 1220388))
hide p11
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1220389)]' (**arg(4, 1220389))
hide p1
$ update_portrait('sc003_01 2', 'p11', [mid(-4), light], 6)
get_char('c113') '[convertstrid(1220390)]' (**arg(5, 1220390))
return