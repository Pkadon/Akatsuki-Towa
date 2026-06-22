label avg24015:

$ play_music("ed7105.ogg")
scene avg_bg_064
$ update_narrator('c7421')
window show
with fade_in
get_char('c7421') '[convertstrid(1200064)]' (**arg(1, 1200064))
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1200065)]' (**arg(2, 1200065))
return