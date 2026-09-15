label avg24070(trans=fade_in):

$ play_music("ed7105.ogg")
scene placeholderbackground
$ update_narrator('c7553')
window show
with trans
get_char('c7553') '[convertstrid(1200276)]' (**arg(1, 1200276))
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1200277)]' (**arg(2, 1200277))
$ update_portrait('oc002_01 5', 'p2', [l(-3), dark, flip], 5)
get_char('c7553') '[convertstrid(1200278)]' (**arg(3, 1200278))
return "avg24070"