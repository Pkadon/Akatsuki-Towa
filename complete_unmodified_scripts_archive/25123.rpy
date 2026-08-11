label avg25123(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1210367)]' (**arg(1, 1210367))
hide p1
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c23') '[convertstrid(1210368)]' (**arg(2, 1210368))
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210369)]' (**arg(3, 1210369))
menu:
    extend ""
    '[convertstrid(1214997)]':
        call avg25124
    '[convertstrid(1214996)]':
        call avg25026
return _return