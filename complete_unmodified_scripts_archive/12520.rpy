label avg12520:

$ play_music("ED6301.ogg")
scene placeholderbackground
$ update_portrait('sc005_01 1', 'p13', [l(-17), light, flip], 6)
$ update_narrator('c131')
window show
with fade_in
get_char('c131') '[convertstrid(1151252)]' (**arg(1, 1151252))
$ update_portrait('sc005_01 1', 'p13', [l(-17), dark, flip], 5)
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1151253)]' (**arg(2, 1151253))
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1151254)]' (**arg(3, 1151254))
hide p3
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1151255)]' (**arg(4, 1151255))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc005_01 1', 'p13', [l(-17), light, flip], 6)
get_char('c131') '[convertstrid(1151256)]' (**arg(5, 1151256))
return