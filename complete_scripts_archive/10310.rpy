label avg10310:

play music "ed7124.ogg"
scene avg_bg_059
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "common_cancel.ogg"
c13 '[textdict[1130291]]'
hide p1
c10063 '[textdict[1130292]]'
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li18.ogg"
c41 '[textdict[1130293]]'
$ update_portrait('oc004_01 8', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 5)
c13 '[textdict[1130294]]'
return