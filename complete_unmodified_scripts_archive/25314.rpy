label avg25314(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 16', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "other_7027.ogg"
play sfxvoice "avg_vocal_na03.ogg"
get_char('c13') '[convertstrid(1211206)]' (**arg(1, 1211206))
hide p1
get_char('c20153') '[convertstrid(1211207)]' (**arg(2, 1211207))
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1211208)]' (**arg(3, 1211208))
hide p1
$ update_portrait('oc002_01 1', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1211209)]' (**arg(4, 1211209))
return "avg25314"