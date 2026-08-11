label avg20089(trans=fade_in):

$ play_music("ed7101.ogg")
scene avg_bg_020
$ update_narrator('c5381')
window show
with trans
get_char('c5381') '[convertstrid(1004491)]' (**arg(1, 1004491))
$ update_portrait('st033_01 2', 'p232', [r(-7), light], 6)
get_char('c2323') '[convertstrid(1004492)]' (**arg(2, 1004492))
$ update_portrait('st033_01 2', 'p232', [r(-7), dark], 5)
get_char('c5381') '[convertstrid(1004493)]' (**arg(3, 1004493))
$ update_portrait('st033_01 4', 'p232', [r(-7), light], 6)
get_char('c2323') '[convertstrid(1004494)]' (**arg(4, 1004494))
$ update_portrait('st033_01 3', 'p232', [r(-7), light], 6)
get_char('c2323') '[convertstrid(1004495)]' (**arg(5, 1004495))
$ update_portrait('st033_01 3', 'p232', [r(-7), dark], 5)
get_char('c5381') '[convertstrid(1004496)]' (**arg(6, 1004496))
$ update_portrait('st033_01 2', 'p232', [r(-7), light], 6)
get_char('c2323') '[convertstrid(1004497)]' (**arg(7, 1004497))
$ update_portrait('st033_01 2', 'p232', [r(-7), dark], 5)
get_char('c5381') '[convertstrid(1004498)]' (**arg(8, 1004498))
get_char('c5381') '[convertstrid(1004499)]' (**arg(9, 1004499))
$ update_portrait('st033_01 3', 'p232', [r(-7), light], 6)
get_char('c2323') '[convertstrid(1004500)]' (**arg(10, 1004500))
$ update_portrait('st033_01 3', 'p232', [r(-7), dark], 5)
get_char('c5381') '[convertstrid(1004501)]' (**arg(11, 1004501))
$ update_portrait('st033_01 3', 'p232', [r(-7), light], 6)
get_char('c2323') '[convertstrid(1004502)]' (**arg(12, 1004502))
hide p232
$ update_narrator('c33')
with fade
$ update_portrait('oc003_01 1', 'p3', [r_entrance(-6), light], 6)
play sfxvoice "avg_vocal_ro02.ogg"
get_char('c33') '[convertstrid(1004503)]' (**arg(13, 1004503))
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li03.ogg"
get_char('c41') '[convertstrid(1004504)]' (**arg(14, 1004504))
hide p3
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 11', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na15.ogg"
get_char('c13') '[convertstrid(1004505)]' (**arg(15, 1004505))
return "avg20089"