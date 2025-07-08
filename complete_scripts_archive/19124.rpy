label avg19124:
stop music

play music "ed7150.ogg"
scene avg_bg_071
$ update_portrait('sc001_01 2', 'p9', [l(-11), light, flip], 6)
window show
with fade_in
c91 '[textdict[1218085]]' (what_size=(gui.text_size*0.9))
hide p9
$ update_portrait('sc001_01 2', 'p9', [l(-11), dark, flip], 6)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
play sfxvoice "bcv_oc002_win_02.ogg"
c13 '[textdict[1218086]]' (what_size=(gui.text_size*0.9))
hide p9
hide p1
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc001_01 1', 'p9', [l(-11), light, flip], 6)
c91 '[textdict[1218087]]' (what_size=(gui.text_size*0.9))
hide p9
hide p1
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc001_01 5', 'p9', [l(-11), light, flip], 6)
c91 '[textdict[1218088]]' (what_size=(gui.text_size*0.9))
hide p1
hide p9
$ update_portrait('sc001_01 5', 'p9', [l(-11), dark, flip], 6)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
play sfxvoice "bcv_oc002_win_02.ogg"
c13 '[textdict[1218089]]' (what_size=(gui.text_size*0.9))
menu:
    extend ""
    "[textdict[1218090]]":
        call avg19125
    "[textdict[1218091]]":
        call avg19126
    "[textdict[1218092]]":
        call avg19127
return