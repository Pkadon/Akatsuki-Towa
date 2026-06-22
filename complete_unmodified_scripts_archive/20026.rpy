label avg20026:

$ play_music("ed7150.ogg")
scene placeholderbackground
$ update_narrator('c5413')
window show
with fade_in
get_char('c5413') '[convertstrid(1001662)]' (**arg(1, 1001662))
get_char('c5413') '[convertstrid(1001663)]' (**arg(2, 1001663))
get_char('c5413') '[convertstrid(1001664)]' (**arg(3, 1001664))
get_char('c5423') '[convertstrid(1001665)]' (**arg(4, 1001665))
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c23') '[convertstrid(1001666)]' (**arg(5, 1001666))
hide p2
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na20.ogg"
get_char('c13') '[convertstrid(1001667)]' (**arg(6, 1001667))
return