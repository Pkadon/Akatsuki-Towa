label avg25258(trans=fade_in):

stop music
scene placeholderbackground
$ update_narrator('c20093')
window show
with trans
get_char('c20093') '[convertstrid(1210958)]' (**arg(1, 1210958))
get_char('c20083') '[convertstrid(1210959)]' (**arg(2, 1210959))
get_char('c20103') '[convertstrid(1210960)]' (**arg(3, 1210960))
get_char('c20093') '[convertstrid(1210961)]' (**arg(4, 1210961))
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1210962)]' (**arg(5, 1210962))
hide p1
get_char('c20093') '[convertstrid(1210963)]' (**arg(6, 1210963))
$ update_portrait('oc002_01 13', 'p2', [mid(-3), light], 6)
play sfx2 "common_35rewardholy.ogg"
get_char('c23') '[convertstrid(1210964)]' (**arg(7, 1210964))
return "avg25258"