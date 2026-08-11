label avg29119(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc001_01 2', 'p9', [mid(-11), light], 6)
$ update_narrator('c93')
window show
with trans
get_char('c93') '[convertstrid(1218066)]' (**arg(1, 1218066))
hide p9
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
play sfxvoice "bcv_oc002_win_02.ogg"
get_char('c13') '[convertstrid(1218067)]' (**arg(2, 1218067))
hide p1
$ update_portrait('sc001_01 5', 'p9', [mid(-11), light], 6)
get_char('c93') '[convertstrid(1218068)]' (**arg(3, 1218068))
$ update_portrait('sc001_01 6', 'p9', [mid(-11), light], 6)
get_char('c93') '[convertstrid(1218069)]' (**arg(4, 1218069))
hide p9
$ update_portrait('oc001_01 6', 'p1', [mid(-2), light], 6)
play sfxvoice "bcv_oc002_c01_01.ogg"
get_char('c13') '[convertstrid(1218070)]' (**arg(5, 1218070))
return "avg29119"