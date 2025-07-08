label avg19120:
stop music

play music "ed7150.ogg"
scene avg_bg_071
$ update_portrait('sc001_01 2', 'p9', [l(-11), light, flip], 6)
window show
with fade_in
c91 '[textdict[1218072]]' (what_size=(gui.text_size*0.9))
$ update_portrait('sc001_01 2', 'p9', [l(-11), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
play sfxvoice "bcv_oc002_get_02.ogg"
c13 '[textdict[1218073]]' (what_size=(gui.text_size*0.9))
hide p9
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc001_01 1', 'p9', [l(-11), light, flip], 6)
c91 '[textdict[1218074]]' (what_size=(gui.text_size*0.9))
hide p1
$ update_portrait('sc001_01 1', 'p9', [l(-11), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
play sfxvoice "bcv_oc002_get_02.ogg"
c13 '[textdict[1218075]]' (what_size=(gui.text_size*0.9))
hide p9
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc001_01 4', 'p9', [l(-11), light, flip], 6)
c91 '[textdict[1218076]]' (what_size=(gui.text_size*0.9))
hide p1
$ update_portrait('sc001_01 4', 'p9', [l(-11), dark, flip], 6)
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 5)
play sfxvoice "bcv_oc002_arts_02.ogg"
c13 '[textdict[1218077]]' (what_size=(gui.text_size*0.9))
menu:
    extend ""
    "[textdict[1218078]]":
        call avg19121
    "[textdict[1218079]]":
        call avg19122
    "[textdict[1218080]]":
        call avg19123
return