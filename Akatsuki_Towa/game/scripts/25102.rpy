label avg25102(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c23') '[convertstrid(1210286)]' (**arg(1, 1210286))
hide p2
play sfx2 "other_7051.ogg"
get_char('c20073') '[convertstrid(1210287)]' (**arg(2, 1210287))
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210288)]' (**arg(3, 1210288))
hide p1
get_char('c20073') '[convertstrid(1210289)]' (**arg(4, 1210289))
menu:
    extend ""
    '[convertstrid(1214995)]':
        call avg25103
    '[convertstrid(1215000)]':
        call avg25000
return _return