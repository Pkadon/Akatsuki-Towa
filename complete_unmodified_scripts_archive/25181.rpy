label avg25181(trans=fade_in):

stop music
scene placeholderbackground
$ update_narrator('c20203')
window show
with trans
play sfx2 "other_7077.ogg"
get_char('c20203') '[convertstrid(1210586)]' (**arg(1, 1210586))
play sfx2 "other_7092.ogg"
get_char('c0') '[convertstrid(1210587)]' (**arg(2, 1210587))
$ update_portrait('oc002_01 14', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch08.ogg"
get_char('c23') '[convertstrid(1210588)]' (**arg(3, 1210588))
hide p2
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na18.ogg"
get_char('c13') '[convertstrid(1210589)]' (**arg(4, 1210589))
hide p1
play sfx2 "other_7092.ogg"
get_char('c0') '[convertstrid(1210590)]' (**arg(5, 1210590))
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 6)
play sfx2 "common_sephi2.ogg"
play sfxvoice "avg_vocal_ch09.ogg"
get_char('c23') '[convertstrid(1210591)]' (**arg(6, 1210591))
hide p2
$ update_portrait('oc001_01 6', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210592)]' (**arg(7, 1210592))
return "avg25181"