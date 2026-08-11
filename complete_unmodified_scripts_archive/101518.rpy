label avg101518(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1221300)]' (**arg(1, 1221300))
hide p1
$ update_portrait('sc007_01 2', 'p15', [mid(-17), light], 6)
get_char('c153') '[convertstrid(1221301)]' (**arg(2, 1221301))
hide p15
$ update_portrait('oc001_01 17', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1221302)]' (**arg(3, 1221302))
hide p1
$ update_portrait('sc007_01 5', 'p15', [mid(-17), light], 6)
get_char('c153') '[convertstrid(1221303)]' (**arg(4, 1221303))
hide p15
$ update_portrait('oc001_01 13', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1221304)]' (**arg(5, 1221304))
hide p1
$ update_portrait('sc007_01 3', 'p15', [mid(-17), light], 6)
get_char('c153') '[convertstrid(1221305)]' (**arg(6, 1221305))
return "avg101518"