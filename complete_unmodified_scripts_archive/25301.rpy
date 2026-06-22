label avg25301:

stop music
scene placeholderbackground
$ update_narrator('c20263')
window show
with fade_in
play sfx2 "other_7088.ogg"
get_char('c20263') '[convertstrid(1211161)]' (**arg(1, 1211161))
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1211162)]' (**arg(2, 1211162))
hide p2
get_char('c20263') '[convertstrid(1211163)]' (**arg(3, 1211163))
return