label avg25162:

stop music
scene placeholderbackground
$ update_narrator('c0')
window show
with fade_in
play sfx2 "common_tag_2.ogg"
get_char('c0') '[convertstrid(1210530)]' (**arg(1, 1210530))
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c23') '[convertstrid(1210531)]' (**arg(2, 1210531))
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
play sfx2 "elc_5004.ogg"
get_char('c13') '[convertstrid(1210532)]' (**arg(3, 1210532))
return