label avg24080:

$ play_music("ed7105.ogg")
scene placeholderbackground
$ update_portrait('oc003_01 5', 'p3', [mid(-6), light], 6)
$ update_narrator('c33')
window show
with fade_in
get_char('c33') '[convertstrid(1200290)]' (**arg(1, 1200290))
hide p3
get_char('c7593') '[convertstrid(1200291)]' (**arg(2, 1200291))
$ update_portrait('oc003_01 1', 'p3', [mid(-6), light], 6)
get_char('c33') '[convertstrid(1200292)]' (**arg(3, 1200292))
hide p3
get_char('c7593') '[convertstrid(1200293)]' (**arg(4, 1200293))
$ update_portrait('oc003_01 1', 'p3', [mid(-6), light], 6)
get_char('c33') '[convertstrid(1200294)]' (**arg(5, 1200294))
return