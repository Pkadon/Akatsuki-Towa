label avg19122:

$ play_music("ed7150.ogg")
scene avg_bg_071
$ update_portrait('sc001_01 1', 'p9', [l(-11), light, flip], 6)
$ update_narrator('c91')
window show
with fade_in
c91 '[convertstrid(1218082)]' (what_size=(gui.text_size*0.9))
return