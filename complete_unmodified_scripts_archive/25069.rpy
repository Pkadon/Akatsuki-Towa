label avg25069:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c23') '[convertstrid(1210220)]' (**arg(1, 1210220))
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210221)]' (**arg(2, 1210221))
menu:
    extend ""
    '[convertstrid(1214997)]':
        call avg25070
    '[convertstrid(1215000)]':
        call avg25026
return