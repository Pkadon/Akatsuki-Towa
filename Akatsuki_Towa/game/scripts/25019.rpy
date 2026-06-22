label avg25019:

stop music
scene placeholderbackground
$ update_narrator('c20083')
window show
with fade_in
get_char('c20083') '[convertstrid(1210042)]' (**arg(1, 1210042))
get_char('c20093') '[convertstrid(1210043)]' (**arg(2, 1210043))
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c23') '[convertstrid(1210044)]' (**arg(3, 1210044))
hide p2
get_char('c20083') '[convertstrid(1210045)]' (**arg(4, 1210045))
get_char('c20093') '[convertstrid(1210046)]' (**arg(5, 1210046))
menu:
    extend ""
    '[convertstrid(1214999)]':
        call avg25020
    '[convertstrid(1215000)]':
        call avg25026
return