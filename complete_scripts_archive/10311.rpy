label avg10311:

play music "ed7105.ogg"
scene avg_bg_022
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
window show
with fade_in
play sfx2 "other_7020.ogg"
c21 '[convertstrid(1130295)]'
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('st053_01 1', 'p1007', [r(-12), light], 5)
c10073 '[convertstrid(1130296)]'
hide p2
$ update_portrait('st053_01 1', 'p1007', [r(-12), dark], 5)
$ update_portrait('oc001_01 6', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1130297)]'
$ update_portrait('oc001_01 6', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('st053_01 2', 'p1007', [r(-12), light], 5)
c10073 '[convertstrid(1130298)]'
hide p1
$ update_portrait('st053_01 2', 'p1007', [r(-12), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1130299)]'
hide p2
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1130300)]'
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('st053_01 5', 'p1007', [r(-12), light], 5)
c10073 '[convertstrid(1130301)]'
$ update_portrait('st053_01 1', 'p1007', [r(-12), light], 5)
c10073 '[convertstrid(1130309)]'
$ update_portrait('st053_01 1', 'p1007', [r(-12), light], 5)
c10073 '[convertstrid(1130310)]'
$ update_portrait('st053_01 1', 'p1007', [r(-12), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1130311)]'
hide p1007
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('oc003_01 5', 'p3', [r(-6), light], 5)
play sfxvoice "avg_vocal_ro05.ogg"
c33 '[convertstrid(1130312)]'
hide p1
$ update_portrait('oc003_01 5', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l(-5), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_li21.ogg"
c41 '[convertstrid(1130313)]'
hide p3
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('st053_01 4', 'p1007', [r(-12), light], 5)
c10073 '[convertstrid(1130314)]'
menu:
    extend ""
    "[textdict[1130315]]":
        call avg10313
    "[textdict[1130316]]":
        call avg10314
return