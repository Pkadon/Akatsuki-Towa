label avg25188:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1210626)]' (**arg(1, 1210626))
hide p1
play sfx2 "other_7004.ogg"
get_char('c0') '[convertstrid(1210627)]' (**arg(2, 1210627))
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
play sfxvoice "bcv_oc002_arts_03.ogg"
get_char('c23') '[convertstrid(1210628)]' (**arg(3, 1210628))
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210629)]' (**arg(4, 1210629))
return