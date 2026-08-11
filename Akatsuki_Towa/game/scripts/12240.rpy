label avg12240(trans=fade_in):

$ play_music("ed7102.ogg")
scene avg_bg_015
$ update_narrator('c0')
window show
with trans
play sfx2 "other_7047.ogg"
get_char('c0') '[convertstrid(1121504)]' (**arg(1, 1121504))
$ update_portrait('oc002_01 8', 'p2', [l_entrance(-3), light, flip], 6)
get_char('c21') '[convertstrid(1121218)]' (**arg(2, 1121218))
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 9', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1121505)]' (**arg(3, 1121505))
hide p2
$ update_portrait('oc004_01 9', 'p4', [r(-5), dark], 5)
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1121219)]' (**arg(4, 1121219))
hide p4
$ update_portrait('oc001_01 10', 'p1', [l(-2), dark, flip], 5)
get_char('c9963') '[convertstrid(1121220)]' (**arg(5, 1121220))
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1121221)]' (**arg(6, 1121221))
hide p1
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1121222)]' (**arg(7, 1121222))
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
get_char('c9963') '[convertstrid(1121223)]' (**arg(8, 1121223))
get_char('c9963') '[convertstrid(1121224)]' (**arg(9, 1121224))
hide p2
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1121225)]' (**arg(10, 1121225))
$ update_portrait('oc001_01 10', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 21', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1121226)]' (**arg(11, 1121226))
$ update_portrait('oc002_01 21', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1121227)]' (**arg(12, 1121227))
hide p2
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1121506)]' (**arg(13, 1121506))
$ update_portrait('oc004_01 9', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1121228)]' (**arg(14, 1121228))
hide p1
$ update_portrait('oc004_01 9', 'p4', [r(-5), dark], 5)
get_char('c9961') '[convertstrid(1121229)]' (**arg(15, 1121229))
get_char('c9961') '[convertstrid(1121230)]' (**arg(16, 1121230))
$ update_portrait('oc004_01 9', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1121231)]' (**arg(17, 1121231))
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1121582)]' (**arg(18, 1121582))
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
get_char('c9961') '[convertstrid(1121583)]' (**arg(19, 1121583))
hide p4
$ update_portrait('oc002_01 21', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1121584)]' (**arg(20, 1121584))
$ update_portrait('oc002_01 21', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1121585)]' (**arg(21, 1121585))
return "avg12240"