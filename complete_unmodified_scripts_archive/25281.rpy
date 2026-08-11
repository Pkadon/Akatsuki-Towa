label avg25281(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "common_tag_2.ogg"
get_char('c13') '[convertstrid(1211064)]' (**arg(1, 1211064))
hide p1
$ update_portrait('oc002_01 10', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch20.ogg"
get_char('c23') '[convertstrid(1211065)]' (**arg(2, 1211065))
hide p2
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1211066)]' (**arg(3, 1211066))
hide p1
$ update_portrait('oc002_01 21', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1211067)]' (**arg(4, 1211067))
return "avg25281"