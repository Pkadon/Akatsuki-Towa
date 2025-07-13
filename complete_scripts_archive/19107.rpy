label avg19107:

play music "ed7150.ogg"
scene avg_bg_071
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
play sfxvoice "avg_vocal_na02.ogg"
c13 '[textdict[1218031]]' (what_size=(gui.text_size*0.9))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc001_01 1', 'p9', [l(-11), light, flip], 6)
c91 '[textdict[1218032]]' (what_size=(gui.text_size*0.9))
$ update_portrait('sc001_01 1', 'p9', [l(-11), dark, flip], 6)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na21.ogg"
c13 '[textdict[1218033]]' (what_size=(gui.text_size*0.9))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('sc001_01 1', 'p9', [l(-11), light, flip], 6)
c91 '[textdict[1218034]]' (what_size=(gui.text_size*0.9))
$ update_portrait('sc001_01 5', 'p9', [l(-11), light, flip], 6)
c91 '[textdict[1218035]]' (what_size=(gui.text_size*0.9))
$ update_portrait('sc001_01 5', 'p9', [l(-11), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na02.ogg"
c13 '[textdict[1218036]]' (what_size=(gui.text_size*0.9))
menu:
    extend ""
    "[textdict[1218037]]":
        call avg19108
    "[textdict[1218038]]":
        call avg19109
    "[textdict[1218039]]":
        call avg19110
return