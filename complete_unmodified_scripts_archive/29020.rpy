label avg29020(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1007260)]' (**arg(1, 1007260))
hide p1
$ update_portrait('oc002_01 17', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch20.ogg"
get_char('c23') '[convertstrid(1007261)]' (**arg(2, 1007261))
return "avg29020"