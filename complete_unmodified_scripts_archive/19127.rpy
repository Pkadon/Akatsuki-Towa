label avg19127:

$ play_music("ed7150.ogg")
scene avg_bg_071
$ update_portrait('sc001_01 6', 'p9', [l(-11), light, flip], 6)
$ update_narrator('c91')
window show
with fade_in
get_char('c91') '[convertstrid(1218095)]' (**arg(1, 1218095, size=(0.9)))
return