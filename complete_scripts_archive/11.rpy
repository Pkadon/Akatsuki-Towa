label avg11:

stop music
scene placeholderbackground
$ update_portrait('sc007_01 5', 'p0', [l(-17), light, flip], 6)
window show
with fade_in
c0 '[textdict[12]]' (what_size=(gui.text_size*2.0))
hide p0
$ update_portrait('sc007_01 6', 'p0', [l(-17), light, flip], 6)
c0 '[textdict[12]]' (what_size=(gui.text_size*2.0))
hide p0
$ update_portrait('sc005_01 5', 'p0', [l(-17), light], 6)
c0 '[textdict[12]]' (what_size=(gui.text_size*2.0))
hide p0
$ update_portrait('sc005_01 6', 'p0', [l(-17), light], 6)
c0 '[textdict[12]]' (what_size=(gui.text_size*2.0))
return