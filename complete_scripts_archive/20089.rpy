label avg20089:

$ play_music("ed7101.ogg")
scene avg_bg_020
$ update_narrator('c5381')
window show
with fade_in
c5381 '[convertstrid(1004491)]'
$ update_portrait('st033_01 2', 'p232', [r(-7), light], 6)
c2323 '[convertstrid(1004492)]'
$ update_portrait('st033_01 2', 'p232', [r(-7), dark], 5)
c5381 '[convertstrid(1004493)]'
$ update_portrait('st033_01 4', 'p232', [r(-7), light], 6)
c2323 '[convertstrid(1004494)]'
$ update_portrait('st033_01 3', 'p232', [r(-7), light], 6)
c2323 '[convertstrid(1004495)]'
$ update_portrait('st033_01 3', 'p232', [r(-7), dark], 5)
c5381 '[convertstrid(1004496)]'
$ update_portrait('st033_01 2', 'p232', [r(-7), light], 6)
c2323 '[convertstrid(1004497)]'
$ update_portrait('st033_01 2', 'p232', [r(-7), dark], 5)
c5381 '[convertstrid(1004498)]'
c5381 '[convertstrid(1004499)]'
$ update_portrait('st033_01 3', 'p232', [r(-7), light], 6)
c2323 '[convertstrid(1004500)]'
$ update_portrait('st033_01 3', 'p232', [r(-7), dark], 5)
c5381 '[convertstrid(1004501)]'
$ update_portrait('st033_01 3', 'p232', [r(-7), light], 6)
c2323 '[convertstrid(1004502)]'
hide p232
$ update_narrator('c33')
with fade
$ update_portrait('oc003_01 1', 'p3', [r_entrance(-6), light], 6)
play sfxvoice "avg_vocal_ro02.ogg"
c33 '[convertstrid(1004503)]'
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li03.ogg"
c41 '[convertstrid(1004504)]'
hide p3
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 11', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na15.ogg"
c13 '[convertstrid(1004505)]'
return