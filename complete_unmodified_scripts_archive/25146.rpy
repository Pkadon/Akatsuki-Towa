label avg25146(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('uc001_02 3', 'p2014', [mid(6), light], 6)
$ update_narrator('c20143')
window show
with trans
get_char('c20143') '[convertstrid(1210463)]' (**arg(1, 1210463))
hide p2014
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210464)]' (**arg(2, 1210464))
hide p1
$ update_portrait('uc001_02 3', 'p2014', [mid(6), light], 6)
get_char('c20143') '[convertstrid(1210465)]' (**arg(3, 1210465))
hide p2014
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch10.ogg"
get_char('c23') '[convertstrid(1210466)]' (**arg(4, 1210466))
hide p2
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
play sfxvoice "bcv_oc001_com_01.ogg"
get_char('c13') '[convertstrid(1210467)]' (**arg(5, 1210467))
return "avg25146"