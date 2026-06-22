label avg20011:

$ play_music("ed7150.ogg")
scene placeholderbackground
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(1000499)]' (**arg(1, 1000499))
get_char('c0') '[convertstrid(1000500)]' (**arg(2, 1000500))
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1000501)]' (**arg(3, 1000501))
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1000502)]' (**arg(4, 1000502))
return