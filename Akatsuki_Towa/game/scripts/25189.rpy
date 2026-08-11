label avg25189(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('uc003_01 1', 'p2018', [mid(-26), light], 6)
$ update_narrator('c20183')
window show
with trans
get_char('c20183') '[convertstrid(1210630)]' (**arg(1, 1210630))
hide p2018
$ update_portrait('oc002_01 19', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch25.ogg"
get_char('c23') '[convertstrid(1210631)]' (**arg(2, 1210631))
hide p2
$ update_portrait('uc003_01 3', 'p2018', [mid(-26), light], 6)
get_char('c20183') '[convertstrid(1210632)]' (**arg(3, 1210632))
hide p2018
play sfx2 "other_7086.ogg"
get_char('c0') '[convertstrid(1210633)]' (**arg(4, 1210633))
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
play sfxvoice "bcv_oc002_c02_01.ogg"
get_char('c23') '[convertstrid(1210634)]' (**arg(5, 1210634))
return "avg25189"