label avg20310(trans=fade_in):

$ play_music("ed7105.ogg")
scene placeholderbackground
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1130291)]' (**arg(1, 1130291))
hide p1
get_char('c10063') '[convertstrid(1130292)]' (**arg(2, 1130292))
$ update_portrait('oc004_01 8', 'p4', [mid(-5), light], 6)
get_char('c43') '[convertstrid(1130293)]' (**arg(3, 1130293))
hide p4
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1130294)]' (**arg(4, 1130294))
return "avg20310"