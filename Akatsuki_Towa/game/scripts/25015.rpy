label avg25015:

stop music
scene placeholderbackground
$ update_portrait('uc001_01 1', 'p587', [mid(-2), light], 6)
$ update_narrator('c5873')
window show
with fade_in
get_char('c5873') '[convertstrid(1210030)]' (**arg(1, 1210030))
hide p587
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210031)]' (**arg(2, 1210031))
hide p1
$ update_portrait('uc001_01 1', 'p587', [mid(-2), light], 6)
play sfx2 "common_sephi2.ogg"
get_char('c5873') '[convertstrid(1210032)]' (**arg(3, 1210032))
return