label avg22315(trans=fade_in):

$ play_music("ed7526.ogg")
scene placeholderbackground
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1133287)]' (**arg(1, 1133287))
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1133288)]' (**arg(2, 1133288))
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1133289)]' (**arg(3, 1133289))
hide p1
$ update_portrait('oc004_01 3', 'p4', [mid(-5), light], 6)
get_char('c43') '[convertstrid(1133290)]' (**arg(4, 1133290))
hide p4
$ update_portrait('oc003_01 7', 'p3', [mid(-6), light], 6)
get_char('c33') '[convertstrid(1133291)]' (**arg(5, 1133291))
$ update_portrait('oc003_01 4', 'p3', [mid(-6), light], 6)
get_char('c33') '[convertstrid(1133292)]' (**arg(6, 1133292))
hide p3
$ update_portrait('oc004_01 4', 'p4', [mid(-5), light], 6)
get_char('c43') '[convertstrid(1133293)]' (**arg(7, 1133293))
hide p4
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1133294)]' (**arg(8, 1133294))
hide p1
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1133295)]' (**arg(9, 1133295))
hide p2
$ update_portrait('oc004_01 17', 'p4', [mid(-5), light], 6)
get_char('c43') '[convertstrid(1133296)]' (**arg(10, 1133296))
$ update_portrait('oc004_01 20', 'p4', [mid(-5), light], 6)
get_char('c43') '[convertstrid(1133297)]' (**arg(11, 1133297))
hide p4
$ update_portrait('oc003_01 4', 'p3', [mid(-6), light], 6)
get_char('c33') '[convertstrid(1133298)]' (**arg(12, 1133298))
return "avg22315"