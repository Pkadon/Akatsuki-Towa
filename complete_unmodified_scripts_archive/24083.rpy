label avg24083:

$ play_music("ed7105.ogg")
scene placeholderbackground
$ update_narrator('c7423')
window show
with fade_in
get_char('c7423') '[convertstrid(1200308)]' (**arg(1, 1200308))
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1200309)]' (**arg(2, 1200309))
hide p1
get_char('c7423') '[convertstrid(1200310)]' (**arg(3, 1200310))
$ update_portrait('oc001_01 5', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1200311)]' (**arg(4, 1200311))
return