label avg24040:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
get_char('c23') '[convertstrid(1200161)]' (**arg(1, 1200161))
hide p2
get_char('c10923') '[convertstrid(1200162)]' (**arg(2, 1200162))
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1200163)]' (**arg(3, 1200163))
return