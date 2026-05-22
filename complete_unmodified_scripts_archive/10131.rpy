label avg10131:

$ play_music("ed7113.ogg")
scene avg_bg_021
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with fade_in
play sfx2 "other_7064.ogg"
c11 '[convertstrid(1007320)]'
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 11', 'p2', [r_entrance(-3), light], 6)
play sfxvoice "avg_vocal_ch18.ogg"
c23 '[convertstrid(1007321)]'
$ update_portrait('oc002_01 11', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1007322)]'
hide p1
hide p2
$ update_narrator('c9683')
with fade
play sfx2 "other_7020.ogg"
c9683 '[convertstrid(1007323)]'
$ update_portrait('oc002_01 1', 'p2', [l_entrance(-3), light, flip], 6)
c21 '[convertstrid(1007324)]'
$ update_portrait('oc002_01 1', 'p2', [l(-3), dark, flip], 5)
c9683 '[convertstrid(1007325)]'
hide p2
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1007326)]'
$ update_portrait('oc001_01 10', 'p1', [l(-2), dark, flip], 5)
c9683 '[convertstrid(1007327)]'
hide p1
$ update_portrait('oc002_01 8', 'p2', [l(-3), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_ch08.ogg"
c21 '[convertstrid(1007328)]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1007329)]'
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 5)
c9683 '[convertstrid(1007330)]'
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1007331)]'
$ update_portrait('oc001_01 17', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1007332)]'
$ update_portrait('oc001_01 17', 'p1', [l(-2), dark, flip], 5)
c9683 '[convertstrid(1007333)]'
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1007334)]'
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1007335)]'
return