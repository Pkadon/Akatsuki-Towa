label avg1(trans=fade_in):

$ play_music("ed7105.ogg")
scene placeholderbackground
$ update_narrator('c7223')
window show
with trans
get_char('c7223') '[convertstrid(1120002)]' (**arg(1, 1120002))
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1120003)]' (**arg(2, 1120003))
hide p2
$ update_portrait('oc001_01 17', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1120004)]' (**arg(3, 1120004))
hide p1
get_char('c7223') '[convertstrid(1120005)]' (**arg(4, 1120005))
get_char('c7223') '[convertstrid(1120006)]' (**arg(5, 1120006))
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1120007)]' (**arg(6, 1120007))
return "avg1"