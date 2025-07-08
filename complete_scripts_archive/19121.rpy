label avg19121:
stop music

play music "ed7150.ogg"
scene avg_bg_071
$ update_portrait('sc001_01 2', 'p9', [l(-11), light, flip], 6)
window show
with fade_in
c91 '[textdict[1218081]]' (what_size=(gui.text_size*0.9))
return