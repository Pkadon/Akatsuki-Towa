label avg24021:

stop music
scene placeholderbackground
$ update_portrait('oc003_01 5', 'p3', [mid(-6), light], 6)
$ update_narrator('c33')
window show
with fade_in
get_char('c33') '[convertstrid(1200089)]' (**arg(1, 1200089))
hide p3
get_char('c7593') '[convertstrid(1200090)]' (**arg(2, 1200090))
$ update_portrait('oc003_01 1', 'p3', [mid(-6), light], 6)
get_char('c33') '[convertstrid(1200091)]' (**arg(3, 1200091))
hide p3
get_char('c7593') '[convertstrid(1200092)]' (**arg(4, 1200092))
get_char('c7593') '[convertstrid(1200093)]' (**arg(5, 1200093))
$ update_portrait('oc003_01 1', 'p3', [mid(-6), light], 6)
get_char('c33') '[convertstrid(1200094)]' (**arg(6, 1200094))
return