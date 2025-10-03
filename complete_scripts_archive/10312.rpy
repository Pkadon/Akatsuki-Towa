label avg10312:

$ play_music("ed7105.ogg")
scene avg_bg_022
$ update_portrait('st053_01 1', 'p1007', [r(-12), light], 6)
$ update_narrator('c10073')
window show
with fade_in
c10073 '[convertstrid(1130302)]'
$ update_portrait('st053_01 1', 'p1007', [r(-12), dark], 5)
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1130303)]'
hide p1007
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1130304)]'
hide p1
$ update_portrait('oc002_01 5', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1130305)]'
hide p2
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('st053_01 2', 'p1007', [r(-12), light], 6)
c10073 '[convertstrid(1130306)]'
hide p3
$ update_portrait('st053_01 2', 'p1007', [r(-12), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1130307)]'
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('st053_01 4', 'p1007', [r(-12), light], 6)
c10073 '[convertstrid(1130308)]'
$ update_portrait('st053_01 1', 'p1007', [r(-12), light], 6)
c10073 '[convertstrid(1130309)]'
$ update_portrait('st053_01 1', 'p1007', [r(-12), light], 6)
c10073 '[convertstrid(1130310)]'
hide p4
$ update_portrait('st053_01 1', 'p1007', [r(-12), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1130311)]'
hide p1007
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 5', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro05.ogg"
c33 '[convertstrid(1130312)]'
hide p1
$ update_portrait('oc003_01 5', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l(-5), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_li21.ogg"
c41 '[convertstrid(1130313)]'
hide p3
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('st053_01 4', 'p1007', [r(-12), light], 6)
c10073 '[convertstrid(1130314)]'
menu:
    extend ""
    "[textdict[1130315]]":
        call avg10313
    "[textdict[1130316]]":
        call avg10314
return