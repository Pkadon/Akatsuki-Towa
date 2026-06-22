label avg24079:

$ play_music("ed7105.ogg")
scene placeholderbackground
$ update_narrator('c9853')
window show
with fade_in
get_char('c9853') '[convertstrid(1200301)]' (**arg(1, 1200301))
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1200302)]' (**arg(2, 1200302))
return