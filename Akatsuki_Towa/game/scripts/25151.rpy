label avg25151:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "common_select.ogg"
play sfxvoice "avg_vocal_na10.ogg"
get_char('c13') '[convertstrid(1210479)]' (**arg(1, 1210479))
hide p1
$ update_portrait('uc001_02 1', 'p2014', [mid(6), light], 6)
get_char('c20143') '[convertstrid(1210480)]' (**arg(2, 1210480))
return