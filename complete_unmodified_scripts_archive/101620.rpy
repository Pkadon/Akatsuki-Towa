label avg101620(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc008_01 1', 'p16', [mid(-18), light], 6)
$ update_narrator('c163')
window show
with trans
get_char('c163') '[convertstrid(1221580)]' (**arg(1, 1221580))
hide p16
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1221581)]' (**arg(2, 1221581))
hide p1
$ update_portrait('sc008_01 5', 'p16', [mid(-18), light], 6)
get_char('c163') '[convertstrid(1221582)]' (**arg(3, 1221582))
hide p16
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1221583)]' (**arg(4, 1221583))
hide p1
$ update_portrait('sc008_01 1', 'p16', [mid(-18), light], 6)
get_char('c163') '[convertstrid(1221584)]' (**arg(5, 1221584))
return "avg101620"