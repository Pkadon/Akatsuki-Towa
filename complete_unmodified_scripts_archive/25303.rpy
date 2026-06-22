label avg25303:

stop music
scene placeholderbackground
$ update_narrator('c20283')
window show
with fade_in
get_char('c20283') '[convertstrid(1211167)]' (**arg(1, 1211167))
$ update_portrait('oc002_01 10', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch17.ogg"
get_char('c23') '[convertstrid(1211168)]' (**arg(2, 1211168))
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
play sfx2 "other_7088.ogg"
play sfxvoice "avg_vocal_na06.ogg"
get_char('c13') '[convertstrid(1211169)]' (**arg(3, 1211169))
return