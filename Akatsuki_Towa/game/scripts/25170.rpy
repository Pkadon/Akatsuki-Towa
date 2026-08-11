label avg25170(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 19', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfxvoice "avg_vocal_na07.ogg"
get_char('c13') '[convertstrid(1210550)]' (**arg(1, 1210550))
return "avg25170"