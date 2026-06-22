label avg20308:

$ play_music("ed7105.ogg")
scene placeholderbackground
$ update_narrator('c10063')
window show
with fade_in
get_char('c10063') '[convertstrid(1130265)]' (**arg(1, 1130265))
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1130266)]' (**arg(2, 1130266))
hide p1
get_char('c10063') '[convertstrid(1130267)]' (**arg(3, 1130267))
get_char('c10063') '[convertstrid(1130268)]' (**arg(4, 1130268))
get_char('c10063') '[convertstrid(1130269)]' (**arg(5, 1130269))
$ update_portrait('oc004_01 2', 'p4', [mid(-5), light], 6)
get_char('c43') '[convertstrid(1130270)]' (**arg(6, 1130270))
hide p4
get_char('c10063') '[convertstrid(1130271)]' (**arg(7, 1130271))
$ update_portrait('oc004_01 2', 'p4', [mid(-5), light], 6)
get_char('c43') '[convertstrid(1130272)]' (**arg(8, 1130272))
hide p4
get_char('c10063') '[convertstrid(1130273)]' (**arg(9, 1130273))
get_char('c10063') '[convertstrid(1130274)]' (**arg(10, 1130274))
$ update_portrait('oc004_01 12', 'p4', [mid(-5), light], 6)
get_char('c43') '[convertstrid(1130275)]' (**arg(11, 1130275))
hide p4
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1130276)]' (**arg(12, 1130276))
hide p1
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1130277)]' (**arg(13, 1130277))
hide p2
$ update_portrait('oc003_01 5', 'p3', [mid(-6), light], 6)
get_char('c33') '[convertstrid(1130278)]' (**arg(14, 1130278))
hide p3
$ update_portrait('oc004_01 7', 'p4', [mid(-5), light], 6)
get_char('c43') '[convertstrid(1130279)]' (**arg(15, 1130279))
hide p4
get_char('c10063') '[convertstrid(1130280)]' (**arg(16, 1130280))
$ update_portrait('oc004_01 5', 'p4', [mid(-5), light], 6)
get_char('c43') '[convertstrid(1130281)]' (**arg(17, 1130281))
hide p4
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1130282)]' (**arg(18, 1130282))
menu:
    extend ""
    '[convertstrid(1130283)]':
        call avg20309
    '[convertstrid(1130284)]':
        call avg20310
return