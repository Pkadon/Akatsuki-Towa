label avg25054(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('uc001_02 2', 'p2006', [mid(6), light], 6)
$ update_narrator('c20063')
window show
with trans
get_char('c20063') '[convertstrid(1210149)]' (**arg(1, 1210149))
hide p2006
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch10.ogg"
get_char('c23') '[convertstrid(1210150)]' (**arg(2, 1210150))
hide p2
$ update_portrait('uc001_02 2', 'p2006', [mid(6), light], 6)
get_char('c20063') '[convertstrid(1210151)]' (**arg(3, 1210151))
$ update_portrait('uc001_02 1', 'p2006', [mid(6), light], 6)
get_char('c20063') '[convertstrid(1210152)]' (**arg(4, 1210152))
hide p2006
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch05.ogg"
get_char('c23') '[convertstrid(1210153)]' (**arg(5, 1210153))
hide p2
$ update_portrait('uc001_02 1', 'p2006', [mid(6), light], 6)
get_char('c20063') '[convertstrid(1210154)]' (**arg(6, 1210154))
$ update_portrait('uc001_02 1', 'p2006', [mid(6), light], 6)
get_char('c20063') '[convertstrid(1210155)]' (**arg(7, 1210155))
return "avg25054"