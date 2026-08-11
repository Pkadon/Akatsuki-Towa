label avg25061(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('uc001_01 2', 'p2004', [mid(-2), light], 6)
$ update_narrator('c20043')
window show
with trans
get_char('c20043') '[convertstrid(1210177)]' (**arg(1, 1210177))
hide p2004
$ update_portrait('uc001_02 1', 'p2005', [mid(6), light], 6)
get_char('c20053') '[convertstrid(1210178)]' (**arg(2, 1210178))
hide p2005
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
play sfx2 "other_7004.ogg"
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c23') '[convertstrid(1210179)]' (**arg(3, 1210179))
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch07.ogg"
get_char('c23') '[convertstrid(1210180)]' (**arg(4, 1210180))
menu:
    extend ""
    '[convertstrid(1214997)]':
        call avg25062
    '[convertstrid(1215000)]':
        call avg25026
return _return