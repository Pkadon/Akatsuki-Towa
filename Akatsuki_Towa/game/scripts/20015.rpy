label avg20015:

$ play_music("ED6518.ogg")
scene avg_bg_008
$ update_narrator('c5171')
window show
with fade_in
play sfx2 "common_select.ogg"
get_char('c5171') '[convertstrid(1000948)]' (**arg(1, 1000948))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000949)]' (**arg(2, 1000949))
return