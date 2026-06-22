label avg101101:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1220379)]' (**arg(1, 1220379))
hide p1
$ update_portrait('sc003_01 6', 'p11', [mid(-4), light], 6)
get_char('c113') '[convertstrid(1220380)]' (**arg(2, 1220380))
$ update_portrait('sc003_01 1', 'p11', [mid(-4), light], 6)
get_char('c113') '[convertstrid(1220381)]' (**arg(3, 1220381))
$ update_portrait('sc003_01 4', 'p11', [mid(-4), light], 6)
get_char('c113') '[convertstrid(1220382)]' (**arg(4, 1220382))
$ update_portrait('sc003_01 2', 'p11', [mid(-4), light], 6)
get_char('c113') '[convertstrid(1220383)]' (**arg(5, 1220383))
hide p11
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1220384)]' (**arg(6, 1220384))
return