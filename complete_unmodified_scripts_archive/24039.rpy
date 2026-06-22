label avg24039:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
get_char('c23') '[convertstrid(1200157)]' (**arg(1, 1200157))
hide p2
get_char('c10923') '[convertstrid(1200158)]' (**arg(2, 1200158))
get_char('c10923') '[convertstrid(1200159)]' (**arg(3, 1200159))
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1200160)]' (**arg(4, 1200160))
return