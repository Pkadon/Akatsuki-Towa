label avg25254:

stop music
scene placeholderbackground
$ update_narrator('c20083')
window show
with fade_in
get_char('c20083') '[convertstrid(1210940)]' (**arg(1, 1210940))
get_char('c20103') '[convertstrid(1210941)]' (**arg(2, 1210941))
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c23') '[convertstrid(1210942)]' (**arg(3, 1210942))
hide p2
get_char('c20083') '[convertstrid(1210943)]' (**arg(4, 1210943))
get_char('c20103') '[convertstrid(1210944)]' (**arg(5, 1210944))
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
play sfxvoice "bcv_oc002_c02_01.ogg"
get_char('c23') '[convertstrid(1210945)]' (**arg(6, 1210945))
return