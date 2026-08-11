label avg25097(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "common_select.ogg"
get_char('c13') '[convertstrid(1210271)]' (**arg(1, 1210271))
hide p1
$ update_portrait('uc001_01 1', 'p587', [mid(-2), light], 6)
get_char('c5873') '[convertstrid(1210272)]' (**arg(2, 1210272))
return "avg25097"